param(
    [Parameter(Mandatory = $true)]
    [string]$InputFile,

    [string]$Workspace = '',
    [int]$ChunkChars = 1800
)

$ErrorActionPreference = 'Stop'

$projectRoot = 'C:\Users\filip\TranslateBooksWithLLMs'
$pythonExe = Join-Path $projectRoot 'venv\Scripts\python.exe'
$prepareScript = Join-Path $PSScriptRoot 'prepare-assistant-epub-workflow.py'

if (-not (Test-Path -LiteralPath $InputFile)) {
    throw "Input file not found: $InputFile"
}
if ([System.IO.Path]::GetExtension($InputFile).ToLowerInvariant() -ne '.epub') {
    throw "Input must be an .epub file: $InputFile"
}
if (-not (Test-Path -LiteralPath $pythonExe)) {
    throw "Python venv not found: $pythonExe"
}
if (-not (Test-Path -LiteralPath $prepareScript)) {
    throw "Prepare script not found: $prepareScript"
}
if ($ChunkChars -lt 200) {
    throw "ChunkChars must be >= 200"
}

if ($Workspace -eq '') {
    $base = [System.IO.Path]::GetFileNameWithoutExtension($InputFile)
    $parent = [System.IO.Path]::GetDirectoryName($InputFile)
    $ts = Get-Date -Format 'yyyyMMdd-HHmmss'
    $Workspace = Join-Path $parent ($base + '_assistant_workflow_' + $ts)
}

$env:PYTHONUTF8 = '1'

Push-Location $projectRoot
try {
    & $pythonExe $prepareScript --input $InputFile --workspace $Workspace --chunk-chars $ChunkChars
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) {
        throw "Prepare workflow failed with exit code $exitCode"
    }
}
finally {
    Pop-Location
}

