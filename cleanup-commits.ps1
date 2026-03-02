# College-Notes Commit Cleanup - PowerShell Version
# Run this in PowerShell

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

Write-Host "Step 3: Analyzing commit messages..." -ForegroundColor Yellow
$messages = git log --format="%s" -170 | Select-Object -First 20
Write-Host "Sample messages (first 20):" -ForegroundColor Cyan
$messages | ForEach-Object { Write-Host "  $_" }
Write-Host ""

# Get unique message patterns
Write-Host "Step 4: Unique message patterns found:" -ForegroundColor Yellow
$uniquePatterns = git log --format="%s" -170 | Sort-Object -Unique
$uniquePatterns | ForEach-Object { Write-Host "  $_" }
Write-Host ""

Write-Host "Step 5: Creating new clean history..." -ForegroundColor Yellow

# We'll use git rebase with a script approach
# First, let's check the commits that need cleaning
$commitsToClean = git log --format="%H|%s" -170

# Create a mapping of old -> new messages
$messageMap = @{
    "Addition for changes" = "Update college notes"
    "Updates" = "Update project files"
    "Updations" = "Update project files"
}

Write-Host "Note: This will require interactive rebase for proper cleanup." -ForegroundColor Yellow
Write-Host ""
Write-Host "Alternative: Using git filter-branch for automated cleanup..." -ForegroundColor Cyan
Write-Host ""

# Automated cleanup using git filter-branch
git filter-branch --msg-filter '
$msg = Get-Content -Raw
# Remove the "Add '\''...'\'' from commit '\''...'\''" patterns
$msg = $msg -replace "Add '\''[^'\'']+/.*'\'' from commit '\''[a-f0-9]+'\''", "Add project files"
$msg = $msg -replace "^Addition for changes`$", "Update college notes"
$msg = $msg -replace "^Updates`$", "Update project files"
$msg = $msg -replace "^Updations`$", "Update project files"
Write-Output $msg
' HEAD 2>&1 | Out-Null

Write-Host "Step 6: Cleanup complete!" -ForegroundColor Green
Write-Host ""

$newCount = git rev-list --count HEAD
Write-Host "Original commits: $commitCount" -ForegroundColor White
Write-Host "New commits: $newCount" -ForegroundColor White
Write-Host ""

Write-Host "Results - New commit log:" -ForegroundColor Cyan
git log --oneline -15

Write-Host ""
Write-Host "To restore if something goes wrong: git reset --hard backup-before-cleanup" -ForegroundColor Yellow
Write-Host "To force push to remote: git push --force origin master" -ForegroundColor Yellow
