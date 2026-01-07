#!/bin/bash
# Configure sudo without password
# Usage: sudo ./sudo_dont_need_passwd.sh <username>

set -e

if [ -z "$1" ]; then
    echo "Usage: sudo ./sudo_dont_need_passwd.sh <username>"
    exit 1
fi

USERNAME="$1"

if [ "$EUID" -ne 0 ]; then
    echo "Error: requires sudo"
    exit 1
fi

if ! id "$USERNAME" &>/dev/null; then
    echo "Error: user '$USERNAME' not found"
    exit 1
fi

BACKUP_FILE="$HOME/sudoers.bak.$(date +%Y%m%d_%H%M%S)"
cp /etc/sudoers "$BACKUP_FILE"
echo "Backup: $BACKUP_FILE"

echo "1) NOPASSWD:ALL"
echo "2) Specific commands"
read -p "Choice (1/2): " choice

case $choice in
    1)
        SUDOERS_LINE="${USERNAME} ALL=(ALL) NOPASSWD:ALL"
        ;;
    2)
        read -p "Commands: " commands
        SUDOERS_LINE="${USERNAME} ALL=(ALL) NOPASSWD:${commands}"
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac

if command -v visudo &> /dev/null; then
    TEMP_FILE=$(mktemp)
    echo "$SUDOERS_LINE" >> "$TEMP_FILE"
    
    if visudo -cf "$TEMP_FILE" 2>/dev/null; then
        echo "$SUDOERS_LINE" | sudo tee -a /etc/sudoers > /dev/null
        
        if visudo -c; then
            echo "Done"
        else
            echo "Syntax error, restoring backup..."
            cp "$BACKUP_FILE" /etc/sudoers
            exit 1
        fi
    else
        echo "Syntax error"
        rm "$TEMP_FILE"
        exit 1
    fi
    
    rm "$TEMP_FILE"
else
    echo "Error: visudo not found"
    exit 1
fi
