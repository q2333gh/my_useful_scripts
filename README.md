# Useful Scripts Collection

Scripts and docs for Linux and Windows development.

## Scripts

### Python

- **`global_proxy.py`** - Enable/disable global proxy in `/etc/environment`
  ```bash
  sudo python3 global_proxy.py [enable|disable]
  ```

- **`shut_cable.py`** - Control Windows network adapter (disable/enable/restart)
  - Edit `ADAPTER_KEYWORD` and `ACTION_FLAG` (0=disable, 1=enable, 2=restart)
  - Run as admin: `python shut_cable.py`

### Shell

- **`sudo_dont_need_passwd.sh`** - Configure sudo without password
  ```bash
  sudo ./sudo_dont_need_passwd.sh <username>
  ```

- **`win10_VPN_delegate_WSL.sh`** - Delegate Windows VPN to WSL
  ```bash
  ./win10_VPN_delegate_WSL.sh <proxy_port>
  ```

## Docs

- `docker.md` - Docker commands
- `gh_CLI.md` - GitHub CLI commands
- `git.md` - Git commands
- `vscode_handy.md` - VS Code tips
- `setup_global_proxy_for_linux_env.md` - Linux proxy setup
- `normal_user_sudo_no__need_passwd.md` - Sudo without password
- `move_task_to_background_in_terminal.md` - Background tasks
