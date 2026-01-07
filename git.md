# Git Commands

## Set editor

```bash
git config --global core.editor "vim"
git config --global core.editor "code --wait"
```

## Squash commits

```bash
git rebase -i HEAD~N
# Change 'pick' to 'squash' for commits to merge
```

## Other

```bash
git log --oneline
git reset --soft HEAD~1
git reset --hard HEAD~1
git commit --amend
```
