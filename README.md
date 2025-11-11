# GitHub Chapter 2 — Sandbox

A tiny practice repo for learning basic Git and GitHub flows (fork, clone, pull, push, and syncing a fork).

This repo currently contains one example file:
- `info.txt` — "Go ahead and fork this repository before cloning to your local computer!"

## Quick start

- Fork this repo on GitHub to your account.
- Clone your fork locally.
- Make a small change on a branch, commit, and push.
- Open a Pull Request to your fork’s `main` or to the original upstream repo.

## Keep your fork in sync with upstream

If you forked from `codedex-io/github-chapter-2-sandbox`, add and use an upstream remote:

```powershell
# From inside the repo folder
git remote add upstream https://github.com/codedex-io/github-chapter-2-sandbox.git

# Fetch upstream branches and tags
git fetch upstream

# Make sure you're on main
git checkout main

# Fast-forward your main to match upstream/main
git merge --ff-only upstream/main
# or equivalently
# git pull --ff-only upstream main
```

## Typical workflow

```powershell
# Create a feature branch
git checkout -b feature/update-readme

# Stage and commit your changes
git add README.md
git commit -m "Improve README"

# Push to your fork
git push -u origin feature/update-readme

# Open a PR from your branch
```

## Notes

- If your fork shows "1 commit ahead" of upstream, that just means you have custom changes (like this README). That’s normal for forks.
- If you ever want to realign exactly with upstream, you can reset your main to `upstream/main` (be careful—this rewrites history) and force-push with lease.
