# College-Notes Commit Cleanup - Fixed Version
Set-Location "c:/Users/USER/Desktop/Extras/College-Notes"

Write-Host "=== College-Notes Commit Cleanup ===" -ForegroundColor Cyan
Write-Host ""

Write-Host "Step 1: Creating backup branch..." -ForegroundColor Yellow
git branch backup-before-cleanup
Write-Host "Backup created: backup-before-cleanup" -ForegroundColor Green
Write-Host ""

Write-Host "Step 2: Current commit analysis..." -ForegroundColor Yellow
$commitCount = git rev-list --count HEAD
Write-Host "Total commits: $commitCount" -ForegroundColor Green
Write-Host ""

Write-Host "Step 3: Unique message patterns..." -ForegroundColor Yellow
git log --format="%s" -170 | Sort-Object -Unique | ForEach-Object { Write-Host "  $_" }
Write-Host ""

Write-Host "Step 4: Running automated cleanup..." -ForegroundColor Yellow

# Run git filter-branch to clean messages
git filter-branch --msg-filter "git log --format=%B -1 | ForEach-Object { $_ -replace 'Add .+?/.* from commit .+', 'Add project files' -replace '^Addition for changes$', 'Update college notes' -replace '^Updates$', 'Update project files' -replace '^Updations$', 'Update project files' }" HEAD 2>&1 | Out-Null

Write-Host "Step 5: Cleanup complete!" -ForegroundColor Green
Write-Host ""

$newCount = git rev-list --count HEAD
Write-Host "Original commits: $commitCount" -ForegroundColor White
Write-Host "New commits: $newCount" -ForegroundColor White
Write-Host ""

Write-Host "Results - New commit log:" -ForegroundColor Cyan
git log --oneline -15
