#### 其实无外乎两种方法：
1. 自己下载安装包<small>(官网、github)</small>，自己解压，自己编译，自己选择路径安装。  
2. 通过安装程序，一站式进行配置安装, 比如：Ubuntu的`sudo apt-get install ...` 和 `npm install --save/--save dev/-g`。  

---------------------------------------------------------------------

#### 1 关于 ubuntu 的 安装，升级和卸载


---------------------------------------------------------------------

#### 2 自己安装的大体方法

1. 如果是源码编译安装，那么一般是以下几个步骤：
> 1 解压并进入包文件: `tar -xvf ...gar.gz | cd package_name`  
> 2 配置：`./configure`<small>(如果有这个文件的话)</small>  
> 3 编译: `make`  
> 4 安装：`make install`  

---------------------------------------------------------------------

### 3 node.js and npm

<mark>Note: 建议使用 `nvm` (node.js version managerment)来安装管理`node.js`</mark>


---------------------------------------------------------------------
##### 安装 nvm：`curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash`, 其安装目录一般是在`~/.nvm` 中  

nvm 常用指令：
> 1 nvm ls-remote (显示远端可用版本号）  
> 2 nvm ls (显示电脑已经安装的）  
> 3 nvm install version (安装指定版本）  
> 4 nvm install --lts (安装最新的稳定版）  
> 5 nvm use version (使用指定版本）  
---------------------------------------------------------------------

1. node.js 安装： `nvm install --lts`
> **npm**(node.js package managerment) 也是随之安装上了  
>> <mark>Note:</mark> 如果使用 nvm 来进行安装，那么 node的安装路径就在这里，和 npm 安装的模块也在这里 ：）。  

2. npm 使用：
> 1 提高下载速度，切换源并保存配置：`npm config set registry https://registry.npm.taobao.org` [ 实际上是修改 `~/.npmrc` ]  
>> 配置后验证是否成功：`npm config get registry`  

> 2 更新 npm ：`npm i -g npm`  

> 3 使用 npm 安装的文件的路径:
>> 1 本地模式下：存放在当前工作目录下的 `node_modules`  
>> 2 全局模式下：一般会在 `{prefix}/...` <small>prefix=> `/usr/`or`/usr/local`</small> 或者 node的安装目录下  

> 3 查看并修改 npm 配置内容：
>> 1 `npm config list`  
>> 2 `npm config set ...`  

> 4 查看安装的全局模块:
>> 1 简易版：`npm list -g --depth=0`, 第一行为路径.  
>> 2 具体版：`npm list -g`  

> 5 安装模块:
>> 1 安装全局模块：`npm install package_name -g`  
>> 2 在工作目录里安装本地模块：
>>> 1 `npm init(-f)` [ <small>产生一个 `package.json` 文件, 里面有工程所需要的所有依赖项, 在copy他人的工程时，只需要把 `package.json` download 下来，然后 `npm i` 就可以了。</small>]  
>>> 2 `npm install --save/--save-dev` [ <small>`--save` 就是发布后，程序还需要用到的。而 `--save-dev(-D)` 就是只在开发中使用，程序发布后不再需要</small>。]

> 6 卸载模块: `npm uninstall pakage_name(-g)`  

> 7 更新模块: `npm-check -du` <small>(-d means -devlopment, -u means update by interactive</small>  
>> 首先，还得要安装上 `npm install npm-check -g1  










