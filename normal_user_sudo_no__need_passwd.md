# Sudo Without Password

## Using visudo (recommended)

```bash
sudo visudo
```

Add to end of file:

```bash
username ALL=(ALL) NOPASSWD:ALL
```

Or specific commands:

```bash
username ALL=(ALL) NOPASSWD:/usr/bin/apt update, /usr/bin/apt upgrade
```

## Commands

```bash
sudo visudo
sudo visudo -c
sudo EDITOR=vim visudo
```
