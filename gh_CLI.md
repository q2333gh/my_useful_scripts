# GitHub CLI

## Auth

```bash
gh auth login
```

## Create repo

```bash
gh repo create <name> --private
gh repo create <name> --public
```

## Clone

```bash
gh repo clone <owner>/<repo>
```

## Link existing repo

```bash
gh repo create <name> --public --source=. --remote=origin --push
```

## Other

```bash
gh repo view
gh repo list
gh issue create
gh pr create
```
