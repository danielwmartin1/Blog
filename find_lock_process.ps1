$handlePath = "C:\Program Files\Sysinternals\Handle.exe"
$lockFile = "C:/Users/danie/OneDrive/Coding/Projects/Blog/.git/index.lock"

if (-Not (Test-Path $handlePath)) {
    Write-Output "Handle.exe not found. Please download it from https://docs.microsoft.com/en-us/sysinternals/downloads/handle and place it in C:\Program Files\Sysinternals."
    exit
}

if (-Not (Test-Path $lockFile)) {
    Write-Output "Lock file not found at $lockFile. Please check the path and try again."
    exit
}

$handleOutput = &"$handlePath" $lockFile 2>&1
$handleOutput | ForEach-Object {
    if ($_ -match 'pid: (\d+)') {
        $pid = $matches[1]
        Write-Output "Process ID $pid is using the lock file."
        Stop-Process -Id $pid -Force
        Write-Output "Process $pid has been terminated."
    }
}
