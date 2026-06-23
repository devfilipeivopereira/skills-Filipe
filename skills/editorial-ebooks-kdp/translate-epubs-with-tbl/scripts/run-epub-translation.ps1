param(
    [Parameter(Mandatory = $true)]
    [string]$InputFile,

    [string]$SourceLang = 'English',
    [string]$TargetLang = 'Portuguese',
    [string]$Provider = 'ollama',
    [string]$Model = 'qwen3:0.6b',
    [string]$ApiEndpoint = 'http://127.0.0.1:11434/api/generate',
    [string]$OutputFile = '',
    [switch]$SkipDefaultQualityFlags,
    [switch]$TextCleanup,
    [switch]$Refine,
    [string]$Glossary = ''
)

$ErrorActionPreference = 'Stop'

$projectRoot = 'C:\Users\filip\TranslateBooksWithLLMs'
$pythonExe = Join-Path $projectRoot 'venv\Scripts\python.exe'
$translateScript = Join-Path $projectRoot 'translate.py'

if (-not (Test-Path -LiteralPath $InputFile)) {
    throw "Input file not found: $InputFile"
}

if ([System.IO.Path]::GetExtension($InputFile).ToLowerInvariant() -ne '.epub') {
    throw "Input must be an .epub file: $InputFile"
}

if (-not (Test-Path -LiteralPath $pythonExe)) {
    throw "Python venv not found: $pythonExe"
}

$args = @(
    $translateScript,
    '-i', $InputFile,
    '-sl', $SourceLang,
    '-tl', $TargetLang,
    '--provider', $Provider,
    '-m', $Model,
    '--api_endpoint', $ApiEndpoint
)

if ($OutputFile -ne '') {
    $args += @('-o', $OutputFile)
}
if ($TextCleanup.IsPresent -or -not $SkipDefaultQualityFlags.IsPresent) {
    $args += '--text-cleanup'
}
if ($Refine.IsPresent -or -not $SkipDefaultQualityFlags.IsPresent) {
    $args += '--refine'
}
if ($Glossary -ne '') {
    $args += @('--glossary', $Glossary)
}

$env:PYTHONUTF8 = '1'

Push-Location $projectRoot
try {
    & $pythonExe @args
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) {
        throw "Translation failed with exit code $exitCode"
    }
}
finally {
    Pop-Location
}
