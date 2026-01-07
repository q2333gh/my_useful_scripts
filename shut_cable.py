#!/usr/bin/env python3
"""
Control Windows network adapter
Requires admin
"""

import subprocess
import time
import sys

ADAPTER_KEYWORD = "Realtek"
ACTION_FLAG = 0  # 0=disable, 1=enable, 2=restart


def get_status(name):
    cmd = f"powershell -Command \"(Get-NetAdapter -Name '{name}').Status\""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None


def is_admin():
    cmd = (
        'powershell -Command "'
        "([Security.Principal.WindowsPrincipal]"
        "[Security.Principal.WindowsIdentity]::GetCurrent())"
        '.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)"'
    )
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, check=True
        )
        return result.stdout.strip().lower() == "true"
    except subprocess.CalledProcessError:
        return False


def find_adapter(keyword):
    cmd = (
        f'powershell -Command "'
        f"Get-NetAdapter | "
        f"Where-Object InterfaceDescription -like '*{keyword}*' | "
        f'Select-Object -ExpandProperty Name"'
    )
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, check=True
        )
        name = result.stdout.strip()
        if name:
            print(f"Found: {name}")
        return name
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None


def set_adapter_state(name, state):
    cmd = f'netsh interface set interface "{name}" admin={state}'
    try:
        subprocess.run(cmd, shell=True, check=True)
        time.sleep(2)
        status = get_status(name)
        if status:
            print(f"{state}: {status}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False


def main():
    print(f"Keyword: {ADAPTER_KEYWORD}")
    print(f"Action: {['disable', 'enable', 'restart'][ACTION_FLAG]}")

    if not is_admin():
        print("Error: requires admin")
        sys.exit(1)

    adapter_name = find_adapter(ADAPTER_KEYWORD)
    if not adapter_name:
        print(f"Error: adapter '{ADAPTER_KEYWORD}' not found")
        sys.exit(1)

    success = False
    if ACTION_FLAG == 0:
        success = set_adapter_state(adapter_name, "disable")
    elif ACTION_FLAG == 1:
        success = set_adapter_state(adapter_name, "enable")
    elif ACTION_FLAG == 2:
        success = set_adapter_state(adapter_name, "disable") and set_adapter_state(
            adapter_name, "enable"
        )
    else:
        print(f"Error: invalid ACTION_FLAG {ACTION_FLAG}")
        sys.exit(1)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
