[CmdletBinding(SupportsShouldProcess)]
param(
    [ValidateSet('Audit', 'Plan', 'Apply', 'Verify', 'Restore')]
    [string]$Mode = 'Audit',
    [ValidateSet('Safe', 'Performance', 'Extreme')]
    [string]$Profile = 'Safe',
    [string]$OutputRoot,
    [string]$StatePath,
    [ValidateRange(0.1, 50)]
    [double]$RegressionThresholdPercent = 3,
    [string[]]$ApprovedActionId = @(),
    [switch]$Elevated
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$requestedWhatIf = [bool]$WhatIfPreference
$WhatIfPreference = $false
$modulePath = Join-Path $PSScriptRoot 'WindowsOptimization.Core.psm1'
Import-Module $modulePath -Force

if ([string]::IsNullOrWhiteSpace($OutputRoot)) {
    $OutputRoot = Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'CodexWindowsOptimizerReports'
}

if ($Mode -in @('Apply', 'Restore') -and -not $requestedWhatIf -and -not (Test-WindowsAdministrator)) {
    if ($Elevated) {
        throw 'Elevation was requested, but the child process is not administrator.'
    }
    $arguments = @(
        '-NoProfile'
        '-ExecutionPolicy', 'Bypass'
        '-File', "`"$PSCommandPath`""
        '-Mode', $Mode
        '-Profile', $Profile
        '-OutputRoot', "`"$OutputRoot`""
        '-RegressionThresholdPercent', $RegressionThresholdPercent
        '-Elevated'
    )
    if (-not [string]::IsNullOrWhiteSpace($StatePath)) {
        $arguments += @('-StatePath', "`"$StatePath`"")
    }
    foreach ($id in $ApprovedActionId) {
        $arguments += @('-ApprovedActionId', $id)
    }
    $child = Start-Process -FilePath 'powershell.exe' -ArgumentList $arguments -Verb RunAs `
        -WindowStyle Normal -Wait -PassThru
    exit $child.ExitCode
}

switch ($Mode) {
    'Audit' {
        $inventory = Get-WindowsOptimizationInventory
        $baseline = Get-WindowsPerformanceBaseline
        $plan = New-WindowsOptimizationPlan -Inventory $inventory -Profile $Profile
        $data = [pscustomobject]@{
            Mode = 'Audit'
            Profile = $Profile
            Inventory = $inventory
            Baseline = $baseline
            CandidatePlan = $plan
            SystemChanged = $false
        }
        Export-WindowsOptimizationReport -Data $data -OutputRoot $OutputRoot -Label 'audit'
        break
    }
    'Plan' {
        $inventory = Get-WindowsOptimizationInventory
        $plan = New-WindowsOptimizationPlan -Inventory $inventory -Profile $Profile
        if (-not (Test-WindowsOptimizationPlan -Plan $plan)) {
            throw 'Generated optimization plan did not pass validation.'
        }
        $data = [pscustomobject]@{
            Mode = 'Plan'
            Profile = $Profile
            Plan = $plan
            SystemChanged = $false
        }
        Export-WindowsOptimizationReport -Data $data -OutputRoot $OutputRoot -Label 'plan'
        break
    }
    'Apply' {
        $includeBenchmark = $Profile -eq 'Extreme'
        $inventory = Get-WindowsOptimizationInventory
        $before = Get-WindowsPerformanceBaseline -IncludeBenchmark:$includeBenchmark
        $plan = New-WindowsOptimizationPlan -Inventory $inventory -Profile $Profile
        if (-not (Test-WindowsOptimizationPlan -Plan $plan)) {
            throw 'Generated optimization plan did not pass validation.'
        }

        if ($requestedWhatIf) {
            $preview = Invoke-WindowsOptimizationPlan -Plan $plan -ApprovedActionId $ApprovedActionId -WhatIf
            [pscustomobject]@{
                Mode = 'Apply'
                Profile = $Profile
                WhatIf = $true
                Plan = $plan
                Preview = $preview
            }
            break
        }

        $state = New-WindowsOptimizationState -Plan $plan -Inventory $inventory -Baseline $before -Confirm:$false
        $results = Invoke-WindowsOptimizationPlan -Plan $plan -StatePath $state.StatePath `
            -ApprovedActionId $ApprovedActionId -Confirm:$false
        $after = Get-WindowsPerformanceBaseline -IncludeBenchmark:$includeBenchmark
        $after | ConvertTo-Json -Depth 8 |
            Set-Content -LiteralPath (Join-Path $state.StatePath 'baseline-after.json') -Encoding UTF8
        $comparison = Compare-WindowsPerformanceBaseline -Before $before -After $after
        $regression = Test-WindowsPerformanceRegression -Comparison $comparison `
            -ThresholdPercent $RegressionThresholdPercent
        $rollback = @()
        if ($regression) {
            $rollback = Restore-WindowsOptimizationState -StatePath $state.StatePath -Confirm:$false
        }
        $data = [pscustomobject]@{
            Mode = 'Apply'
            Profile = $Profile
            StatePath = $state.StatePath
            Results = $results
            Before = $before
            After = $after
            Comparison = $comparison
            RegressionDetected = $regression
            Rollback = $rollback
            RebootRecommended = @($results | Where-Object Status -eq 'Applied').Count -gt 0
        }
        $report = Export-WindowsOptimizationReport -Data $data -OutputRoot $OutputRoot -Label 'apply'
        $data | ConvertTo-Json -Depth 12 |
            Set-Content -LiteralPath (Join-Path $state.StatePath 'result.json') -Encoding UTF8
        [pscustomobject]@{ StatePath = $state.StatePath; Report = $report; RegressionDetected = $regression }
        break
    }
    'Verify' {
        if ([string]::IsNullOrWhiteSpace($StatePath)) {
            $latest = Join-Path $env:ProgramData 'CodexWindowsOptimizer\latest.txt'
            if (-not (Test-Path -LiteralPath $latest)) {
                throw 'No prior optimization state was found. Pass -StatePath explicitly.'
            }
            $StatePath = (Get-Content -LiteralPath $latest -Raw).Trim()
        }
        if (-not (Test-WindowsOptimizationState -StatePath $StatePath)) {
            throw "Optimization state is incomplete: $StatePath"
        }
        $before = Get-Content -LiteralPath (Join-Path $StatePath 'baseline-before.json') -Raw | ConvertFrom-Json
        $after = Get-WindowsPerformanceBaseline -IncludeBenchmark:($Profile -eq 'Extreme')
        $comparison = Compare-WindowsPerformanceBaseline -Before $before -After $after
        $data = [pscustomobject]@{
            Mode = 'Verify'
            Profile = $Profile
            StatePath = $StatePath
            Current = $after
            Comparison = $comparison
            RegressionDetected = Test-WindowsPerformanceRegression -Comparison $comparison `
                -ThresholdPercent $RegressionThresholdPercent
            SystemChanged = $false
        }
        Export-WindowsOptimizationReport -Data $data -OutputRoot $OutputRoot -Label 'verify'
        break
    }
    'Restore' {
        if ([string]::IsNullOrWhiteSpace($StatePath)) {
            $latest = Join-Path $env:ProgramData 'CodexWindowsOptimizer\latest.txt'
            if (-not (Test-Path -LiteralPath $latest)) {
                throw 'No prior optimization state was found. Pass -StatePath explicitly.'
            }
            $StatePath = (Get-Content -LiteralPath $latest -Raw).Trim()
        }
        Restore-WindowsOptimizationState -StatePath $StatePath -WhatIf:$requestedWhatIf -Confirm:$false
        break
    }
}
