Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$skillRoot = Split-Path $PSScriptRoot -Parent
$modulePath = Join-Path $skillRoot 'scripts\WindowsOptimization.Core.psm1'
$launcherPath = Join-Path $skillRoot 'scripts\Invoke-WindowsOptimization.ps1'
$skillPath = Join-Path $skillRoot 'SKILL.md'

if (-not (Test-Path -LiteralPath $modulePath)) {
    throw "RED: missing implementation module: $modulePath"
}

Import-Module $modulePath -Force
$script:Passed = 0

function Assert-True {
    param(
        [Parameter(Mandatory)]
        [bool]$Condition,
        [Parameter(Mandatory)]
        [string]$Message
    )
    if (-not $Condition) {
        throw $Message
    }
}

function Invoke-Test {
    param(
        [Parameter(Mandatory)]
        [string]$Name,
        [Parameter(Mandatory)]
        [scriptblock]$Test
    )
    & $Test
    $script:Passed++
    Write-Host "[PASS] $Name"
}

function New-TestInventory {
    param(
        [double]$FreeDiskPercent = 8,
        [object[]]$StartupEntries = @(),
        [object[]]$Services = @(),
        [bool]$WslPresent = $false
    )

    [pscustomobject]@{
        CapturedAt = (Get-Date).ToString('o')
        OperatingSystem = [pscustomobject]@{
            Caption = 'Microsoft Windows 11 Pro'
            Version = '10.0.26100'
            Build = '26100'
            Architecture = '64-bit'
        }
        Computer = [pscustomobject]@{
            Manufacturer = 'Contoso'
            Model = 'Portable 14'
            SystemSku = 'CT-1400'
            TotalMemoryGB = 16
        }
        Bios = [pscustomobject]@{
            Version = '1.0.0'
            ReleaseDate = '2025-01-01'
        }
        Processor = [pscustomobject]@{
            Name = 'Contoso CPU'
            LogicalProcessors = 12
        }
        Disks = @(
            [pscustomobject]@{
                Drive = 'C:'
                MediaType = 'SSD'
                HealthStatus = 'Healthy'
                FreePercent = $FreeDiskPercent
                FreeGB = 36
                SizeGB = 450
            }
        )
        StartupEntries = $StartupEntries
        Services = $Services
        Wsl = [pscustomobject]@{ Present = $WslPresent }
        RemoteAccess = @()
        SecurityProducts = @([pscustomobject]@{ Name = 'Microsoft Defender'; Enabled = $true })
        OptionalFeatures = @()
        AppPackages = @()
        ScheduledTasks = @()
        Events = @()
    }
}

Invoke-Test 'exports the public API' {
    foreach ($name in @(
        'Get-WindowsOptimizationInventory'
        'Get-WindowsPerformanceBaseline'
        'New-WindowsOptimizationPlan'
        'Test-WindowsOptimizationPlan'
        'Get-WindowsForbiddenActions'
        'Compare-WindowsPerformanceBaseline'
        'Test-WindowsPerformanceRegression'
        'New-WindowsOptimizationState'
        'Test-WindowsOptimizationState'
        'Export-WindowsOptimizationReport'
        'Invoke-WindowsOptimizationPlan'
        'Restore-WindowsOptimizationState'
        'Invoke-WindowsMaintenance'
    )) {
        Assert-True ($null -ne (Get-Command $name -ErrorAction SilentlyContinue)) "Missing public command: $name"
    }
}

Invoke-Test 'forbids destructive security and placebo tweaks' {
    $forbidden = Get-WindowsForbiddenActions
    foreach ($name in @(
        'DisableDefender'
        'DisableWindowsUpdate'
        'DisableUac'
        'DisableMitigations'
        'DisablePageFile'
        'DeletePrefetch'
        'ClearEventLogs'
        'DeleteSoftwareDistribution'
        'RemoveEdge'
        'InstallGenericBios'
        'InstallCrossOemThermalDriver'
        'TakeOwnershipOfOemService'
    )) {
        Assert-True ($forbidden -contains $name) "Missing forbidden action: $name"
    }
}

Invoke-Test 'creates an adaptive low disk plan without machine-specific targets' {
    $inventory = New-TestInventory -FreeDiskPercent 8
    $plan = New-WindowsOptimizationPlan -Inventory $inventory -Profile Safe
    Assert-True ($plan.Actions.Action -contains 'InventoryRegenerableCaches') 'Low disk must trigger cache inventory.'
    Assert-True ($plan.Actions.Action -contains 'RunStorageMaintenance') 'Low disk must trigger supported storage maintenance.'
    Assert-True (@($plan.Actions | Where-Object { $_.Target -match 'Contoso|Portable 14|CT-1400' }).Count -eq 0) 'Plan must not turn machine identity into an optimization target.'
    Assert-True ($plan.ProtectedComponents -contains 'Microsoft Defender') 'Defender must be explicitly protected.'
    Assert-True ($plan.ProtectedComponents -contains 'Windows Update') 'Windows Update must be explicitly protected.'
    Assert-True ($plan.ProtectedComponents -contains 'UAC') 'UAC must be explicitly protected.'
}

Invoke-Test 'requires consent before disabling sync or remote access startup' {
    $startup = @(
        [pscustomobject]@{ Name = 'Cloud Sync'; Enabled = $true; Impact = 'High'; IsSecurity = $false; IsRemoteAccess = $false; IsSync = $true; IsOemRequired = $false }
        [pscustomobject]@{ Name = 'Remote Support'; Enabled = $true; Impact = 'High'; IsSecurity = $false; IsRemoteAccess = $true; IsSync = $false; IsOemRequired = $false }
        [pscustomobject]@{ Name = 'Chat Client'; Enabled = $true; Impact = 'High'; IsSecurity = $false; IsRemoteAccess = $false; IsSync = $false; IsOemRequired = $false }
    )
    $plan = New-WindowsOptimizationPlan -Inventory (New-TestInventory -StartupEntries $startup) -Profile Performance
    foreach ($target in @('Cloud Sync', 'Remote Support')) {
        $action = $plan.Actions | Where-Object Target -eq $target | Select-Object -First 1
        Assert-True ($null -ne $action) "Missing startup action for $target"
        Assert-True ($action.RequiresConsent) "$target must require functional consent."
    }
    $chat = $plan.Actions | Where-Object Target -eq 'Chat Client' | Select-Object -First 1
    Assert-True (-not $chat.RequiresConsent) 'Ordinary high-impact startup can be proposed without a functional-choice gate.'
}

Invoke-Test 'preserves security and OEM-required startup entries' {
    $startup = @(
        [pscustomobject]@{ Name = 'Security Tray'; Enabled = $true; Impact = 'Low'; IsSecurity = $true; IsRemoteAccess = $false; IsSync = $false; IsOemRequired = $false }
        [pscustomobject]@{ Name = 'Hotkey Service'; Enabled = $true; Impact = 'Medium'; IsSecurity = $false; IsRemoteAccess = $false; IsSync = $false; IsOemRequired = $true }
    )
    $plan = New-WindowsOptimizationPlan -Inventory (New-TestInventory -StartupEntries $startup) -Profile Extreme
    Assert-True (@($plan.Actions | Where-Object Target -in @('Security Tray', 'Hotkey Service')).Count -eq 0) 'Protected startup entries must not be disabled.'
}

Invoke-Test 'targets only evidenced service failures' {
    $services = @(
        [pscustomobject]@{ Name = 'Broken Updater'; StartMode = 'Auto'; State = 'Running'; HasRepeatedFailures = $true; IsProtected = $false; IsOemProtected = $false; IsOptional = $true }
        [pscustomobject]@{ Name = 'Healthy Service'; StartMode = 'Auto'; State = 'Running'; HasRepeatedFailures = $false; IsProtected = $false; IsOemProtected = $false; IsOptional = $true }
        [pscustomobject]@{ Name = 'OEM Thermal'; StartMode = 'Auto'; State = 'Running'; HasRepeatedFailures = $true; IsProtected = $true; IsOemProtected = $true; IsOptional = $false }
    )
    $plan = New-WindowsOptimizationPlan -Inventory (New-TestInventory -Services $services) -Profile Performance
    Assert-True ($plan.Actions.Target -contains 'Broken Updater') 'Repeated optional service failure should be targeted.'
    Assert-True ($plan.Actions.Target -notcontains 'Healthy Service') 'Healthy service must not be changed without evidence.'
    Assert-True ($plan.Actions.Target -notcontains 'OEM Thermal') 'Protected OEM thermal service must be preserved.'
}

Invoke-Test 'handles missing optional properties and empty collections' {
    $inventory = New-TestInventory
    $inventory.StartupEntries = @([pscustomobject]@{ Name = 'Minimal App'; Enabled = $true })
    $inventory.Services = @()
    $plan = New-WindowsOptimizationPlan -Inventory $inventory -Profile Safe
    Assert-True ($null -ne $plan) 'Planning must tolerate sparse inventory.'
    Assert-True (@($plan.Actions).Count -ge 1) 'Low disk actions should still be present.'
}

Invoke-Test 'detects sustained performance regression' {
    $before = [pscustomobject]@{
        CpuIdleAveragePercent = 7
        AvailableMemoryMB = 8000
        ProcessCount = 240
        FreeDiskGB = 50
        BenchmarkScore = 1000
        NetworkLatencyMs = 20
        CriticalEventCount = 0
    }
    $after = [pscustomobject]@{
        CpuIdleAveragePercent = 6
        AvailableMemoryMB = 8200
        ProcessCount = 230
        FreeDiskGB = 55
        BenchmarkScore = 900
        NetworkLatencyMs = 18
        CriticalEventCount = 0
    }
    $comparison = Compare-WindowsPerformanceBaseline -Before $before -After $after
    Assert-True ([math]::Abs($comparison.BenchmarkChangePercent - (-10)) -lt 0.01) 'Benchmark change must be calculated.'
    Assert-True (Test-WindowsPerformanceRegression -Comparison $comparison -ThresholdPercent 3) 'A ten percent benchmark loss must trigger rollback.'
}

Invoke-Test 'detects network and critical event regressions' {
    $comparison = [pscustomobject]@{
        BenchmarkChangePercent = 1
        NetworkLatencyChangePercent = 60
        NewCriticalEvents = 1
        FunctionalLoss = $false
    }
    Assert-True (Test-WindowsPerformanceRegression -Comparison $comparison -ThresholdPercent 3) 'Network or critical event regression must trigger rollback.'
}

Invoke-Test 'validates complete state and rejects incomplete restore state' {
    $root = Join-Path ([IO.Path]::GetTempPath()) ('optimizer-state-' + [guid]::NewGuid())
    New-Item -ItemType Directory -Path $root | Out-Null
    try {
        $manifest = [pscustomobject]@{
            SchemaVersion = 1
            Complete = $true
            RequiredArtifacts = @('plan.json', 'baseline-before.json')
        }
        $manifest | ConvertTo-Json | Set-Content (Join-Path $root 'manifest.json') -Encoding UTF8
        '{}' | Set-Content (Join-Path $root 'plan.json') -Encoding UTF8
        '{}' | Set-Content (Join-Path $root 'baseline-before.json') -Encoding UTF8
        Assert-True (Test-WindowsOptimizationState -StatePath $root) 'Complete state must validate.'
        Remove-Item (Join-Path $root 'plan.json')
        Assert-True (-not (Test-WindowsOptimizationState -StatePath $root)) 'Missing artifact must invalidate restore state.'
    }
    finally {
        Remove-Item -LiteralPath $root -Recurse -Force -ErrorAction SilentlyContinue
    }
}

Invoke-Test 'creates machine-readable and human-readable reports' {
    $root = Join-Path ([IO.Path]::GetTempPath()) ('optimizer-report-' + [guid]::NewGuid())
    try {
        $result = Export-WindowsOptimizationReport -Data ([pscustomobject]@{ Status = 'Audit'; Count = 3 }) -OutputRoot $root -Label 'test'
        Assert-True (Test-Path -LiteralPath $result.Json) 'JSON report missing.'
        Assert-True (Test-Path -LiteralPath $result.Markdown) 'Markdown report missing.'
        $json = Get-Content -LiteralPath $result.Json -Raw | ConvertFrom-Json
        Assert-True ($json.Status -eq 'Audit') 'JSON report content incorrect.'
    }
    finally {
        Remove-Item -LiteralPath $root -Recurse -Force -ErrorAction SilentlyContinue
    }
}

Invoke-Test 'mutating public commands support WhatIf' {
    foreach ($name in @('Invoke-WindowsOptimizationPlan', 'Restore-WindowsOptimizationState', 'Invoke-WindowsMaintenance')) {
        $command = Get-Command $name
        Assert-True ($command.Parameters.ContainsKey('WhatIf')) "$name must support -WhatIf."
    }
}

Invoke-Test 'launcher has safe visible elevation and five modes' {
    Assert-True (Test-Path -LiteralPath $launcherPath) 'Launcher script missing.'
    $text = Get-Content -LiteralPath $launcherPath -Raw
    foreach ($mode in @('Audit', 'Plan', 'Apply', 'Verify', 'Restore')) {
        Assert-True ($text -match [regex]::Escape("'$mode'")) "Launcher missing mode: $mode"
    }
    Assert-True ($text -match '-WindowStyle\s+Normal') 'Elevation must stay visible.'
    Assert-True ($text -match '\.ExitCode') 'Launcher must return child ExitCode.'
    Assert-True ($text -notmatch '\$LASTEXITCODE.+Start-Process') 'Launcher must not use LASTEXITCODE for Start-Process.'
}

Invoke-Test 'inventory reads StartupApproved instead of assuming every registered command is enabled' {
    $moduleText = Get-Content -LiteralPath $modulePath -Raw
    Assert-True ($moduleText -match 'function\s+Get-StartupEntryApprovalState') 'Startup approval reader is missing.'
    Assert-True ($moduleText -match 'Enabled\s*=\s*Get-StartupEntryApprovalState') 'Inventory must derive Enabled from StartupApproved.'
}

Invoke-Test 'skill content exposes the evidence-first workflow and references' {
    Assert-True (Test-Path -LiteralPath $skillPath) 'SKILL.md missing.'
    $text = Get-Content -LiteralPath $skillPath -Raw
    Assert-True ($text -match 'description:\s+Use when') 'Description must begin with Use when.'
    foreach ($term in @('audit', 'baseline', 'backup', 'consent', 'rollback', 'regression', 'WhatIf')) {
        Assert-True ($text -match $term) "SKILL.md missing keyword: $term"
    }
    foreach ($reference in @(
        'safety-and-rollback.md'
        'diagnosis-and-measurement.md'
        'optimization-catalog.md'
        'oem-drivers-and-firmware.md'
    )) {
        Assert-True (Test-Path -LiteralPath (Join-Path $skillRoot "references\$reference")) "Missing reference: $reference"
        Assert-True ($text -match [regex]::Escape($reference)) "SKILL.md does not route to $reference"
    }
}

Write-Host "All $script:Passed optimizer skill tests passed."
