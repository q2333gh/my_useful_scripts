#!/bin/bash
# Delegate Windows VPN to WSL
# Usage: ./win10_VPN_delegate_WSL.sh <proxy_port>

set -e

if [ -z "$1" ]; then
    echo "Usage: ./win10_VPN_delegate_WSL.sh <proxy_port>"
    exit 1
fi

PROXY_PORT="$1"

if ! [[ "$PROXY_PORT" =~ ^[0-9]+$ ]] || [ "$PROXY_PORT" -lt 1 ] || [ "$PROXY_PORT" -gt 65535 ]; then
    echo "Error: invalid port"
    exit 1
fi

PROXY_SERVER=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')

if [ -z "$PROXY_SERVER" ]; then
    echo "Error: cannot get Windows host IP"
    exit 1
fi

export http_proxy="http://${PROXY_SERVER}:${PROXY_PORT}"
export HTTP_PROXY="$http_proxy"
export https_proxy="$http_proxy"
export HTTPS_PROXY="$http_proxy"

echo "Proxy: $http_proxy"

if curl --silent --head --max-time 5 https://www.google.com/ | grep -q "HTTP.*200"; then
    echo "Connection OK"
else
    echo "Connection failed"
    exit 1
fi
