#!/bin/bash

# College-Notes Commit Cleanup Script
# This script will clean up commit messages and prepare for daily commits

echo "College-Notes Commit Cleanup"
echo "============================"
echo ""
echo "Current commit count:"
cd "c:/Users/USER/Desktop/Extras/College-Notes"
git rev-list --count HEAD
echo ""
echo "Starting interactive rebase for the last 170 commits..."
echo "This will open your editor to configure the rebase."
echo ""
echo "Instructions for the rebase:"
echo "1. In the editor, you'll see a list of commits"
echo "2. For each 'pick', you can change to:"
echo "   - 'reword' or 'r' to change the commit message"
echo "   - 'squash' or 's' to merge with previous commit"
echo "   - 'fixup' or 'f' to merge and discard this message"
echo ""
echo "Recommended approach:"
echo "- Keep first commit as 'pick'"
echo "- Change 'pick' to 'squash' for similar commits"
echo "- Change 'pick' to 'reword' for messy messages"
echo ""
echo "Starting rebase..."
git rebase -i HEAD~170
