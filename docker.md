# Docker Commands

## Check restart policy

```bash
docker ps -aq | xargs docker inspect --format '{{ .Name }}: {{ .HostConfig.RestartPolicy }}'
```

## Rename container

```bash
docker rename <old_name> <new_name>
```

## Execute command in container

```bash
docker exec <container_name> <command>
```

## Copy file to container

```bash
docker cp <host_path> <container_name>:<container_path>
```

## Enable proxy

### Environment variables

```bash
docker run -it -e http_proxy=http://host:port -e https_proxy=http://host:port ubuntu
```

### Docker config (`~/.docker/config.json`)

```json
{
  "proxies": {
    "default": {
      "httpProxy": "http://host:port",
      "httpsProxy": "http://host:port"
    }
  }
}
```

### Daemon config (`/etc/docker/daemon.json`)

```json
{
  "proxies": {
    "http-proxy": "http://host:port",
    "https-proxy": "http://host:port"
  }
}
```

```bash
sudo systemctl restart docker
```
