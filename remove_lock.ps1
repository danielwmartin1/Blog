$lockFile = "C:/Users/danie/OneDrive/Coding/Projects/Blog/.git/index.lock"
if (Test-Path $lockFile) {
    Remove-Item -Path $lockFile -Force
    Write-Output "Lock file removed."
} else {
    Write-Output "Lock file does not exist."
}
