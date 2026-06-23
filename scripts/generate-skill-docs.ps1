[CmdletBinding()]
param(
    [string]$ProjectRoot = '',
    [switch]$Clean
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
    if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) {
        $ProjectRoot = Join-Path $PSScriptRoot '..'
    }
    else {
        $ProjectRoot = '.'
    }
}
$ProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path

function ConvertTo-RepoPath {
    param([string]$Path)

    $full = [IO.Path]::GetFullPath($Path)
    if ($full.StartsWith($ProjectRoot, [StringComparison]::OrdinalIgnoreCase)) {
        $full = $full.Substring($ProjectRoot.Length).TrimStart('\', '/')
    }
    return ($full -replace '\\', '/')
}

function ConvertTo-MarkdownLink {
    param(
        [string]$Label,
        [string]$Target
    )

    $safeLabel = $Label -replace '\|', '\|'
    $safeTarget = ($Target -replace '\\', '/') -replace ' ', '%20'
    return "[$safeLabel]($safeTarget)"
}

function ConvertTo-IndexRelativePath {
    param([string]$RepoPath)

    $normalized = ($RepoPath -replace '\\', '/')
    if ($normalized.StartsWith('docs/', [StringComparison]::OrdinalIgnoreCase)) {
        return $normalized.Substring(5)
    }
    return "../$normalized"
}

function Escape-MarkdownCell {
    param([string]$Text)
    if ($null -eq $Text) {
        return ''
    }
    $singleLine = ($Text -replace '\r?\n', ' ').Trim()
    $singleLine = $singleLine -replace '\|', '\|'
    return $singleLine
}

function Format-Bytes {
    param([long]$Bytes)

    if ($Bytes -ge 1GB) {
        return ('{0:N2} GB' -f ($Bytes / 1GB))
    }
    if ($Bytes -ge 1MB) {
        return ('{0:N2} MB' -f ($Bytes / 1MB))
    }
    if ($Bytes -ge 1KB) {
        return ('{0:N1} KB' -f ($Bytes / 1KB))
    }
    return "$Bytes B"
}

function Write-TextFile {
    param(
        [string]$Path,
        [string[]]$Lines
    )

    $parent = Split-Path $Path -Parent
    if (-not [string]::IsNullOrWhiteSpace($parent)) {
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
    }
    $cleanLines = New-Object System.Collections.Generic.List[string]
    foreach ($line in $Lines) {
        if ($null -eq $line) {
            $cleanLines.Add('') | Out-Null
        }
        else {
            foreach ($part in ($line -split '\r?\n', -1)) {
                $cleanLines.Add(($part -replace '[ \t]+$', '')) | Out-Null
            }
        }
    }
    while ($cleanLines.Count -gt 0 -and [string]::IsNullOrWhiteSpace($cleanLines[$cleanLines.Count - 1])) {
        $cleanLines.RemoveAt($cleanLines.Count - 1)
    }
    $content = ($cleanLines -join [Environment]::NewLine) + [Environment]::NewLine
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [IO.File]::WriteAllText($Path, $content, $utf8NoBom)
}

function Get-CodeFence {
    param([string]$Content)

    $max = 3
    foreach ($match in [regex]::Matches($Content, '`+')) {
        if ($match.Value.Length -ge $max) {
            $max = $match.Value.Length + 1
        }
    }
    return ('`' * $max)
}

function Read-SkillFrontMatter {
    param([string]$SkillMdPath)

    $raw = Get-Content -LiteralPath $SkillMdPath -Raw -Encoding UTF8
    $metadata = [ordered]@{}
    $body = $raw
    $frontMatter = ''

    if ($raw -match "(?s)\A---\s*\r?\n(.*?)\r?\n---\s*\r?\n?") {
        $frontMatter = $Matches[1]
        $body = $raw.Substring($Matches[0].Length)
    }

    if (-not [string]::IsNullOrWhiteSpace($frontMatter)) {
        $lines = @($frontMatter -split "\r?\n")
        for ($i = 0; $i -lt $lines.Count; $i++) {
            $line = $lines[$i]
            if ($line -match '^\s*([A-Za-z0-9_-]+)\s*:\s*(.*)\s*$') {
                $key = $Matches[1].Trim()
                $value = $Matches[2].Trim()

                if ($value -in @('>', '>-', '|', '|-')) {
                    $collected = New-Object System.Collections.Generic.List[string]
                    while (($i + 1) -lt $lines.Count) {
                        $next = $lines[$i + 1]
                        if ($next -match '^[A-Za-z0-9_-]+\s*:') {
                            break
                        }
                        $i++
                        if (-not [string]::IsNullOrWhiteSpace($next)) {
                            $collected.Add($next.Trim()) | Out-Null
                        }
                    }
                    $value = ($collected -join ' ')
                }

                $metadata[$key] = $value.Trim('"').Trim("'")
            }
        }
    }

    $headings = @(
        [regex]::Matches($body, '(?m)^(#{1,4})\s+(.+?)\s*$') |
            ForEach-Object {
                [PSCustomObject]@{
                    level = $_.Groups[1].Value.Length
                    title = $_.Groups[2].Value.Trim()
                }
            }
    )

    return [PSCustomObject]@{
        raw = $raw
        front_matter = $frontMatter
        body = $body
        metadata = $metadata
        headings = $headings
    }
}

function Get-DirectoryFileSummary {
    param([string]$Directory)

    $files = @(Get-ChildItem -LiteralPath $Directory -Recurse -File -Force -ErrorAction SilentlyContinue)
    $directories = @(Get-ChildItem -LiteralPath $Directory -Recurse -Directory -Force -ErrorAction SilentlyContinue)
    $totalBytes = 0L
    foreach ($file in $files) {
        $totalBytes += $file.Length
    }

    $topDirectories = @(
        Get-ChildItem -LiteralPath $Directory -Directory -Force -ErrorAction SilentlyContinue |
            ForEach-Object {
                $nestedFiles = @(Get-ChildItem -LiteralPath $_.FullName -Recurse -File -Force -ErrorAction SilentlyContinue)
                $nestedBytes = 0L
                foreach ($nestedFile in $nestedFiles) {
                    $nestedBytes += $nestedFile.Length
                }
                [PSCustomObject]@{
                    name = $_.Name
                    files = $nestedFiles.Count
                    bytes = $nestedBytes
                }
            } |
            Sort-Object name
    )

    $fileRows = @(
        $files |
            Sort-Object FullName |
            ForEach-Object {
                [PSCustomObject]@{
                    path = (ConvertTo-RepoPath $_.FullName)
                    size = (Format-Bytes $_.Length)
                    bytes = $_.Length
                }
            }
    )

    return [PSCustomObject]@{
        file_count = $files.Count
        directory_count = $directories.Count
        total_bytes = $totalBytes
        total_size = Format-Bytes $totalBytes
        top_directories = $topDirectories
        files = $fileRows
    }
}

function Get-CategoryLabel {
    param([string]$Category)

    $labels = @{
        'academia-nature' = 'Academia e Nature'
        'desenvolvimento-devops' = 'Desenvolvimento e DevOps'
        'design-figma-frontend' = 'Design, Figma e Frontend'
        'documentos-dados-midia' = 'Documentos, Dados e Midia'
        'editorial-ebooks-kdp' = 'Editorial, Ebooks e KDP'
        'notion-produtividade' = 'Notion e Produtividade'
        'palestras-motivacao' = 'Palestras e Motivacao'
        'sermoes-pregacao' = 'Sermoes e Pregacao'
        'sistema-agentes' = 'Sistema e Agentes'
    }

    if ($labels.ContainsKey($Category)) {
        return $labels[$Category]
    }
    return $Category
}

$manifestPath = Join-Path $ProjectRoot 'docs\manifest.json'
if (-not (Test-Path -LiteralPath $manifestPath)) {
    throw "Manifest not found: $manifestPath"
}

$manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
$docsRoot = Join-Path $ProjectRoot 'docs'
$skillDocsRoot = Join-Path $docsRoot 'skills'

if ($Clean -and (Test-Path -LiteralPath $skillDocsRoot)) {
    Remove-Item -LiteralPath $skillDocsRoot -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $skillDocsRoot | Out-Null

$generatedAt = (Get-Date).ToString('o')
$docRows = New-Object System.Collections.Generic.List[object]

foreach ($skill in ($manifest.skills | Sort-Object category, package_id)) {
    $skillDirectory = Join-Path $ProjectRoot $skill.copied_path
    $skillMd = Join-Path $skillDirectory 'SKILL.md'
    if (-not (Test-Path -LiteralPath $skillMd)) {
        throw "Missing SKILL.md for $($skill.package_id): $skillMd"
    }

    $parsed = Read-SkillFrontMatter -SkillMdPath $skillMd
    $summary = Get-DirectoryFileSummary -Directory $skillDirectory
    $categoryLabel = Get-CategoryLabel $skill.category
    $docDirectory = Join-Path (Join-Path $skillDocsRoot $skill.category) $skill.package_id
    $docPath = Join-Path $docDirectory 'README.md'
    $repoDocPath = ConvertTo-RepoPath $docPath
    $repoSkillPath = ConvertTo-RepoPath $skillDirectory
    $repoSkillMd = ConvertTo-RepoPath $skillMd
    $repoZipPath = $skill.zip_path
    $zipFullPath = Join-Path $ProjectRoot $skill.zip_path
    $repoZipFullPath = ConvertTo-RepoPath $zipFullPath
    $zipSize = if (Test-Path -LiteralPath $zipFullPath) { Format-Bytes (Get-Item -LiteralPath $zipFullPath).Length } else { 'missing' }

    $metadataName = if ($parsed.metadata.Contains('name')) { $parsed.metadata['name'] } else { $skill.skill_name }
    $metadataDescription = if ($parsed.metadata.Contains('description')) { $parsed.metadata['description'] } else { $skill.description }

    $lines = @(
        "# $($skill.package_id)",
        '',
        "- Categoria: **$categoryLabel** (``$($skill.category)``)",
        "- Nome declarado: ``$metadataName``",
        "- Pacote instalavel: ``$repoZipFullPath``",
        "- Pasta copiada: ``$repoSkillPath``",
        "- Fonte original: ``$($skill.source_path)``",
        "- Hash do ``SKILL.md``: ``$($skill.skill_md_sha256)``",
        '',
        '## Resumo',
        '',
        $metadataDescription,
        '',
        '## Instalacao individual',
        '',
        '```powershell',
        "`$zip = `"$repoZipPath`"",
        "`$destino = `"C:\Users\filip\.codex\skills`"",
        'Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force',
        '```',
        '',
        '## Rastreabilidade',
        '',
        '| Campo | Valor |',
        '|---|---|',
        "| Package ID | ``$($skill.package_id)`` |",
        "| Skill name | ``$($skill.skill_name)`` |",
        "| Categoria | ``$($skill.category)`` |",
        "| Namespace | ``$($skill.namespace)`` |",
        "| Tipo da fonte | $($skill.source_kind) |",
        "| Fonte original | ``$($skill.source_path)`` |",
        "| Pasta no repositorio | ``$repoSkillPath`` |",
        "| Arquivo principal | ``$repoSkillMd`` |",
        "| Zip | ``$repoZipPath`` |",
        "| Tamanho do zip | $zipSize |",
        "| Duplicatas consolidadas | $($skill.duplicate_source_count) |",
        '',
        '## Metadados do SKILL.md',
        '',
        '| Chave | Valor |',
        '|---|---|'
    )

    if ($parsed.metadata.Count -gt 0) {
        foreach ($key in $parsed.metadata.Keys) {
            $value = Escape-MarkdownCell $parsed.metadata[$key]
            $lines += "| ``$key`` | $value |"
        }
    }
    else {
        $lines += '| _sem frontmatter_ | _sem metadados estruturados_ |'
    }

    $lines += @(
        '',
        '## Estrutura do pacote',
        '',
        "| Metrica | Valor |",
        "|---|---:|",
        "| Arquivos | $($summary.file_count) |",
        "| Diretorios | $($summary.directory_count) |",
        "| Tamanho copiado | $($summary.total_size) |",
        ''
    )

    if ($summary.top_directories.Count -gt 0) {
        $lines += @(
            '### Diretorios principais',
            '',
            '| Diretorio | Arquivos | Tamanho |',
            '|---|---:|---:|'
        )
        foreach ($directory in $summary.top_directories) {
            $directoryName = Escape-MarkdownCell $directory.name
            $directorySize = Format-Bytes $directory.bytes
            $lines += "| ``$directoryName`` | $($directory.files) | $directorySize |"
        }
        $lines += ''
    }

    if ($parsed.headings.Count -gt 0) {
        $lines += @(
            '## Secoes internas detectadas',
            ''
        )
        foreach ($heading in $parsed.headings) {
            $indent = if ($heading.level -gt 1) { '  ' * ($heading.level - 1) } else { '' }
            $lines += "- $indent$($heading.title)"
        }
        $lines += ''
    }

    $lines += @(
        '## Arquivos do pacote',
        '',
        '| Arquivo | Tamanho |',
        '|---|---:|'
    )
    foreach ($file in $summary.files) {
        $filePath = Escape-MarkdownCell $file.path
        $lines += "| ``$filePath`` | $($file.size) |"
    }

    if ($skill.duplicate_sources.Count -gt 0) {
        $lines += @(
            '',
            '## Fontes equivalentes consolidadas',
            ''
        )
        foreach ($source in $skill.duplicate_sources) {
            $lines += "- ``$source``"
        }
    }

    $fence = Get-CodeFence $parsed.raw
    $lines += @(
        '',
        '## Conteudo integral do SKILL.md',
        '',
        "$fence" + 'markdown',
        $parsed.raw.TrimEnd(),
        "$fence"
    )

    Write-TextFile -Path $docPath -Lines $lines

    $docRows.Add([PSCustomObject]@{
        package_id = $skill.package_id
        skill_name = $skill.skill_name
        category = $skill.category
        category_label = $categoryLabel
        description = $metadataDescription
        doc_path = $repoDocPath
        copied_path = $repoSkillPath
        zip_path = $repoZipPath
        zip_size = $zipSize
        file_count = $summary.file_count
        total_size = $summary.total_size
        source_kind = $skill.source_kind
        namespace = $skill.namespace
    }) | Out-Null
}

$index = @(
    '# Indice Detalhado de Skills',
    '',
    "Gerado em: ``$generatedAt``",
    '',
    "Total de skills documentadas: **$($docRows.Count)**",
    '',
    '## Como usar este indice',
    '',
    '- Use a tabela geral para localizar rapidamente uma skill por categoria, nome, origem ou pacote zip.',
    '- Abra a pagina individual para ver instalacao, rastreabilidade, estrutura de arquivos e o `SKILL.md` completo.',
    '- Os zips em `packages/` sao instalaveis individualmente.',
    '',
    '## Resumo por categoria',
    '',
    '| Categoria | Skills | Documentacao |',
    '|---|---:|---|'
)

foreach ($group in ($docRows | Group-Object category | Sort-Object Name)) {
    $label = Get-CategoryLabel $group.Name
    $categoryPath = "skills/$($group.Name)"
    $escapedCategoryPath = Escape-MarkdownCell $categoryPath
    $index += "| $label (``$($group.Name)``) | $($group.Count) | ``$escapedCategoryPath`` |"
}

$index += @(
    '',
    '## Tabela geral',
    '',
    '| Skill | Categoria | Origem | Arquivos | Zip | Documentacao | Descricao |',
    '|---|---|---|---:|---|---|---|'
)

foreach ($row in ($docRows | Sort-Object category, package_id)) {
    $description = Escape-MarkdownCell $row.description
    if ($description.Length -gt 180) {
        $description = $description.Substring(0, 177) + '...'
    }
    $docLink = ConvertTo-MarkdownLink 'abrir' (ConvertTo-IndexRelativePath $row.doc_path)
    $zipLink = ConvertTo-MarkdownLink $row.zip_size (ConvertTo-IndexRelativePath $row.zip_path)
    $index += "| ``$($row.package_id)`` | ``$($row.category)`` | $($row.source_kind) / ``$($row.namespace)`` | $($row.file_count) | $zipLink | $docLink | $description |"
}

$index += @(
    '',
    '## Indice por categoria',
    ''
)

foreach ($group in ($docRows | Group-Object category | Sort-Object Name)) {
    $label = Get-CategoryLabel $group.Name
    $index += "### $label (``$($group.Name)``)"
    $index += ''
    foreach ($row in ($group.Group | Sort-Object package_id)) {
        $docLink = ConvertTo-MarkdownLink $row.package_id (ConvertTo-IndexRelativePath $row.doc_path)
        $description = Escape-MarkdownCell $row.description
        if ($description.Length -gt 220) {
            $description = $description.Substring(0, 217) + '...'
        }
        $index += "- $docLink - $description"
    }
    $index += ''
}

Write-TextFile -Path (Join-Path $docsRoot 'INDICE_DETALHADO.md') -Lines $index

$docRows |
    Select-Object package_id, skill_name, category, description, doc_path, copied_path, zip_path, zip_size, file_count, total_size, source_kind, namespace |
    Export-Csv -LiteralPath (Join-Path $docsRoot 'skill-docs.csv') -NoTypeInformation -Encoding UTF8

Write-Host "Generated detailed skill docs: $($docRows.Count)"
Write-Host "Index: $(Join-Path $docsRoot 'INDICE_DETALHADO.md')"
