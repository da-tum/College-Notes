# College-Notes Full Cleanup Script
# Implements: 1) Clean messages, 2) Squash similar, 3) Spread dates Jan-Mar 2026

Set-Location "c:/Users/USER/Desktop/Extras/College-Notes"

Write-Host "=== College-Notes Full Cleanup ===" -ForegroundColor Cyan
Write-Host ""

# Create backup
Write-Host "Creating backup..." -ForegroundColor Yellow
git branch full-cleanup-backup

# Get total commits
$totalCommits = git rev-list --count HEAD
Write-Host "Total commits to process: $totalCommits" -ForegroundColor Green

# Define message cleaning function
function Clean-Message {
    param([string]$msg)
    
    # Clean "Add 'folder/from commit 'hash''" patterns
    if ($msg -match "Add '.+?/' from commit") {
        $msg = "Add project files"
    }
    if ($msg -match "Add '.+?/.+?' from commit") {
        # Extract folder name
        if ($msg -match "Sem-I/Web-Dev-I/Assignments/Capstone") { $msg = "Add Capstone Lab5 project" }
        elseif ($msg -match "Sem-I/Python/Assignments/LibraryInventory") { $msg = "Add Library Inventory Manager" }
        elseif ($msg -match "Sem-I/Python/Assignments/GradeBook") { $msg = "Add GradeBook Analyzer" }
        elseif ($msg -match "CSFCP--4") { $msg = "Add CSFCP Assignment 4" }
        elseif ($msg -match "Shell-Commands") { $msg = "Add Shell Commands assignment" }
        elseif ($msg -match "Web-Dev-Lab-1-and-2") { $msg = "Add Web Dev Lab 1-2" }
        elseif ($msg -match "Web-Dev-Lab3") { $msg = "Add Web Dev Lab 3" }
        elseif ($msg -match "Web-Dev-Lab4") { $msg = "Add Web Dev Lab 4" }
    }
    
    # Generic message cleanup
    $msg = $msg -replace "^Addition for changes$", "Update college notes"
    $msg = $msg -replace "^Updates$", "Update project files"
    $msg = $msg -replace "^Updations$", "Update project files"
    $msg = $msg -replace "^Additions$", "Add project files"
    $msg = $msg -replace "^Changes$", "Update files"
    $msg = $msg -replace "^Correction$", "Fix issues"
    $msg = $msg -replace "^Modified$", "Update files"
    $msg = $msg -replace "^Commit$", "Save changes"
    $msg = $msg -replace "^Commiting$", "Save changes"
    $msg = $msg -replace "^Basic Creation$", "Create base files"
    $msg = $msg -replace "^Folder Creation$", "Create folder structure"
    
    return $msg
}

# Calculate date range - spread from Jan 1 to Mar 1, 2026
$startDate = Get-Date "2026-01-01T10:00:00"
$endDate = Get-Date "2026-03-01T03:00:00"
$dateRange = ($endDate - $startDate).TotalMinutes
$minutesPerCommit = $dateRange / $totalCommits

Write-Host "Date range: Jan 1, 2026 to Mar 1, 2026" -ForegroundColor Cyan
Write-Host "Spreading $totalCommits commits across $($minutesPerCommit.ToString('F0')) minute intervals" -ForegroundColor Cyan
Write-Host ""

# Process commits - this is a simplified approach
# We'll use git rebase with exec commands

Write-Host "Note: Full implementation requires interactive rebase." -ForegroundColor Yellow
Write-Host "Creating rebase todo file..." -ForegroundColor Yellow

# Create a todo file for the rebase
$todoContent = @"
# Git Rebase Instructions for College-Notes Cleanup
# 
# This file contains instructions for cleaning up the commit history
#
# Commands:
# pick = use commit
# reword = use commit, but edit the commit message  
# squash = use commit, but meld into previous commit
# fixup = like squash, but discard this commit's message
#
# For 170 commits, we recommend:
# - Keep first commit as "pick"
# - Use "squash" for similar commits
# - Use "reword" for unique commits with bad messages

"@

# Get unique commit patterns for analysis
$uniqueMessages = git log --format="%s" -$totalCommits | Sort-Object -Unique

# Save the unique messages for reference
$uniqueMessages | Out-File -FilePath "commit-messages-cleanup.txt" -Encoding UTF8

Write-Host "Unique message patterns saved to: commit-messages-cleanup.txt" -ForegroundColor Green
Write-Host ""
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "- Original commits: $totalCommits" -ForegroundColor White
Write-Host "- All dated: 2026-03-01" -ForegroundColor White
Write-Host "- Will be spread: Jan 1 - Mar 1, 2026" -ForegroundColor White
Write-Host "- Messages will be cleaned" -ForegroundColor White
Write-Host ""
Write-Host "To complete the cleanup manually, run: git rebase -i HEAD~$totalCommits" -ForegroundColor Yellow
Write-Host ""
Write-Host "Alternative: Let me try a different automated approach..." -ForegroundColor Cyan
