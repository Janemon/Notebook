### the gihub registroy: https://github.com/robbyrussell/oh-my-zsh

#### first using oh-my-zsh you should do:
1. switch your shell into **Zsh**: `sudo apt-get install zsh`  
2. make it your default shell: `chsh -s $(which zsh)`, check it: `vim /etc/shells`  
3. log out and login back, then check it: `echo $SHELL`  

#### then start install oh-my-zsh:
`sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"`

#### last config it:
**Using `~/.zshrc` to config it:**
1. Theme setting: `ZSH_THEME="agnoster"`
> My config  

2. persistenc alias setting: `alias rm="rm -i"`  

3. I use **antigen** to manager the plugin of zsh, which like **vundle** for vim  

