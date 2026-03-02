#!/bin/bash

# College-Notes Automated Commit Cleanup
# This script cleans up commit messages without losing any data

cd "c:/Users/USER/Desktop/Extras/College-Notes"

echo "=== College-Notes Commit Cleanup ==="
echo ""
echo "Step 1: Backing up current state..."
git branch backup-before-cleanup
echo "Backup created: backup-before-cleanup"
echo ""

echo "Step 2: Analyzing commits..."
echo "Total commits: $(git rev-list --count HEAD)"
echo ""

# Get all commits and analyze
echo "Step 3: Creating cleaned commit history..."
echo ""

# Use git filter-branch to rewrite messages
# This preserves all data while cleaning messages
git filter-branch --msg-filter '
# Read the commit message
msg=$(cat)

# Clean up patterns
# Remove "Add '\''...'\'' from commit '\''...'\''" patterns
msg=$(echo "$msg" | sed "s/Add '\''[^ '\'']*\/.*'\'' from commit '\''[a-f0-9]*'\''/Add project files/g")

# Clean up generic messages
msg=$(echo "$msg" | sed "s/^Addition for changes$/Update college notes/g")
msg=$(echo "$msg" | sed "s/^Updates$/Update project files/g")
msg=$(echo "$msg" | sed "s/^Updations$/Update project files/g")

echo "$msg"
' HEAD

echo ""
echo "Step 4: Cleanup complete!"
echo ""
echo "New commit count: $(git rev-list --count HEAD)"
echo ""
echo "Check the results with: git log --oneline -20"
echo "If something went wrong, restore with: git reset --hard backup-before-cleanup"
