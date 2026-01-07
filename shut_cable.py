import subprocess
import time

# Adapter to control (search by description)
ADAPTER_KEYWORD = "Realtek"

# Action flag: 0=disable, 1=enable, 2=restart
ACTION_FLAG = 0


def get_status(name):
    cmd = f"powershell -Command \"(Get-NetAdapter -Name '{name}').Status\""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


def is_admin():
    cmd = 'powershell -Command "([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip().lower() == "true"


def find_adapter(keyword):
    cmd = f"powershell -Command \"Get-NetAdapter | Where-Object InterfaceDescription -like '*{keyword}*' | Select-Object -ExpandProperty Name\""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    name = result.stdout.strip()
    if name:
        print(f"Found: {name}")
    return name


def set_adapter_state(name, state):
    subprocess.run(f'netsh interface set interface "{name}" admin={state}', shell=True)
    time.sleep(2)
    print(f"execute {state}: {get_status(name)}")


def main():
    print(f"Keyword: {ADAPTER_KEYWORD}")

    # Check admin
    if not is_admin():
        print("Error: Requires admin")
        exit(1)

    # Find adapter name
    name = find_adapter(ADAPTER_KEYWORD)

    if name:
        if ACTION_FLAG == 0:
            set_adapter_state(name, "disable")
        elif ACTION_FLAG == 1:
            set_adapter_state(name, "enable")
        elif ACTION_FLAG == 2:
            set_adapter_state(name, "disable")
            set_adapter_state(name, "enable")
    else:
        print(f"Error: Adapter '{ADAPTER_KEYWORD}' not found")


if __name__ == "__main__":
    main()
