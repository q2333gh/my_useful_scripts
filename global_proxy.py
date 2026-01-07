#!/usr/bin/env python3
"""
Enable/disable global proxy in /etc/environment
Requires sudo
"""

import os
import sys
import shutil
from datetime import datetime

ENVIRONMENT_FILE = "/etc/environment"
BACKUP_SUFFIX = ".bak"


def backup_file(file_path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{file_path}{BACKUP_SUFFIX}.{timestamp}"
    try:
        shutil.copy2(file_path, backup_path)
        print(f"Backup: {backup_path}")
        return True
    except Exception as e:
        print(f"Backup failed: {e}")
        return False


def enable_proxy():
    print("Enabling proxy...")
    if not os.path.exists(ENVIRONMENT_FILE):
        print(f"Error: {ENVIRONMENT_FILE} not found")
        return False

    if not backup_file(ENVIRONMENT_FILE):
        return False

    try:
        with open(ENVIRONMENT_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        modified = False
        new_lines = []

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("# http_proxy="):
                new_lines.append(line[1:])
                modified = True
            elif stripped.startswith("# https_proxy="):
                new_lines.append(line[1:])
                modified = True
            else:
                new_lines.append(line)

        if modified:
            with open(ENVIRONMENT_FILE, "w", encoding="utf-8") as file:
                file.writelines(new_lines)
            print("Proxy enabled. Relogin to apply.")
            return True
        else:
            print("No commented proxy config found")
            return False

    except PermissionError:
        print("Error: requires sudo")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def disable_proxy():
    print("Disabling proxy...")
    if not os.path.exists(ENVIRONMENT_FILE):
        print(f"Error: {ENVIRONMENT_FILE} not found")
        return False

    if not backup_file(ENVIRONMENT_FILE):
        return False

    try:
        with open(ENVIRONMENT_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        modified = False
        new_lines = []

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("http_proxy=") and not stripped.startswith("#"):
                new_lines.append("#" + line)
                modified = True
            elif stripped.startswith("https_proxy=") and not stripped.startswith("#"):
                new_lines.append("#" + line)
                modified = True
            else:
                new_lines.append(line)

        if modified:
            with open(ENVIRONMENT_FILE, "w", encoding="utf-8") as file:
                file.writelines(new_lines)
            print("Proxy disabled. Relogin to apply.")
            return True
        else:
            print("No active proxy config found")
            return False

    except PermissionError:
        print("Error: requires sudo")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    if os.geteuid() != 0:
        print("Error: requires sudo")
        print("Usage: sudo python3 global_proxy.py [enable|disable]")
        sys.exit(1)

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
    else:
        command = input("Command (enable/disable): ").strip().lower()

    if command == "enable":
        success = enable_proxy()
        sys.exit(0 if success else 1)
    elif command == "disable":
        success = disable_proxy()
        sys.exit(0 if success else 1)
    else:
        print('Invalid command. Use "enable" or "disable"')
        sys.exit(1)


if __name__ == "__main__":
    main()
