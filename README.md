# Useful Scripts Collection

Collection of useful scripts and documentation for Linux and Windows development.

## Scripts

### Python Scripts

#### `shut_cable.py`
Windows script to control network adapter (disable/enable/restart).
- Control adapter by keyword (e.g., "Realtek", "Intel")
- Requires admin privileges
- Actions: disable (0), enable (1), restart (2)

**Usage:**
```bash
# Edit ACTION_FLAG and ADAPTER_KEYWORD in the script, then:
python shut_cable.py
```

#### `global_proxy.py`
Linux script to enable/disable global proxy settings in `/etc/environment`.
- Enable/disable HTTP and HTTPS proxy
- Requires sudo privileges

**Usage:**
```bash
sudo python global_proxy.py
# Enter 'enable' or 'disable'
```

### Shell Scripts

#### `sudo_dont_need_passwd.sh`
Script to configure sudo without password prompt.

#### `win10_VPN_delegate_WSL.sh`
Script for Windows 10 to delegate VPN to WSL.

## Documentation

- `docker.md` - Docker useful commands and tips
- `gh_CLI.md` - GitHub CLI commands
- `git.md` - Git commands
- `vscode_handy.md` - VS Code handy tips
- `setup_global_proxy_for_linux_env.md` - Setup global proxy for Linux environment
- `normal_user_sudo_no__need_passwd.md` - Configure sudo without password
- `move_task_to_background_in_terminal.md` - Move task to background in terminal

## License

See individual files for license information.
