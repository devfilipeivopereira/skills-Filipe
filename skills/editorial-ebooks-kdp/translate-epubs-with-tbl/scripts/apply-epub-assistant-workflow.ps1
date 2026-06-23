param(
    [Parameter(Mandatory = $true)]
    [string]$Workspace,

    [Parameter(Mandatory = $true)]
    [string]$TranslationsPath,

    [Parameter(Mandatory = $true)]
    [string]$OutputFile,

    [string]$LangTag = 'pt-BR',
    [ValidateSet('auto', 'on', 'off')]
    [string]$PtBrNaturalPass = 'auto'
)

$ErrorActionPreference = 'Stop'

$projectRoot = 'C:\Users\filip\TranslateBooksWithLLMs'
$pythonExe = Join-Path $projectRoot 'venv\Scripts\python.exe'
$applyScript = Join-Path $PSScriptRoot 'apply-assistant-epub-workflow.py'

if (-not (Test-Path -LiteralPath $Workspace)) {
    throw "Workspace not found: $Workspace"
}
if (-not (Test-Path -LiteralPath $TranslationsPath)) {
    throw "Translations path not found: $TranslationsPath"
}
if (-not (Test-Path -LiteralPath $pythonExe)) {
    throw "Python venv not found: $pythonExe"
}
if (-not (Test-Path -LiteralPath $applyScript)) {
    throw "Apply script not found: $applyScript"
}

$env:PYTHONUTF8 = '1'

$args = @(
    $applyScript,
    '--workspace', $Workspace,
    '--translations', $TranslationsPath,
    '--output', $OutputFile,
    '--ptbr-natural-pass', $PtBrNaturalPass
)

if ($LangTag -ne '') {
    $args += @('--lang-tag', $LangTag)
}

Push-Location $projectRoot
try {
    & $pythonExe @args
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) {
        throw "Apply workflow failed with exit code $exitCode"
    }
}
finally {
    Pop-Location
}
