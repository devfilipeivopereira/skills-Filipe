[CmdletBinding()]
param(
    [string]$ProjectRoot = '',
    [switch]$Clean
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$UserHome = [Environment]::GetFolderPath('UserProfile')
if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
    if (-not [string]::IsNullOrWhiteSpace($PSScriptRoot)) {
        $ProjectRoot = Join-Path $PSScriptRoot '..'
    }
    else {
        $ProjectRoot = '.'
    }
}
$ProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path

function Join-UserPath {
    param([string]$RelativePath)
    return (Join-Path $UserHome $RelativePath)
}

function Remove-Diacritics {
    param([string]$Text)
    if ([string]::IsNullOrWhiteSpace($Text)) {
        return ''
    }

    $normalized = $Text.Normalize([Text.NormalizationForm]::FormD)
    $builder = New-Object System.Text.StringBuilder
    foreach ($char in $normalized.ToCharArray()) {
        $category = [Globalization.CharUnicodeInfo]::GetUnicodeCategory($char)
        if ($category -ne [Globalization.UnicodeCategory]::NonSpacingMark) {
            [void]$builder.Append($char)
        }
    }
    return $builder.ToString().Normalize([Text.NormalizationForm]::FormC)
}

function ConvertTo-Slug {
    param([string]$Text)
    $plain = (Remove-Diacritics $Text).ToLowerInvariant()
    $plain = $plain -replace '[^a-z0-9._-]+', '-'
    $plain = $plain -replace '-{2,}', '-'
    $plain = $plain.Trim('-')
    if ([string]::IsNullOrWhiteSpace($plain)) {
        return 'skill'
    }
    return $plain
}

function Read-SkillMetadata {
    param(
        [string]$SkillDirectory
    )

    $skillMd = Join-Path $SkillDirectory 'SKILL.md'
    $raw = Get-Content -LiteralPath $skillMd -Raw -Encoding UTF8
    $meta = @{}

    if ($raw -match "(?s)\A---\s*\r?\n(.*?)\r?\n---") {
        $frontMatter = $Matches[1]
        foreach ($line in ($frontMatter -split "\r?\n")) {
            if ($line -match '^\s*([A-Za-z0-9_-]+)\s*:\s*(.*)\s*$') {
                $key = $Matches[1].Trim().ToLowerInvariant()
                $value = $Matches[2].Trim().Trim('"').Trim("'")
                $meta[$key] = $value
            }
        }
    }

    $name = $null
    $description = ''
    if ($meta.ContainsKey('name')) {
        $name = $meta['name']
    }
    if ($meta.ContainsKey('description')) {
        $description = $meta['description']
    }
    if ([string]::IsNullOrWhiteSpace($name)) {
        $name = Split-Path $SkillDirectory -Leaf
    }

    return [PSCustomObject]@{
        Name = $name
        Description = $description
        Raw = $raw
    }
}

function New-SourceRoot {
    param(
        [string]$RelativePath,
        [string]$Namespace,
        [string]$Kind,
        [int]$Priority
    )

    return [PSCustomObject]@{
        Path = Join-UserPath $RelativePath
        Namespace = $Namespace
        Kind = $Kind
        Priority = $Priority
    }
}

function Get-PluginNamespace {
    param([string]$SkillsRoot)

    $normalized = $SkillsRoot -replace '/', '\'
    $patterns = @(
        '\\openai-curated\\([^\\]+)\\',
        '\\openai-bundled\\([^\\]+)\\',
        '\\openai-primary-runtime\\([^\\]+)\\',
        '\\chatgpt-global\\([^\\]+)\\'
    )
    foreach ($pattern in $patterns) {
        if ($normalized -match $pattern) {
            return (ConvertTo-Slug $Matches[1])
        }
    }

    return 'plugin'
}

function Add-Prefix {
    param(
        [string]$Prefix,
        [string]$Slug
    )

    $cleanPrefix = ConvertTo-Slug $Prefix
    if ($Slug.StartsWith("$cleanPrefix-")) {
        return $Slug
    }
    return "$cleanPrefix-$Slug"
}

function Get-SkillCategory {
    param(
        [string]$PackageBase,
        [string]$SkillName,
        [string]$Description,
        [string]$Namespace,
        [string]$Kind
    )

    $text = "$PackageBase $SkillName $Description $Namespace $Kind"

    if ($PackageBase -match '^(system|superpowers|agents-system)-' -or $Namespace -match '^(system|superpowers|agents-system)$' -or $text -match '\bskill-creator\b|\bskill-installer\b|\bplugin-creator\b|\boptimize-windows\b') {
        return 'sistema-agentes'
    }
    if ($text -match 'kdp|ebook|e-book|epub|\bbook\b|corrigido|transcri|bonus_pdf|ebook_html|kindle|book cover') {
        return 'editorial-ebooks-kdp'
    }
    if ($text -match 'talks|motivational|adam-grant|brene-brown|david-goggins|james-clear|john-maxwell|jordan-peterson|les-brown|mel-robbins|robin-sharma|simon-sinek|steve-jobs|tony-robbins|lecture') {
        return 'palestras-motivacao'
    }
    if ($text -match 'sermon|sermao|sermoes|pregador|pregadores|preaching|preacher|biblia|crista|pastor|homiletic') {
        return 'sermoes-pregacao'
    }
    if ($text -match '\bnature\b|\bacademic\b|\bjournal\b|\bcitation\b|paper-framework|high-impact journal|data availability|reviewer response|submission-grade|manuscript text') {
        return 'academia-nature'
    }
    if ($text -match 'notion|gmail|meeting|knowledge|research|spec|capture|sync') {
        return 'notion-produtividade'
    }
    if ($text -match 'figma|frontend|ui-ux|design|theme|slide|presentation|satori|geist|shadcn') {
        return 'design-figma-frontend'
    }
    if ($text -match 'github|gh-|ci|vercel|deploy|nextjs|react|auth|ai-sdk|swr|cron|workflow|routing|env-vars|browser|playwright|android|turborepo|turbopack|ncc|api|functions|firewall|storage') {
        return 'desenvolvimento-devops'
    }
    if ($text -match 'docx|document|documents|pdf|spreadsheet|spreadsheets|sheet|data|analytics|youtube|video|media|financeiro|excel|csv') {
        return 'documentos-dados-midia'
    }
    if ($text -match 'skill|plugin|openai|agent|template') {
        return 'sistema-agentes'
    }
    if ($text -match 'prompt|fpm|automation') {
        return 'prompts-automacao'
    }

    return 'outras-skills'
}

function ConvertTo-RepoPath {
    param([string]$Path)

    $full = [IO.Path]::GetFullPath($Path)
    if ($full.StartsWith($ProjectRoot, [StringComparison]::OrdinalIgnoreCase)) {
        $full = $full.Substring($ProjectRoot.Length).TrimStart('\', '/')
    }
    return ($full -replace '\\', '/')
}

function Escape-MarkdownCell {
    param([string]$Text)
    if ($null -eq $Text) {
        return ''
    }
    $singleLine = ($Text -replace '\r?\n', ' ').Trim()
    $singleLine = $singleLine -replace '\|', '\|'
    if ($singleLine.Length -gt 150) {
        $singleLine = $singleLine.Substring(0, 147) + '...'
    }
    return $singleLine
}

function Test-PathUnderDirectory {
    param(
        [string]$ChildPath,
        [string]$ParentPath
    )

    $parent = $ParentPath.TrimEnd('\', '/') + '\'
    return $ChildPath.StartsWith($parent, [StringComparison]::OrdinalIgnoreCase)
}

function Test-TextLikeFile {
    param([string]$Path)

    $extension = [IO.Path]::GetExtension($Path).ToLowerInvariant()
    $textExtensions = @(
        '.md',
        '.txt',
        '.json',
        '.yaml',
        '.yml',
        '.py',
        '.ps1',
        '.psm1',
        '.js',
        '.mjs',
        '.cjs',
        '.ts',
        '.tsx',
        '.html',
        '.css',
        '.csv',
        '.xml',
        '.svg',
        '.toml',
        '.ini',
        '.cfg',
        '.conf',
        '.example',
        '.gitignore',
        '.gitattributes'
    )

    if ($textExtensions -contains $extension) {
        return $true
    }

    $leaf = (Split-Path $Path -Leaf).ToLowerInvariant()
    return $leaf -in @('readme', 'license', 'version', 'dockerfile')
}

function Sanitize-TextContent {
    param([string]$Content)

    $sanitized = $Content
    $sanitized = $sanitized -replace '(?i)secret_[a-z0-9]{20,}', 'REDACTED_NOTION_API_TOKEN'
    $sanitized = $sanitized -replace '(?i)ntn_[a-z0-9_=-]{20,}', 'REDACTED_NOTION_API_TOKEN'
    $sanitized = $sanitized -replace 'sk-[A-Za-z0-9_-]{20,}', 'REDACTED_OPENAI_API_KEY'
    $sanitized = $sanitized -replace 'ghp_[A-Za-z0-9]{20,}', 'REDACTED_GITHUB_TOKEN'
    $sanitized = $sanitized -replace 'github_pat_[A-Za-z0-9_]{20,}', 'REDACTED_GITHUB_TOKEN'
    $sanitized = $sanitized -replace 'token_v2=[^''"\s;]+', 'token_v2=REDACTED_NOTION_COOKIE'
    $sanitized = $sanitized -replace 'notion_user_id=[^''"\s;]+', 'notion_user_id=REDACTED_NOTION_USER_ID'
    return $sanitized
}

function Copy-SanitizedFile {
    param(
        [string]$Source,
        [string]$Destination
    )

    Copy-Item -LiteralPath $Source -Destination $Destination -Force

    if (-not (Test-TextLikeFile $Destination)) {
        return
    }

    $fileInfo = Get-Item -LiteralPath $Destination
    if ($fileInfo.Length -gt 5MB) {
        return
    }

    try {
        $content = Get-Content -LiteralPath $Destination -Raw -Encoding UTF8
        $sanitized = Sanitize-TextContent $content
        if ($sanitized -ne $content) {
            $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
            [IO.File]::WriteAllText($Destination, $sanitized, $utf8NoBom)
        }
    }
    catch {
        return
    }
}

function Copy-SkillDirectory {
    param(
        [string]$Source,
        [string]$Destination
    )

    $sourceFull = (Resolve-Path -LiteralPath $Source).Path.TrimEnd('\', '/')
    if (Test-Path -LiteralPath $Destination) {
        Remove-Item -LiteralPath $Destination -Recurse -Force
    }
    New-Item -ItemType Directory -Force -Path $Destination | Out-Null

    $skipSegments = @(
        '.git',
        '.hg',
        '.svn',
        'node_modules',
        '.venv',
        'venv',
        '__pycache__',
        '.pytest_cache',
        '.mypy_cache',
        'outputs',
        'backup',
        'backups',
        '.backup',
        'dist',
        'build',
        '.tmp-skill-build'
    )

    $directories = New-Object 'System.Collections.Generic.Stack[string]'
    $directories.Push($sourceFull)

    while ($directories.Count -gt 0) {
        $current = $directories.Pop()
        $isRoot = $current.Equals($sourceFull, [StringComparison]::OrdinalIgnoreCase)

        if (-not $isRoot) {
            $leaf = (Split-Path $current -Leaf).ToLowerInvariant()
            if ($skipSegments -contains $leaf) {
                continue
            }
            if (Test-Path -LiteralPath (Join-Path $current 'SKILL.md')) {
                continue
            }
        }

        $files = Get-ChildItem -LiteralPath $current -File -Force -ErrorAction SilentlyContinue
        foreach ($file in $files) {
            $fullName = $file.FullName
            $relative = $fullName.Substring($sourceFull.Length).TrimStart('\', '/')
            $target = Join-Path $Destination $relative
            $targetParent = Split-Path $target -Parent
            New-Item -ItemType Directory -Force -Path $targetParent | Out-Null
            Copy-SanitizedFile -Source $fullName -Destination $target
        }

        $childDirectories = Get-ChildItem -LiteralPath $current -Directory -Force -ErrorAction SilentlyContinue
        foreach ($childDirectory in $childDirectories) {
            $directories.Push($childDirectory.FullName)
        }
    }
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
    $content = ($Lines -join [Environment]::NewLine) + [Environment]::NewLine
    Set-Content -LiteralPath $Path -Value $content -Encoding UTF8
}

$directRoots = @(
    New-SourceRoot '.codex\skills' 'local' 'Codex local' 10
    New-SourceRoot '.codex\skills\.system' 'system' 'Codex system' 12
    New-SourceRoot '.codex\superpowers\skills' 'superpowers' 'Superpowers' 14
    New-SourceRoot '.agents\skills' 'agents' 'Agents local' 20
    New-SourceRoot '.agents\skills\.system' 'agents-system' 'Agents system' 22
    New-SourceRoot '.claude\skills' 'claude' 'Claude local' 30
    New-SourceRoot '.cursor\skills' 'cursor' 'Cursor local' 35
    New-SourceRoot '.gemini\skills' 'gemini' 'Gemini local' 40
    New-SourceRoot '.windsurf\skills' 'windsurf' 'Windsurf local' 45
    New-SourceRoot '.codex-2\skills' 'codex-2' 'Codex backup' 50
    New-SourceRoot '.codex-3\skills' 'codex-3' 'Codex backup' 51
    New-SourceRoot '.codex-4\skills' 'codex-4' 'Codex backup' 52
    New-SourceRoot '.codex-5\skills' 'codex-5' 'Codex backup' 53
)

$candidates = New-Object System.Collections.Generic.List[object]
$scannedRoots = New-Object System.Collections.Generic.List[object]

foreach ($root in $directRoots) {
    if (-not (Test-Path -LiteralPath $root.Path)) {
        continue
    }

    $children = @(
        Get-ChildItem -LiteralPath $root.Path -Directory -Force -ErrorAction SilentlyContinue |
            Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') }
    )
    $scannedRoots.Add([PSCustomObject]@{
        path = $root.Path
        namespace = $root.Namespace
        kind = $root.Kind
        direct_skills = $children.Count
    }) | Out-Null

    foreach ($child in $children) {
        $meta = Read-SkillMetadata -SkillDirectory $child.FullName
        $slug = ConvertTo-Slug $meta.Name
        $packageBase = $slug
        if ($root.Namespace -eq 'system' -or $root.Namespace -eq 'agents-system' -or $root.Namespace -eq 'superpowers') {
            $packageBase = Add-Prefix $root.Namespace $slug
        }

        $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $child.FullName 'SKILL.md')).Hash.ToLowerInvariant()
        $category = Get-SkillCategory -PackageBase $packageBase -SkillName $meta.Name -Description $meta.Description -Namespace $root.Namespace -Kind $root.Kind

        $candidates.Add([PSCustomObject]@{
            Name = $meta.Name
            Slug = $slug
            Description = $meta.Description
            SourcePath = $child.FullName
            SourceRoot = $root.Path
            SourceKind = $root.Kind
            Namespace = $root.Namespace
            Priority = $root.Priority
            SkillMdHash = $hash
            PackageBase = $packageBase
            Category = $category
        }) | Out-Null
    }
}

$pluginCacheRoots = @(
    Join-UserPath '.codex\plugins\cache',
    Join-UserPath '.agents\plugins\cache'
)

foreach ($cacheRoot in $pluginCacheRoots) {
    if (-not (Test-Path -LiteralPath $cacheRoot)) {
        continue
    }

    $skillsRoots = @(
        Get-ChildItem -LiteralPath $cacheRoot -Recurse -Directory -Force -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -eq 'skills' }
    )

    foreach ($skillsRoot in $skillsRoots) {
        $namespace = Get-PluginNamespace $skillsRoot.FullName
        $children = @(
            Get-ChildItem -LiteralPath $skillsRoot.FullName -Directory -Force -ErrorAction SilentlyContinue |
                Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') }
        )
        if ($children.Count -eq 0) {
            continue
        }

        $scannedRoots.Add([PSCustomObject]@{
            path = $skillsRoot.FullName
            namespace = $namespace
            kind = 'Plugin cache'
            direct_skills = $children.Count
        }) | Out-Null

        foreach ($child in $children) {
            $meta = Read-SkillMetadata -SkillDirectory $child.FullName
            $slug = ConvertTo-Slug $meta.Name
            $packageBase = Add-Prefix $namespace $slug
            $hash = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $child.FullName 'SKILL.md')).Hash.ToLowerInvariant()
            $category = Get-SkillCategory -PackageBase $packageBase -SkillName $meta.Name -Description $meta.Description -Namespace $namespace -Kind 'Plugin cache'

            $candidates.Add([PSCustomObject]@{
                Name = $meta.Name
                Slug = $slug
                Description = $meta.Description
                SourcePath = $child.FullName
                SourceRoot = $skillsRoot.FullName
                SourceKind = 'Plugin cache'
                Namespace = $namespace
                Priority = 80
                SkillMdHash = $hash
                PackageBase = $packageBase
                Category = $category
            }) | Out-Null
        }
    }
}

if ($candidates.Count -eq 0) {
    throw 'No installable skills were found.'
}

$selectedByContent = New-Object System.Collections.Generic.List[object]
foreach ($group in ($candidates | Group-Object { "$($_.PackageBase)|$($_.SkillMdHash)" })) {
    $preferred = $group.Group | Sort-Object Priority, @{ Expression = { $_.SourcePath.Length } }, SourcePath | Select-Object -First 1
    $duplicateSources = @($group.Group | Sort-Object Priority, SourcePath | ForEach-Object { $_.SourcePath })
    $selectedByContent.Add([PSCustomObject]@{
        Name = $preferred.Name
        Slug = $preferred.Slug
        Description = $preferred.Description
        SourcePath = $preferred.SourcePath
        SourceRoot = $preferred.SourceRoot
        SourceKind = $preferred.SourceKind
        Namespace = $preferred.Namespace
        Priority = $preferred.Priority
        SkillMdHash = $preferred.SkillMdHash
        PackageBase = $preferred.PackageBase
        Category = $preferred.Category
        DuplicateSources = $duplicateSources
    }) | Out-Null
}

$selected = New-Object System.Collections.Generic.List[object]
foreach ($baseGroup in ($selectedByContent | Group-Object PackageBase | Sort-Object Name)) {
    $ordered = @($baseGroup.Group | Sort-Object Priority, SourcePath)
    for ($i = 0; $i -lt $ordered.Count; $i++) {
        $item = $ordered[$i]
        $packageId = $item.PackageBase
        if ($i -gt 0) {
            $packageId = "$($item.PackageBase)--v$($i + 1)"
        }

        $selected.Add([PSCustomObject]@{
            PackageId = $packageId
            Name = $item.Name
            Slug = $item.Slug
            Description = $item.Description
            Category = $item.Category
            SourcePath = $item.SourcePath
            SourceRoot = $item.SourceRoot
            SourceKind = $item.SourceKind
            Namespace = $item.Namespace
            Priority = $item.Priority
            SkillMdHash = $item.SkillMdHash
            DuplicateSources = $item.DuplicateSources
        }) | Out-Null
    }
}

if ($Clean) {
    $pathsToClean = @(
        (Join-Path $ProjectRoot 'skills'),
        (Join-Path $ProjectRoot 'packages'),
        (Join-Path $ProjectRoot 'README.md'),
        (Join-Path $ProjectRoot 'INSTALL.md'),
        (Join-Path $ProjectRoot 'docs\CATALOGO.md'),
        (Join-Path $ProjectRoot 'docs\FONTES.md'),
        (Join-Path $ProjectRoot 'docs\manifest.json'),
        (Join-Path $ProjectRoot 'docs\manifest.csv')
    )
    foreach ($path in $pathsToClean) {
        if (Test-Path -LiteralPath $path) {
            Remove-Item -LiteralPath $path -Recurse -Force
        }
    }
}

$skillsOutputRoot = Join-Path $ProjectRoot 'skills'
$packagesOutputRoot = Join-Path $ProjectRoot 'packages'
$docsRoot = Join-Path $ProjectRoot 'docs'
New-Item -ItemType Directory -Force -Path $skillsOutputRoot, $packagesOutputRoot, $docsRoot | Out-Null

$manifestRows = New-Object System.Collections.Generic.List[object]
$orderedSelected = @($selected | Sort-Object Category, PackageId)
for ($skillIndex = 0; $skillIndex -lt $orderedSelected.Count; $skillIndex++) {
    $skill = $orderedSelected[$skillIndex]
    Write-Host ("[{0}/{1}] {2}" -f ($skillIndex + 1), $orderedSelected.Count, $skill.PackageId)
    $skillDestination = Join-Path (Join-Path $skillsOutputRoot $skill.Category) $skill.PackageId
    $zipDirectory = Join-Path $packagesOutputRoot $skill.Category
    $zipPath = Join-Path $zipDirectory "$($skill.PackageId).zip"

    New-Item -ItemType Directory -Force -Path $zipDirectory | Out-Null
    Copy-SkillDirectory -Source $skill.SourcePath -Destination $skillDestination

    if (Test-Path -LiteralPath $zipPath) {
        Remove-Item -LiteralPath $zipPath -Force
    }
    Compress-Archive -LiteralPath $skillDestination -DestinationPath $zipPath -CompressionLevel Optimal -Force

    $manifestRows.Add([PSCustomObject]@{
        package_id = $skill.PackageId
        skill_name = $skill.Name
        category = $skill.Category
        description = $skill.Description
        source_kind = $skill.SourceKind
        namespace = $skill.Namespace
        source_path = $skill.SourcePath
        copied_path = ConvertTo-RepoPath $skillDestination
        zip_path = ConvertTo-RepoPath $zipPath
        skill_md_sha256 = $skill.SkillMdHash
        duplicate_source_count = $skill.DuplicateSources.Count
        duplicate_sources = $skill.DuplicateSources
    }) | Out-Null
}

$categoryCounts = $manifestRows | Group-Object category | Sort-Object Name
$sourceSummary = $scannedRoots | Sort-Object path
$generatedAt = (Get-Date).ToString('o')

$manifest = [PSCustomObject]@{
    generated_at = $generatedAt
    project_root = $ProjectRoot
    strategy = 'Direct installable skill directories are selected; duplicate SKILL.md content is collapsed; divergent same-name content is retained as versioned package ids.'
    counts = [PSCustomObject]@{
        scanned_roots = $sourceSummary.Count
        discovered_candidates = $candidates.Count
        selected_packages = $manifestRows.Count
        generated_zips = (Get-ChildItem -LiteralPath $packagesOutputRoot -Recurse -Filter '*.zip' -File | Measure-Object).Count
    }
    source_roots = $sourceSummary
    categories = @($categoryCounts | ForEach-Object { [PSCustomObject]@{ category = $_.Name; count = $_.Count } })
    skills = $manifestRows
}

($manifest | ConvertTo-Json -Depth 10) | Set-Content -LiteralPath (Join-Path $docsRoot 'manifest.json') -Encoding UTF8
$manifestRows |
    Select-Object package_id, skill_name, category, description, source_kind, namespace, source_path, copied_path, zip_path, skill_md_sha256, duplicate_source_count |
    Export-Csv -LiteralPath (Join-Path $docsRoot 'manifest.csv') -NoTypeInformation -Encoding UTF8

$readme = @(
    '# Skills Filipe',
    '',
    "Biblioteca organizada de skills locais encontradas nas pastas de IAs do notebook em $generatedAt.",
    '',
    '## O que tem aqui',
    '',
    "- `skills/`: copia organizada das skills instalaveis, separadas por categoria.",
    "- `packages/`: um `.zip` individual por skill para instalacao manual.",
    "- `docs/CATALOGO.md`: catalogo navegavel com nome, categoria, origem e pacote.",
    "- `docs/FONTES.md`: fontes escaneadas e estrategia de deduplicacao.",
    "- `docs/manifest.json` e `docs/manifest.csv`: inventario estruturado.",
    "- `scripts/organize-skills.ps1`: script para regenerar tudo.",
    "- Tokens conhecidos sao redigidos durante a copia para evitar publicar secrets acidentais.",
    '',
    '## Resumo por categoria',
    '',
    '| Categoria | Skills |',
    '|---|---:|'
)
foreach ($category in $categoryCounts) {
    $readme += "| $($category.Name) | $($category.Count) |"
}
$readme += @(
    '',
    '## Como regenerar',
    '',
    '```powershell',
    'powershell -NoProfile -ExecutionPolicy Bypass -File scripts/organize-skills.ps1 -Clean',
    '```',
    '',
    '## Instalacao rapida',
    '',
    'Escolha um pacote em `packages/<categoria>/<skill>.zip` e extraia em uma pasta de skills, por exemplo `C:\Users\filip\.codex\skills`.',
    '',
    'Veja mais detalhes em `INSTALL.md`.'
)
Write-TextFile -Path (Join-Path $ProjectRoot 'README.md') -Lines $readme

$install = @(
    '# Instalacao Individual das Skills',
    '',
    'Cada `.zip` em `packages/` contem uma pasta de skill pronta para copiar ou extrair.',
    '',
    '## Instalar no Codex',
    '',
    '```powershell',
    '$zip = "packages\categoria\nome-da-skill.zip"',
    '$destino = "C:\Users\filip\.codex\skills"',
    'Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force',
    '```',
    '',
    '## Instalar em outra pasta',
    '',
    'Troque `$destino` pela pasta de skills da IA desejada, como `.agents\skills`, `.claude\skills`, `.cursor\skills`, `.gemini\skills` ou `.windsurf\skills`.',
    '',
    '## Observacoes',
    '',
    '- O nome do pacote pode ter prefixos como `vercel-`, `figma-`, `system-` ou `superpowers-` para evitar colisao.',
    '- Pacotes com sufixo `--v2`, `--v3` etc. representam variantes reais com `SKILL.md` diferente.',
    '- A origem exata de cada pacote esta em `docs/manifest.json`.'
)
Write-TextFile -Path (Join-Path $ProjectRoot 'INSTALL.md') -Lines $install

$catalog = @(
    '# Catalogo de Skills',
    '',
    "Gerado em: ``$generatedAt``",
    '',
    "Total de pacotes: **$($manifestRows.Count)**",
    '',
    '| Pacote | Skill | Categoria | Origem | Zip | Descricao |',
    '|---|---|---|---|---|---|'
)
foreach ($row in ($manifestRows | Sort-Object category, package_id)) {
    $packageId = Escape-MarkdownCell $row.package_id
    $skillName = Escape-MarkdownCell $row.skill_name
    $category = Escape-MarkdownCell $row.category
    $sourceKind = Escape-MarkdownCell $row.source_kind
    $namespace = Escape-MarkdownCell $row.namespace
    $zipPath = Escape-MarkdownCell $row.zip_path
    $description = Escape-MarkdownCell $row.description
    $catalog += "| ``$packageId`` | $skillName | ``$category`` | $sourceKind / ``$namespace`` | ``$zipPath`` | $description |"
}
Write-TextFile -Path (Join-Path $docsRoot 'CATALOGO.md') -Lines $catalog

$sources = @(
    '# Fontes Escaneadas',
    '',
    "Gerado em: ``$generatedAt``",
    '',
    '## Estrategia',
    '',
    '- Fonte primaria: `C:\Users\filip\.codex\skills`.',
    '- Tambem foram consideradas pastas `skills` de `.agents`, `.claude`, `.cursor`, `.gemini`, `.windsurf`, backups `.codex-*`, `superpowers` e caches de plugins.',
    '- Apenas filhos diretos de uma pasta `skills` com `SKILL.md` entram como pacotes instalaveis.',
    '- Diretorios descendentes que contem outro `SKILL.md` sao tratados como sub-skills/backups e nao entram recursivamente dentro do pacote pai.',
    '- Duplicatas com mesmo pacote base e mesmo hash de `SKILL.md` foram consolidadas; variantes com hash diferente foram mantidas com `--v2`, `--v3` etc.',
    '- Padroes conhecidos de tokens e cookies sao substituidos por placeholders `REDACTED_*` antes de copiar e compactar.',
    '',
    '## Raizes',
    '',
    '| Raiz | Namespace | Tipo | Skills diretas |',
    '|---|---|---|---:|'
)
foreach ($source in $sourceSummary) {
    $sourcePath = Escape-MarkdownCell $source.path
    $sourceNamespace = Escape-MarkdownCell $source.namespace
    $sourceKind = Escape-MarkdownCell $source.kind
    $sources += "| ``$sourcePath`` | ``$sourceNamespace`` | $sourceKind | $($source.direct_skills) |"
}
$sources += @(
    '',
    '## Contagens',
    '',
    "- Candidatos descobertos: ``$($candidates.Count)``",
    "- Pacotes selecionados: ``$($manifestRows.Count)``",
    "- Zips gerados: ``$((Get-ChildItem -LiteralPath $packagesOutputRoot -Recurse -Filter '*.zip' -File | Measure-Object).Count)``"
)
Write-TextFile -Path (Join-Path $docsRoot 'FONTES.md') -Lines $sources

Write-Host "Discovered candidates: $($candidates.Count)"
Write-Host "Selected packages: $($manifestRows.Count)"
Write-Host "Generated zips: $((Get-ChildItem -LiteralPath $packagesOutputRoot -Recurse -Filter '*.zip' -File | Measure-Object).Count)"
Write-Host "Catalog: $(Join-Path $docsRoot 'CATALOGO.md')"
