
# Fish Shell 个人配置（btwl@btwl-virtual-machine）

## 功能（别名 + 函数）

```fish
# 别名
alias py3="python3"
alias tree="tree -s -h --du"
alias dkcp="docker-compose"
# alias rvpn="sudo ip link delete nekoray-tun"
# alias vpn="sudo /home/btwl/app/nekoray_proxy_gui/nekoray/launcher"

# 函数
function mcd
    mkdir $argv[1]; and cd $argv[1]
end

# function pc4 --wraps=proxychains4 --description 'alias pc4=proxychains4'
#     proxychains4 $argv
# end


# for var in HTTP_PROXY HTTPS_PROXY ALL_PROXY http_proxy https_proxy all_proxy
#     set -x $var 127.0.0.1:2080
# end
function vpn
    export https_proxy=http://127.0.0.1:2080
    export http_proxy=http://127.0.0.1:2080
end

# set -e HTTP_PROXY && set -e HTTPS_PROXY && set -e ALL_PROXY && set -e http_proxy && set -e https_proxy && set -e all_proxy   
function dvpn
    export http_proxy=
    export https_proxy=
end

function hgp
    history | grep --color=always $argv | awk '{print NR " " $0}' | sort -nr | cut -d' ' -f2-
end
```

## 交互 / 启动配置

```fish
if status is-interactive
    # Commands to run in interactive sessions can go here
end

# 去掉启动问候信息
set fish_greeting
```

