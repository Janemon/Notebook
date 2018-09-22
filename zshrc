# If you come from bash you might have to change your $PATH.
 export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
  export ZSH="/home/janemon/.oh-my-zsh"

# Theme
ZSH_THEME="peepcode"


# Uncomment the following line to use case-sensitive completion.
 CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
 HYPHEN_INSENSITIVE="true"
 
# show the time pre-fix front the indirectives
 HIST_STAMPS="yyyy-mm-dd"

# update
# export UPDATE_ZSH_DAYS=30


# Uncomment the following line to display red dots whilst waiting for completion.
 COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
 DISABLE_UNTRACKED_FILES_DIRTY="true"


# Plugin
#plugins=(
#  git
#)

source /home/janemon/antigen/antigen.zsh

# Load the oh-my-zsh's library.
 antigen use oh-my-zsh

# Bundles from the default repo (robbyrussell's oh-my-zsh).
 antigen bundle git
 antigen bundle heroku
 antigen bundle pip
 antigen bundle lein
 antigen bundle command-not-found

# Syntax highlighting bundle.
 antigen bundle zsh-users/zsh-syntax-highlighting
 
# useful plugin finded on web 
 antigen bundle rupa/z
 antigen bundle wting/autojump
 antigen bundle zsh-users/zsh-autosuggestions
 antigen bundle paulirish/git-open
# # Tell Antigen that you're done.
 antigen apply




source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
 export SSH_KEY_PATH="~/.ssh/rsa_id"

# Aliases
alias zshconfig="vim ~/.zshrc"
alias ohmyzsh="cd ~/.oh-my-zsh"
alias gop="git-open"

alias rm="trash -i"  # 防止误删，把文件丢到 /.local/share/Trash/files
alias rmr="trash -rf"
alias rml="trash-list"
alias rmall="trash-empty"
alias cp="cp -i" # 防止文件覆盖到已存在的文件上
alias szh="source ~/.zshrc"
alias sai="sudo apt-get install"
function mkcd
{
    command mkdir $1 && cd $1
}



# nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm


