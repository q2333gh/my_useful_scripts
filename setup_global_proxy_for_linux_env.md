# Linux Global Proxy Setup

Edit `/etc/environment`:

```bash
http_proxy="http://host:port"
https_proxy="http://host:port"
```

Relogin or reboot to apply.

## Verify

```bash
env | grep -i proxy
curl -I https://www.google.com
```
