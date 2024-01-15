#!/usr/bin/env bash
# Make sure this file is executable
# chmod +x .github/script/merge-branch.sh

# USAGE: This script is used to merge a branch into another branch

# BACKGROUND: This operation is required to avoid conflicts between branches.

# Setup commiter identity
git config user.name github-actions
git config user.email github-actions@github.com

# Merge branch
echo "If branch $branch2 exists, merge branch $branch1 into branch $branch2"
if git show-ref --quiet refs/heads/$branch2
then
  git checkout $branch2
  git merge $branch1
  git push origin $branch2
else
  echo "Branch $branch2 does not exist"
fi
