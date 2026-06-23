Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-OptionalValue {
    param(
        [AllowNull()]
        [object]$InputObject,
        [Parameter(Mandatory)]
        [string]$Name,
        [AllowNull()]
        [object]$Default = $null
    )

    if ($null -eq $InputObject) {
        return $Default
    }
    $property = $InputObject.PSObject.Properties[$Name]
    if ($null -eq $property) {
        return $Default
    }
    return $property.Value
}

function ConvertTo-SafeBoolean {
    param(
        [AllowNull()]
        [object]$Value,
        [bool]$Default = $false
    )
    if ($null -eq $Value) {
        return $Default
    }
    if ($Value -is [bool]) {
        return $Value
    }
    if ($Value -is [string]) {
        return $Value -match '^(1|true|yes|enabled|on)$'
    }
    return [bool]$Value
}

function Get-SafePercentChange {
    param(
        [AllowNull()]
        [object]$Before,
        [AllowNull()]
        [object]$After
    )
    if ($null -eq $Before -or $null -eq $After) {
        return $null
    }
    $beforeNumber = [double]$Before
    $afterNumber = [double]$After
    if ([math]::Abs($beforeNumber) -lt 0.000001) {
        return $null
    }
    return [math]::Round((($afterNumber - $beforeNumber) / $beforeNumber) * 100, 2)
}

function Test-WindowsAdministrator {
    [CmdletBinding()]
    param()

    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = [Security.Principal.WindowsPrincipal]::new($identity)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Get-WindowsForbiddenActions {
    [CmdletBinding()]
    param()

    return @(
        'DisableDefender'
        'DisableWindowsUpdate'
        'DisableUac'
        'DisableMitigations'
        'DisablePageFile'
        'DisableSearchWithoutEvidence'
        'DisableSysMainWithoutEvidence'
        'DeletePrefetch'
        'ClearEventLogs'
        'DeleteSoftwareDistribution'
        'RemoveEdge'
        'InstallGenericBios'
        'InstallCrossOemThermalDriver'
        'TakeOwnershipOfOemService'
        'KillGenericDeveloperProcesses'
        'DeletePersonalDataAsCache'
    )
}

function Get-StartupEntryApprovalState {
    param(
        [Parameter(Mandatory)]
        [string]$Name,
        [bool]$Default = $true
    )

    $candidateNames = @($Name)
    if (-not $Name.EndsWith('.lnk', [StringComparison]::OrdinalIgnoreCase)) {
        $candidateNames += "$Name.lnk"
    }
    foreach ($path in Get-StartupApprovedPaths) {
        if (-not (Test-Path -LiteralPath $path)) {
            continue
        }
        $item = Get-ItemProperty -LiteralPath $path
        foreach ($candidate in $candidateNames) {
            $property = $item.PSObject.Properties[$candidate]
            if ($null -eq $property) {
                continue
            }
            try {
                $bytes = [byte[]]$property.Value
                if ($bytes.Length -gt 0) {
                    return $bytes[0] -eq 2
                }
            }
            catch {
                return $Default
            }
        }
    }
    return $Default
}

function Get-WindowsPerformanceBaseline {
    [CmdletBinding()]
    param(
        [ValidateRange(1, 30)]
        [int]$SampleCount = 5,
        [ValidateRange(100, 5000)]
        [int]$SampleIntervalMilliseconds = 500,
        [switch]$IncludeBenchmark,
        [ValidateRange(1, 5)]
        [int]$BenchmarkRounds = 3,
        [ValidateRange(1, 30)]
        [int]$BenchmarkSeconds = 3
    )

    $cpuSamples = [System.Collections.Generic.List[double]]::new()
    $diskSamples = [System.Collections.Generic.List[double]]::new()
    for ($index = 0; $index -lt $SampleCount; $index++) {
        try {
            $cpu = Get-CimInstance Win32_PerfFormattedData_PerfOS_Processor -Filter "Name='_Total'" -ErrorAction Stop
            $cpuSamples.Add([double]$cpu.PercentProcessorTime)
        }
        catch {
        }
        try {
            $disk = Get-CimInstance Win32_PerfFormattedData_PerfDisk_PhysicalDisk -Filter "Name='_Total'" -ErrorAction Stop
            $diskSamples.Add([double]$disk.PercentDiskTime)
        }
        catch {
        }
        if ($index -lt ($SampleCount - 1)) {
            Start-Sleep -Milliseconds $SampleIntervalMilliseconds
        }
    }

    $os = Get-CimInstance Win32_OperatingSystem
    $memory = Get-CimInstance Win32_PerfFormattedData_PerfOS_Memory -ErrorAction SilentlyContinue
    $drive = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'" -ErrorAction SilentlyContinue
    $criticalEvents = @(
        Get-WinEvent -FilterHashtable @{
            LogName = 'System'
            StartTime = (Get-Date).AddHours(-24)
            Level = 1, 2
        } -ErrorAction SilentlyContinue |
            Where-Object {
                $_.Id -in @(7, 41, 51, 55, 129, 153, 219, 1001, 7000, 7009, 7011, 7031, 7034)
            }
    )

    $latency = $null
    try {
        $ping = Test-Connection -ComputerName '1.1.1.1' -Count 2 -ErrorAction Stop
        $latency = [math]::Round(($ping.ResponseTime | Measure-Object -Average).Average, 2)
    }
    catch {
    }

    $benchmarkScore = $null
    if ($IncludeBenchmark) {
        $scores = [System.Collections.Generic.List[double]]::new()
        for ($round = 1; $round -le $BenchmarkRounds; $round++) {
            $buffer = New-Object byte[] (1MB)
            [Random]::new().NextBytes($buffer)
            $sha = [Security.Cryptography.SHA256]::Create()
            $watch = [Diagnostics.Stopwatch]::StartNew()
            $iterations = 0L
            try {
                while ($watch.Elapsed.TotalSeconds -lt $BenchmarkSeconds) {
                    $null = $sha.ComputeHash($buffer)
                    $iterations++
                }
            }
            finally {
                $sha.Dispose()
                $watch.Stop()
            }
            $scores.Add([math]::Round($iterations / $watch.Elapsed.TotalSeconds, 2))
        }
        $ordered = @($scores | Sort-Object)
        if ($ordered.Count -gt 0) {
            if ($ordered.Count % 2) {
                $benchmarkScore = $ordered[[math]::Floor($ordered.Count / 2)]
            }
            else {
                $benchmarkScore = ($ordered[$ordered.Count / 2 - 1] + $ordered[$ordered.Count / 2]) / 2
            }
        }
    }

    $cpuAverage = if ($cpuSamples.Count -gt 0) {
        [math]::Round(($cpuSamples | Measure-Object -Average).Average, 2)
    }
    else {
        $null
    }
    $diskAverage = if ($diskSamples.Count -gt 0) {
        [math]::Round(($diskSamples | Measure-Object -Average).Average, 2)
    }
    else {
        $null
    }

    [pscustomobject]@{
        CapturedAt = (Get-Date).ToString('o')
        LastBoot = $os.LastBootUpTime
        CpuIdleAveragePercent = $cpuAverage
        AvailableMemoryMB = if ($null -ne $memory) { [int]$memory.AvailableMBytes } else { $null }
        CommittedMemoryPercent = if ($null -ne $memory) { [int]$memory.PercentCommittedBytesInUse } else { $null }
        ProcessCount = @(Get-Process).Count
        FreeDiskGB = if ($null -ne $drive) { [math]::Round($drive.FreeSpace / 1GB, 2) } else { $null }
        FreeDiskPercent = if ($null -ne $drive -and $drive.Size -gt 0) {
            [math]::Round(($drive.FreeSpace / $drive.Size) * 100, 2)
        }
        else {
            $null
        }
        DiskActiveAveragePercent = $diskAverage
        BenchmarkScore = $benchmarkScore
        NetworkLatencyMs = $latency
        CriticalEventCount = $criticalEvents.Count
        ActivePowerScheme = ((& powercfg.exe /getactivescheme 2>$null) -join ' ').Trim()
    }
}

function Get-WindowsOptimizationInventory {
    [CmdletBinding()]
    param(
        [ValidateRange(1, 90)]
        [int]$EventLookbackDays = 7
    )

    $os = Get-CimInstance Win32_OperatingSystem
    $computer = Get-CimInstance Win32_ComputerSystem
    $bios = Get-CimInstance Win32_BIOS
    $processor = Get-CimInstance Win32_Processor | Select-Object -First 1

    $physicalHealth = @{}
    try {
        foreach ($disk in @(Get-PhysicalDisk -ErrorAction Stop)) {
            $physicalHealth[$disk.FriendlyName] = [pscustomobject]@{
                MediaType = $disk.MediaType.ToString()
                HealthStatus = $disk.HealthStatus.ToString()
                OperationalStatus = ($disk.OperationalStatus -join ',')
            }
        }
    }
    catch {
    }

    $disks = @(
        Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=3' | ForEach-Object {
            [pscustomobject]@{
                Drive = $_.DeviceID
                VolumeName = $_.VolumeName
                FileSystem = $_.FileSystem
                SizeGB = [math]::Round($_.Size / 1GB, 2)
                FreeGB = [math]::Round($_.FreeSpace / 1GB, 2)
                FreePercent = if ($_.Size -gt 0) { [math]::Round(($_.FreeSpace / $_.Size) * 100, 2) } else { 0 }
                MediaType = 'Unknown'
                HealthStatus = 'Unknown'
            }
        }
    )

    $startupEntries = @(
        Get-CimInstance Win32_StartupCommand -ErrorAction SilentlyContinue | ForEach-Object {
            $identity = "$($_.Name) $($_.Command)"
            [pscustomobject]@{
                Name = $_.Name
                Command = $_.Command
                Location = $_.Location
                User = $_.User
                Enabled = Get-StartupEntryApprovalState -Name $_.Name
                Impact = 'Unknown'
                IsSecurity = $identity -match 'SecurityHealth|Windows Security|Defender'
                IsRemoteAccess = $identity -match 'TeamViewer|AnyDesk|RustDesk|ScreenConnect|Splashtop|RemotePC'
                IsSync = $identity -match 'OneDrive|Dropbox|Box|Google Drive|DriveFS|iCloud|Syncthing'
                IsOemRequired = $identity -match 'Hotkey|SystemSupport|System Support|SettingsService|ControlCenter'
            }
        }
    )

    $serviceFailureEvents = @(
        Get-WinEvent -FilterHashtable @{
            LogName = 'System'
            ProviderName = 'Service Control Manager'
            StartTime = (Get-Date).AddDays(-$EventLookbackDays)
        } -ErrorAction SilentlyContinue |
            Where-Object Id -in @(7000, 7009, 7011, 7031, 7034)
    )
    $services = @(
        Get-CimInstance Win32_Service | ForEach-Object {
            $serviceName = $_.Name
            $displayName = $_.DisplayName
            $failures = @($serviceFailureEvents | Where-Object {
                $_.Message -match [regex]::Escape($serviceName) -or
                $_.Message -match [regex]::Escape($displayName)
            }).Count
            $identity = "$serviceName $displayName $($_.PathName)"
            [pscustomobject]@{
                Name = $serviceName
                DisplayName = $displayName
                State = $_.State
                StartMode = $_.StartMode
                PathName = $_.PathName
                FailureCount = $failures
                HasRepeatedFailures = $failures -ge 2
                IsProtected = $identity -match 'WinDefend|wuauserv|WSearch|SysMain|SecurityHealth|WdNisSvc|mpssvc|EventLog|RpcSs'
                IsOemProtected = $identity -match 'Thermal|Dynamic Tuning|Innovation Platform|Hotkey|System Support|Firmware'
                IsOptional = $identity -match 'Updater|Update Service|Telemetry|Assistant|Cloud|Companion'
            }
        }
    )

    $wslPresent = $null -ne (Get-Command wsl.exe -ErrorAction SilentlyContinue)
    $wslDistributions = @()
    if ($wslPresent) {
        try {
            $wslDistributions = @(& wsl.exe --list --quiet 2>$null | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
        }
        catch {
        }
    }

    $securityProducts = @()
    try {
        $securityProducts = @(
            Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntiVirusProduct -ErrorAction Stop |
                ForEach-Object {
                    [pscustomobject]@{
                        Name = $_.displayName
                        ProductState = $_.productState
                    }
                }
        )
    }
    catch {
    }

    $optionalFeatures = @()
    try {
        $optionalFeatures = @(
            Get-WindowsOptionalFeature -Online -ErrorAction Stop |
                Select-Object FeatureName, State
        )
    }
    catch {
    }

    $appPackages = @()
    try {
        $appPackages = @(Get-AppxPackage -ErrorAction Stop | Select-Object Name, PackageFullName, Publisher)
    }
    catch {
    }

    $scheduledTasks = @()
    try {
        $scheduledTasks = @(
            Get-ScheduledTask -ErrorAction Stop |
                Select-Object TaskPath, TaskName, State
        )
    }
    catch {
    }

    $events = @(
        Get-WinEvent -FilterHashtable @{
            LogName = 'System'
            StartTime = (Get-Date).AddDays(-$EventLookbackDays)
        } -ErrorAction SilentlyContinue |
            Where-Object {
                $_.Id -in @(7, 37, 41, 51, 55, 129, 153, 219, 1001, 7000, 7009, 7011, 7031, 7034)
            } |
            Select-Object TimeCreated, Id, ProviderName, LevelDisplayName, Message
    )

    $trimStatus = $null
    try {
        $trimStatus = ((& fsutil.exe behavior query DisableDeleteNotify 2>$null) -join [Environment]::NewLine).Trim()
    }
    catch {
    }

    [pscustomobject]@{
        SchemaVersion = 1
        CapturedAt = (Get-Date).ToString('o')
        OperatingSystem = [pscustomobject]@{
            Caption = $os.Caption
            Version = $os.Version
            Build = $os.BuildNumber
            Architecture = $os.OSArchitecture
            LastBoot = $os.LastBootUpTime
        }
        Computer = [pscustomobject]@{
            Manufacturer = $computer.Manufacturer
            Model = $computer.Model
            SystemSku = $computer.SystemSKUNumber
            TotalMemoryGB = [math]::Round($computer.TotalPhysicalMemory / 1GB, 2)
        }
        Bios = [pscustomobject]@{
            Manufacturer = $bios.Manufacturer
            Version = $bios.SMBIOSBIOSVersion
            SerialNumber = $bios.SerialNumber
            ReleaseDate = $bios.ReleaseDate
        }
        Processor = [pscustomobject]@{
            Name = $processor.Name
            Manufacturer = $processor.Manufacturer
            Cores = $processor.NumberOfCores
            LogicalProcessors = $processor.NumberOfLogicalProcessors
            MaxClockMHz = $processor.MaxClockSpeed
        }
        Disks = $disks
        PhysicalDiskHealth = $physicalHealth
        TrimStatus = $trimStatus
        PageFiles = @(Get-CimInstance Win32_PageFileUsage -ErrorAction SilentlyContinue | Select-Object Name, AllocatedBaseSize, CurrentUsage, PeakUsage)
        StartupEntries = $startupEntries
        Services = $services
        Wsl = [pscustomobject]@{
            Present = $wslPresent
            Distributions = $wslDistributions
            ConfigPath = Join-Path $env:USERPROFILE '.wslconfig'
        }
        RemoteAccess = @($startupEntries | Where-Object IsRemoteAccess)
        SecurityProducts = $securityProducts
        OptionalFeatures = $optionalFeatures
        AppPackages = $appPackages
        ScheduledTasks = $scheduledTasks
        Events = $events
        ActivePowerScheme = ((& powercfg.exe /getactivescheme 2>$null) -join ' ').Trim()
    }
}

function New-OptimizationAction {
    param(
        [Parameter(Mandatory)]
        [string]$Category,
        [Parameter(Mandatory)]
        [string]$Action,
        [Parameter(Mandatory)]
        [string]$Target,
        [Parameter(Mandatory)]
        [string]$Evidence,
        [ValidateSet('Low', 'Medium', 'High', 'Critical')]
        [string]$Risk = 'Low',
        [bool]$RequiresAdmin = $false,
        [bool]$RequiresConsent = $false,
        [string]$Backup = 'Not required',
        [string]$Verification = 'Re-audit target state',
        [string]$Restore = 'Not required'
    )

    [pscustomobject]@{
        Id = [guid]::NewGuid().ToString('n')
        Category = $Category
        Action = $Action
        Target = $Target
        Evidence = $Evidence
        Risk = $Risk
        RequiresAdmin = $RequiresAdmin
        RequiresConsent = $RequiresConsent
        Backup = $Backup
        Verification = $Verification
        Restore = $Restore
    }
}

function New-WindowsOptimizationPlan {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [pscustomobject]$Inventory,
        [ValidateSet('Safe', 'Performance', 'Extreme')]
        [string]$Profile = 'Safe'
    )

    $actions = [System.Collections.Generic.List[object]]::new()
    $systemDrive = @((Get-OptionalValue $Inventory 'Disks' @()) | Where-Object Drive -eq 'C:' | Select-Object -First 1)
    if ($systemDrive.Count -gt 0) {
        $freePercent = [double](Get-OptionalValue $systemDrive[0] 'FreePercent' 100)
        if ($freePercent -lt 12) {
            $actions.Add((New-OptimizationAction -Category 'Storage' -Action 'InventoryRegenerableCaches' `
                -Target 'System drive caches' -Evidence "System drive has $freePercent percent free." `
                -Risk 'Low' -Verification 'Report cache candidates without deleting personal data.'))
            $actions.Add((New-OptimizationAction -Category 'Storage' -Action 'RunStorageMaintenance' `
                -Target 'System drive' -Evidence "System drive has $freePercent percent free." `
                -Risk 'Low' -RequiresAdmin $true -Backup 'Record TRIM and disk health state.' `
                -Verification 'Verify disk health, TRIM and free space.' -Restore 'No data deletion is performed.'))
        }
        if ($freePercent -lt 8) {
            $actions.Add((New-OptimizationAction -Category 'Storage' -Action 'ReviewHibernate' `
                -Target 'Hibernation and Fast Startup' -Evidence "System drive has critically low free space: $freePercent percent." `
                -Risk 'Medium' -RequiresAdmin $true -RequiresConsent $true `
                -Backup 'Record current hibernation state.' -Verification 'Verify hiberfil.sys and user preference.' `
                -Restore 'Run powercfg /hibernate on if previously enabled.'))
        }
    }

    $startupEntries = @((Get-OptionalValue $Inventory 'StartupEntries' @()))
    foreach ($entry in $startupEntries) {
        $enabled = ConvertTo-SafeBoolean (Get-OptionalValue $entry 'Enabled' $true) $true
        $isSecurity = ConvertTo-SafeBoolean (Get-OptionalValue $entry 'IsSecurity' $false)
        $isOemRequired = ConvertTo-SafeBoolean (Get-OptionalValue $entry 'IsOemRequired' $false)
        if (-not $enabled -or $isSecurity -or $isOemRequired) {
            continue
        }
        $impact = [string](Get-OptionalValue $entry 'Impact' 'Unknown')
        $isRemote = ConvertTo-SafeBoolean (Get-OptionalValue $entry 'IsRemoteAccess' $false)
        $isSync = ConvertTo-SafeBoolean (Get-OptionalValue $entry 'IsSync' $false)
        $shouldTarget = $Profile -in @('Performance', 'Extreme') -or $impact -eq 'High'
        if (-not $shouldTarget) {
            continue
        }
        $name = [string](Get-OptionalValue $entry 'Name' 'Unnamed startup entry')
        $actions.Add((New-OptimizationAction -Category 'Startup' -Action 'DisableStartupEntry' `
            -Target $name -Evidence "Enabled startup entry; reported impact: $impact." `
            -Risk 'Low' -RequiresConsent ($isRemote -or $isSync) `
            -Backup 'Export startup registry and record command.' `
            -Verification 'Confirm entry is disabled after login.' `
            -Restore 'Import startup registry or re-enable the entry.'))
    }

    $services = @((Get-OptionalValue $Inventory 'Services' @()))
    foreach ($service in $services) {
        $hasFailures = ConvertTo-SafeBoolean (Get-OptionalValue $service 'HasRepeatedFailures' $false)
        $isProtected = ConvertTo-SafeBoolean (Get-OptionalValue $service 'IsProtected' $false)
        $isOemProtected = ConvertTo-SafeBoolean (Get-OptionalValue $service 'IsOemProtected' $false)
        $isOptional = ConvertTo-SafeBoolean (Get-OptionalValue $service 'IsOptional' $false)
        if (-not $hasFailures -or $isProtected -or $isOemProtected -or -not $isOptional) {
            continue
        }
        $name = [string](Get-OptionalValue $service 'Name' 'Unnamed service')
        $failureCount = Get-OptionalValue $service 'FailureCount' 'multiple'
        $actions.Add((New-OptimizationAction -Category 'Services' -Action 'SetServiceManual' `
            -Target $name -Evidence "Optional service has $failureCount recent failures." `
            -Risk 'Medium' -RequiresAdmin $true -RequiresConsent $true `
            -Backup 'Record service start mode and running state.' `
            -Verification 'Verify service no longer delays boot and starts on demand.' `
            -Restore 'Restore original start mode and running state.'))
    }

    $wsl = Get-OptionalValue $Inventory 'Wsl' $null
    if ($Profile -in @('Performance', 'Extreme') -and (ConvertTo-SafeBoolean (Get-OptionalValue $wsl 'Present' $false))) {
        $actions.Add((New-OptimizationAction -Category 'Development' -Action 'ConfigureWslMemoryReclaim' `
            -Target 'WSL 2 memory reclamation' -Evidence 'WSL is installed and may retain file cache memory.' `
            -Risk 'Low' -RequiresConsent $true -Backup 'Copy the existing .wslconfig when present.' `
            -Verification 'Verify WSL starts and returns idle memory.' -Restore 'Restore the original .wslconfig.'))
    }

    if ($Profile -eq 'Extreme') {
        $actions.Add((New-OptimizationAction -Category 'Power' -Action 'BenchmarkPowerExperiment' `
            -Target 'AC processor energy preference and boost' `
            -Evidence 'Extreme profile requested; power changes require sustained before/after measurement.' `
            -Risk 'High' -RequiresAdmin $true -RequiresConsent $true `
            -Backup 'Export active scheme and all changed AC/DC values.' `
            -Verification 'Run at least three sustained benchmark rounds and inspect thermal/power events.' `
            -Restore 'Automatically restore if the median regresses beyond the configured threshold.'))
    }

    $actions.Add((New-OptimizationAction -Category 'Drivers' -Action 'AuditOfficialDriversAndFirmware' `
        -Target 'Exact computer model and system SKU' `
        -Evidence 'Firmware and platform drivers are hardware-specific.' `
        -Risk 'Low' -Verification 'Compare installed versions with OEM or Windows Update offers.'))

    [pscustomobject]@{
        SchemaVersion = 1
        CreatedAt = (Get-Date).ToString('o')
        Profile = $Profile
        Machine = [pscustomobject]@{
            Manufacturer = Get-OptionalValue (Get-OptionalValue $Inventory 'Computer' $null) 'Manufacturer' 'Unknown'
            Model = Get-OptionalValue (Get-OptionalValue $Inventory 'Computer' $null) 'Model' 'Unknown'
            SystemSku = Get-OptionalValue (Get-OptionalValue $Inventory 'Computer' $null) 'SystemSku' 'Unknown'
        }
        ProtectedComponents = @(
            'Microsoft Defender'
            'Windows Update'
            'UAC'
            'DEP/ASLR/CFG mitigations'
            'Page file'
            'Windows Search unless evidence proves a fault'
            'SysMain unless evidence proves a fault'
            'Event logs'
            'Prefetch'
        )
        ForbiddenActions = Get-WindowsForbiddenActions
        Actions = @($actions)
    }
}

function Test-WindowsOptimizationPlan {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [pscustomobject]$Plan
    )

    if ((Get-OptionalValue $Plan 'SchemaVersion' 0) -ne 1) {
        return $false
    }
    $forbidden = @(Get-WindowsForbiddenActions)
    foreach ($action in @((Get-OptionalValue $Plan 'Actions' @()))) {
        foreach ($required in @('Id', 'Category', 'Action', 'Target', 'Evidence', 'Risk', 'RequiresAdmin', 'RequiresConsent', 'Backup', 'Verification', 'Restore')) {
            if ($null -eq $action.PSObject.Properties[$required]) {
                return $false
            }
        }
        if ($forbidden -contains $action.Action) {
            return $false
        }
    }
    return $true
}

function Compare-WindowsPerformanceBaseline {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [pscustomobject]$Before,
        [Parameter(Mandatory)]
        [pscustomobject]$After,
        [bool]$FunctionalLoss = $false
    )

    $beforeBenchmark = Get-OptionalValue $Before 'BenchmarkScore' $null
    $afterBenchmark = Get-OptionalValue $After 'BenchmarkScore' $null
    $beforeLatency = Get-OptionalValue $Before 'NetworkLatencyMs' $null
    $afterLatency = Get-OptionalValue $After 'NetworkLatencyMs' $null
    $beforeEvents = [int](Get-OptionalValue $Before 'CriticalEventCount' 0)
    $afterEvents = [int](Get-OptionalValue $After 'CriticalEventCount' 0)

    [pscustomobject]@{
        CapturedAt = (Get-Date).ToString('o')
        CpuIdleChangePercent = Get-SafePercentChange (Get-OptionalValue $Before 'CpuIdleAveragePercent' $null) (Get-OptionalValue $After 'CpuIdleAveragePercent' $null)
        AvailableMemoryChangePercent = Get-SafePercentChange (Get-OptionalValue $Before 'AvailableMemoryMB' $null) (Get-OptionalValue $After 'AvailableMemoryMB' $null)
        ProcessCountChangePercent = Get-SafePercentChange (Get-OptionalValue $Before 'ProcessCount' $null) (Get-OptionalValue $After 'ProcessCount' $null)
        FreeDiskChangePercent = Get-SafePercentChange (Get-OptionalValue $Before 'FreeDiskGB' $null) (Get-OptionalValue $After 'FreeDiskGB' $null)
        BenchmarkChangePercent = Get-SafePercentChange $beforeBenchmark $afterBenchmark
        NetworkLatencyChangePercent = Get-SafePercentChange $beforeLatency $afterLatency
        NewCriticalEvents = [math]::Max(0, $afterEvents - $beforeEvents)
        FunctionalLoss = $FunctionalLoss
    }
}

function Test-WindowsPerformanceRegression {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [pscustomobject]$Comparison,
        [ValidateRange(0.1, 50)]
        [double]$ThresholdPercent = 3,
        [ValidateRange(5, 500)]
        [double]$NetworkLatencyThresholdPercent = 50
    )

    $benchmark = Get-OptionalValue $Comparison 'BenchmarkChangePercent' $null
    $latency = Get-OptionalValue $Comparison 'NetworkLatencyChangePercent' $null
    $events = [int](Get-OptionalValue $Comparison 'NewCriticalEvents' 0)
    $functionalLoss = ConvertTo-SafeBoolean (Get-OptionalValue $Comparison 'FunctionalLoss' $false)

    if ($null -ne $benchmark -and [double]$benchmark -lt (-1 * $ThresholdPercent)) {
        return $true
    }
    if ($null -ne $latency -and [double]$latency -gt $NetworkLatencyThresholdPercent) {
        return $true
    }
    return $events -gt 0 -or $functionalLoss
}

function New-WindowsOptimizationState {
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory)]
        [pscustomobject]$Plan,
        [Parameter(Mandatory)]
        [pscustomobject]$Inventory,
        [Parameter(Mandatory)]
        [pscustomobject]$Baseline,
        [string]$StateRoot = "$env:ProgramData\CodexWindowsOptimizer"
    )

    if (-not (Test-WindowsOptimizationPlan -Plan $Plan)) {
        throw 'Refusing to create state for an invalid optimization plan.'
    }
    $statePath = Join-Path $StateRoot (Get-Date -Format 'yyyyMMdd-HHmmss')
    if (-not $PSCmdlet.ShouldProcess($statePath, 'Create optimization backup state')) {
        return [pscustomobject]@{ StatePath = $statePath; WhatIf = $true }
    }

    New-Item -ItemType Directory -Path $statePath -Force | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $statePath 'logs') -Force | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $statePath 'policies-before') -Force | Out-Null

    $Plan | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $statePath 'plan.json') -Encoding UTF8
    $Inventory | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath (Join-Path $statePath 'inventory-before.json') -Encoding UTF8
    $Baseline | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $statePath 'baseline-before.json') -Encoding UTF8
    @((Get-OptionalValue $Inventory 'Services' @())) | ConvertTo-Json -Depth 6 |
        Set-Content -LiteralPath (Join-Path $statePath 'services-before.json') -Encoding UTF8
    @((Get-OptionalValue $Inventory 'ScheduledTasks' @())) | ConvertTo-Json -Depth 6 |
        Set-Content -LiteralPath (Join-Path $statePath 'tasks-before.json') -Encoding UTF8
    @((Get-OptionalValue $Inventory 'AppPackages' @())) | ConvertTo-Json -Depth 6 |
        Set-Content -LiteralPath (Join-Path $statePath 'packages-before.json') -Encoding UTF8

    $powerText = ((& powercfg.exe /getactivescheme 2>$null) -join [Environment]::NewLine)
    Set-Content -LiteralPath (Join-Path $statePath 'power-before.txt') -Value $powerText -Encoding UTF8

    $registryBackups = [System.Collections.Generic.List[string]]::new()
    foreach ($definition in @(
        [pscustomobject]@{ Key = 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved'; File = 'startup-user-before.reg' }
        [pscustomobject]@{ Key = 'HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved'; File = 'startup-machine-before.reg' }
    )) {
        $destination = Join-Path $statePath $definition.File
        $previous = $ErrorActionPreference
        try {
            $ErrorActionPreference = 'Continue'
            & reg.exe export $definition.Key $destination /y 2>$null | Out-Null
            if ($LASTEXITCODE -eq 0 -and (Test-Path -LiteralPath $destination)) {
                $registryBackups.Add($definition.File)
            }
        }
        finally {
            $ErrorActionPreference = $previous
        }
    }

    $requiredArtifacts = @(
        'plan.json'
        'inventory-before.json'
        'baseline-before.json'
        'services-before.json'
        'tasks-before.json'
        'packages-before.json'
        'power-before.txt'
    )
    $manifest = [pscustomobject]@{
        SchemaVersion = 1
        CreatedAt = (Get-Date).ToString('o')
        ComputerName = $env:COMPUTERNAME
        UserName = [Environment]::UserName
        Complete = $true
        RequiredArtifacts = $requiredArtifacts
        RegistryBackups = @($registryBackups)
        NonAutomaticRestoreActions = @(
            'Removed Appx packages may require reinstall from Microsoft Store or OEM source.'
            'Firmware and driver updates are never automatically rolled back by this skill.'
        )
    }
    $manifest | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $statePath 'manifest.json') -Encoding UTF8
    Set-Content -LiteralPath (Join-Path $StateRoot 'latest.txt') -Value $statePath -Encoding UTF8
    return [pscustomobject]@{ StatePath = $statePath; WhatIf = $false }
}

function Test-WindowsOptimizationState {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$StatePath
    )

    $manifestPath = Join-Path $StatePath 'manifest.json'
    if (-not (Test-Path -LiteralPath $manifestPath)) {
        return $false
    }
    try {
        $manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
    }
    catch {
        return $false
    }
    if ((Get-OptionalValue $manifest 'SchemaVersion' 0) -ne 1 -or
        -not (ConvertTo-SafeBoolean (Get-OptionalValue $manifest 'Complete' $false))) {
        return $false
    }
    foreach ($artifact in @((Get-OptionalValue $manifest 'RequiredArtifacts' @()))) {
        if (-not (Test-Path -LiteralPath (Join-Path $StatePath $artifact))) {
            return $false
        }
    }
    return $true
}

function Export-WindowsOptimizationReport {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [pscustomobject]$Data,
        [Parameter(Mandatory)]
        [string]$OutputRoot,
        [string]$Label = 'windows-optimization'
    )

    New-Item -ItemType Directory -Path $OutputRoot -Force | Out-Null
    $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $safeLabel = $Label -replace '[^a-zA-Z0-9._-]', '-'
    $jsonPath = Join-Path $OutputRoot "$stamp-$safeLabel.json"
    $markdownPath = Join-Path $OutputRoot "$stamp-$safeLabel.md"
    $Data | ConvertTo-Json -Depth 15 | Set-Content -LiteralPath $jsonPath -Encoding UTF8

    $lines = [System.Collections.Generic.List[string]]::new()
    $lines.Add("# Windows optimization report - $Label")
    $lines.Add('')
    $lines.Add("- Generated: $((Get-Date).ToString('o'))")
    $lines.Add("- Computer: $env:COMPUTERNAME")
    $lines.Add('')
    $lines.Add('## Summary')
    $lines.Add('')
    foreach ($property in $Data.PSObject.Properties) {
        if ($property.Value -is [string] -or $property.Value -is [ValueType] -or $null -eq $property.Value) {
            $lines.Add("- $($property.Name): $($property.Value)")
        }
        else {
            $count = @($property.Value).Count
            $lines.Add("- $($property.Name): structured data ($count item(s)); see JSON report")
        }
    }
    Set-Content -LiteralPath $markdownPath -Value $lines -Encoding UTF8

    [pscustomobject]@{
        Json = $jsonPath
        Markdown = $markdownPath
    }
}

function Get-StartupApprovedPaths {
    return @(
        'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run'
        'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run32'
        'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\StartupFolder'
        'HKLM:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run'
        'HKLM:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run32'
        'HKLM:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\StartupFolder'
    )
}

function Set-StartupEntryDisabled {
    param(
        [Parameter(Mandatory)]
        [string]$Name
    )
    $changed = $false
    foreach ($path in Get-StartupApprovedPaths) {
        if (-not (Test-Path -LiteralPath $path)) {
            continue
        }
        $item = Get-ItemProperty -LiteralPath $path
        $property = $item.PSObject.Properties[$Name]
        if ($null -eq $property) {
            continue
        }
        $existing = [byte[]]$property.Value
        $bytes = New-Object byte[] ([math]::Max(12, $existing.Length))
        [Array]::Copy($existing, $bytes, $existing.Length)
        $bytes[0] = 3
        Set-ItemProperty -LiteralPath $path -Name $Name -Value $bytes -Type Binary
        $changed = $true
    }
    return $changed
}

function Get-RegenerableCacheInventory {
    $paths = @(
        "$env:LOCALAPPDATA\Temp"
        "$env:LOCALAPPDATA\npm-cache\_cacache"
        "$env:LOCALAPPDATA\uv\cache"
        "$env:LOCALAPPDATA\D3DSCache"
        "$env:LOCALAPPDATA\CrashDumps"
        "$env:LOCALAPPDATA\Microsoft\Windows\INetCache"
    )
    foreach ($path in $paths) {
        if (-not (Test-Path -LiteralPath $path)) {
            continue
        }
        $files = @(Get-ChildItem -LiteralPath $path -File -Recurse -Force -ErrorAction SilentlyContinue)
        $bytes = if ($files.Count -gt 0) {
            [long](($files | Measure-Object Length -Sum).Sum)
        }
        else {
            [long]0
        }
        [pscustomobject]@{
            Path = $path
            SizeGB = [math]::Round($bytes / 1GB, 3)
            FileCount = $files.Count
            Classification = 'Regenerable cache candidate; review before deletion'
        }
    }
}

function Invoke-WindowsOptimizationPlan {
    [CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'High')]
    param(
        [Parameter(Mandatory)]
        [pscustomobject]$Plan,
        [string]$StatePath,
        [string[]]$ApprovedActionId = @()
    )

    if (-not (Test-WindowsOptimizationPlan -Plan $Plan)) {
        throw 'Refusing to execute an invalid optimization plan.'
    }
    $allowed = @(
        'InventoryRegenerableCaches'
        'RunStorageMaintenance'
        'ReviewHibernate'
        'DisableStartupEntry'
        'SetServiceManual'
        'ConfigureWslMemoryReclaim'
        'BenchmarkPowerExperiment'
        'AuditOfficialDriversAndFirmware'
    )
    $results = [System.Collections.Generic.List[object]]::new()
    foreach ($action in @($Plan.Actions)) {
        if ($allowed -notcontains $action.Action) {
            throw "Action is not allowlisted: $($action.Action)"
        }
        if ($action.RequiresConsent -and $ApprovedActionId -notcontains $action.Id) {
            $results.Add([pscustomobject]@{
                Id = $action.Id
                Action = $action.Action
                Target = $action.Target
                Status = 'ConsentRequired'
            })
            continue
        }

        switch ($action.Action) {
            'InventoryRegenerableCaches' {
                $results.Add([pscustomobject]@{
                    Id = $action.Id
                    Action = $action.Action
                    Target = $action.Target
                    Status = 'Audited'
                    Data = @(Get-RegenerableCacheInventory)
                })
            }
            'AuditOfficialDriversAndFirmware' {
                $results.Add([pscustomobject]@{
                    Id = $action.Id
                    Action = $action.Action
                    Target = $action.Target
                    Status = 'ManualReviewRequired'
                })
            }
            'ReviewHibernate' {
                $results.Add([pscustomobject]@{
                    Id = $action.Id
                    Action = $action.Action
                    Target = $action.Target
                    Status = 'ExplicitChoiceRequired'
                })
            }
            'BenchmarkPowerExperiment' {
                $results.Add([pscustomobject]@{
                    Id = $action.Id
                    Action = $action.Action
                    Target = $action.Target
                    Status = 'DedicatedBenchmarkWorkflowRequired'
                })
            }
            'ConfigureWslMemoryReclaim' {
                $results.Add([pscustomobject]@{
                    Id = $action.Id
                    Action = $action.Action
                    Target = $action.Target
                    Status = 'ExplicitConfigurationReviewRequired'
                })
            }
            'DisableStartupEntry' {
                if ($PSCmdlet.ShouldProcess($action.Target, 'Disable startup entry')) {
                    $changed = Set-StartupEntryDisabled -Name $action.Target
                    $results.Add([pscustomobject]@{
                        Id = $action.Id
                        Action = $action.Action
                        Target = $action.Target
                        Status = if ($changed) { 'Applied' } else { 'NotFound' }
                    })
                }
            }
            'SetServiceManual' {
                if ($PSCmdlet.ShouldProcess($action.Target, 'Set optional failing service to Manual')) {
                    Set-Service -Name $action.Target -StartupType Manual
                    $results.Add([pscustomobject]@{
                        Id = $action.Id
                        Action = $action.Action
                        Target = $action.Target
                        Status = 'Applied'
                    })
                }
            }
            'RunStorageMaintenance' {
                if ($PSCmdlet.ShouldProcess('C:', 'Run SSD ReTrim')) {
                    $volume = Get-Volume -DriveLetter C -ErrorAction SilentlyContinue
                    if ($null -ne $volume) {
                        Optimize-Volume -DriveLetter C -ReTrim -Verbose 4>&1 | Out-String |
                            Set-Content -LiteralPath (Join-Path $StatePath 'logs\retrim.log') -Encoding UTF8
                    }
                    $results.Add([pscustomobject]@{
                        Id = $action.Id
                        Action = $action.Action
                        Target = $action.Target
                        Status = 'Applied'
                    })
                }
            }
        }
    }
    return @($results)
}

function Restore-WindowsOptimizationState {
    [CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'High')]
    param(
        [Parameter(Mandatory)]
        [string]$StatePath,
        [switch]$AllowPartial
    )

    $valid = Test-WindowsOptimizationState -StatePath $StatePath
    if (-not $valid -and -not $AllowPartial) {
        throw 'Restore state is incomplete. Use -AllowPartial only after reviewing the manifest.'
    }
    $manifest = Get-Content -LiteralPath (Join-Path $StatePath 'manifest.json') -Raw | ConvertFrom-Json
    $restored = [System.Collections.Generic.List[object]]::new()

    foreach ($backup in @((Get-OptionalValue $manifest 'RegistryBackups' @()))) {
        $path = Join-Path $StatePath $backup
        if ((Test-Path -LiteralPath $path) -and $PSCmdlet.ShouldProcess($path, 'Import registry backup')) {
            & reg.exe import $path | Out-Null
            if ($LASTEXITCODE -ne 0) {
                throw "Registry restore failed: $path"
            }
            $restored.Add([pscustomobject]@{ Type = 'Registry'; Artifact = $backup; Status = 'Restored' })
        }
    }

    $servicesPath = Join-Path $StatePath 'services-before.json'
    if (Test-Path -LiteralPath $servicesPath) {
        $services = @(Get-Content -LiteralPath $servicesPath -Raw | ConvertFrom-Json)
        foreach ($service in $services) {
            $name = [string](Get-OptionalValue $service 'Name' '')
            if ([string]::IsNullOrWhiteSpace($name) -or $null -eq (Get-Service -Name $name -ErrorAction SilentlyContinue)) {
                continue
            }
            $startMode = [string](Get-OptionalValue $service 'StartMode' '')
            $startupType = switch ($startMode) {
                'Auto' { 'Automatic' }
                'Automatic' { 'Automatic' }
                'Manual' { 'Manual' }
                'Disabled' { 'Disabled' }
                default { $null }
            }
            if ($null -ne $startupType -and $PSCmdlet.ShouldProcess($name, "Restore service startup to $startupType")) {
                Set-Service -Name $name -StartupType $startupType
                $restored.Add([pscustomobject]@{ Type = 'Service'; Artifact = $name; Status = 'Restored' })
            }
        }
    }
    return @($restored)
}

function Invoke-ExternalMaintenanceCommand {
    param(
        [Parameter(Mandatory)]
        [string]$Name,
        [Parameter(Mandatory)]
        [string]$FilePath,
        [Parameter(Mandatory)]
        [string[]]$ArgumentList,
        [Parameter(Mandatory)]
        [string]$LogRoot
    )
    $stdout = Join-Path $LogRoot "$Name.stdout.log"
    $stderr = Join-Path $LogRoot "$Name.stderr.log"
    $process = Start-Process -FilePath $FilePath -ArgumentList $ArgumentList -Wait -PassThru `
        -RedirectStandardOutput $stdout -RedirectStandardError $stderr -WindowStyle Normal
    [pscustomobject]@{
        Name = $Name
        ExitCode = $process.ExitCode
        StandardOutput = $stdout
        StandardError = $stderr
        Success = $process.ExitCode -eq 0
    }
}

function Invoke-WindowsMaintenance {
    [CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'High')]
    param(
        [ValidateSet('Quick', 'Deep')]
        [string]$Level = 'Quick',
        [Parameter(Mandatory)]
        [string]$LogRoot
    )

    if (-not $PSCmdlet.ShouldProcess('Windows component store and system volume', "Run $Level maintenance")) {
        return
    }
    New-Item -ItemType Directory -Path $LogRoot -Force | Out-Null
    $results = [System.Collections.Generic.List[object]]::new()
    $results.Add((Invoke-ExternalMaintenanceCommand -Name 'DISM-CheckHealth' -FilePath 'dism.exe' `
        -ArgumentList @('/Online', '/Cleanup-Image', '/CheckHealth') -LogRoot $LogRoot))
    $results.Add((Invoke-ExternalMaintenanceCommand -Name 'SFC-VerifyOnly' -FilePath 'sfc.exe' `
        -ArgumentList @('/verifyonly') -LogRoot $LogRoot))
    $results.Add((Invoke-ExternalMaintenanceCommand -Name 'CHKDSK-Scan' -FilePath 'chkdsk.exe' `
        -ArgumentList @('C:', '/scan') -LogRoot $LogRoot))
    if ($Level -eq 'Deep') {
        $results.Add((Invoke-ExternalMaintenanceCommand -Name 'DISM-ComponentCleanup' -FilePath 'dism.exe' `
            -ArgumentList @('/Online', '/Cleanup-Image', '/StartComponentCleanup') -LogRoot $LogRoot))
        $results.Add((Invoke-ExternalMaintenanceCommand -Name 'DISM-RestoreHealth' -FilePath 'dism.exe' `
            -ArgumentList @('/Online', '/Cleanup-Image', '/RestoreHealth') -LogRoot $LogRoot))
    }
    return @($results)
}

Export-ModuleMember -Function @(
    'Test-WindowsAdministrator'
    'Get-WindowsForbiddenActions'
    'Get-WindowsPerformanceBaseline'
    'Get-WindowsOptimizationInventory'
    'New-WindowsOptimizationPlan'
    'Test-WindowsOptimizationPlan'
    'Compare-WindowsPerformanceBaseline'
    'Test-WindowsPerformanceRegression'
    'New-WindowsOptimizationState'
    'Test-WindowsOptimizationState'
    'Export-WindowsOptimizationReport'
    'Invoke-WindowsOptimizationPlan'
    'Restore-WindowsOptimizationState'
    'Invoke-WindowsMaintenance'
)
