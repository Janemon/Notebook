#### 其实无外乎两种方法：
1. 自己下载安装包<small>(官网、github)</small>，自己解压，自己编译，自己选择路径安装。  
2. 通过安装程序，一站式进行配置安装, 比如：Ubuntu的`sudo apt-get install ...` 。  

---------------------------------------------------------------------

#### 1 关于 ubuntu 的 安装，升级和卸载

1. 如果是U盘安装各类系统，一般网上会有各种装机软件下载，对我一般使用 _大白菜_ ，但是各类使用软件使用方法都类似。过程：
> 1 下载U盘启动盘制作工具，并准备U盘  
> 2 使用制作工具对 U盘 进行格式化并制作成 U盘启动盘  
> 3 把系统镜像放进去  
> LAST 把电脑资料安置好后，重启电脑并把U盘插上，按`<F2>/<F12>' 设置成U盘为第一启动项, 进入界面，进行安装，等待完成！  

2. 如果直接在原本的 _linux系统_ 上进行U盘启动盘制作，也可以，步骤如下：
> 1 `sudo fdisk -l`, 查看U盘设备号，根据U盘的内存可以辨别出，一般为：`/dev/sdc`  
> 2 `sudo umount /dev/sdname*`  
> 3 `sudo dd if=~/downloads/ubuntu-18.04-desktop-amd64.iso of=/dev/sdname` 把你的镜像文件压入U盘中  
> LAST， 等待装入完成。。。  

3. <mark>如何通过命令格式化U盘</mark>  
> 1 `sudo dd count=1 bs=512 if=/dev/zero of=/dev/sdname`  
> 2 `sudo fdisk /dev/sdc`  
>> 出现列表项，让你选择，请按：p，默认回车，n，t，1, 7，w。  

> 3 `sudo umount /dev/sdc1`(一般是为 _sdc1_ )  
> 4 `sudo mkfs.fat /dev/sdc1`  

4. <mark>在 Ubuntu 上安装 Ubuntu图是最简单的</mark>  

输入 `sudo usb-creator-gtk` 就有一个图形界面，然后**两步搞定**！！

--------------------------------------------
##### ubuntu 安装完成后，因不是外国用户，需要安装的东西有点多

1. 有时候系统可能会马上更新一些补丁，但是有时候会迟点，这无所谓，反正到时候都要选择更新的

2. 首先先安装中文输入法吧，就用搜狗拼音了，毕竟他已经熟悉我的打法了
> 1. 去官网上下载 搜狗的linux拼音版本  
> 2. `sudo apt-get install facitx` and `sudo apt  --fix-broken install`  
> 3. 进入 ”region and language“，设置为全局应用并且框架选择为 ”facitx“  
> 4. 系统重启，会发现右上角有个键盘的图标，点击，进行 ”设置当前输入法“, 进入之后点击 `+` 添加 sougou Pinyin。 完成。

3. 安装 ”google-chrome“ 
> 1. `wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`
> 2. `sudo dpkg -i google-chrome*`
> 3. `sudo apt-get -f install`
> 4. 安装翻墙插件： 一般来说最简单的还是： ”谷歌访问助手， 谷歌上网助手， setup vpn“ 等等，可能会挂，到时候自己再搜，一般可以到chrome插件网去搜索  




--------------------------------------------

##### ubuntu 软件升级与卸载  

1. 更换国内源，建议选择高校及大企业源 `~/etc/apt/sources.list`  

2. 安装升级： `sudo apt-get check` => `sudo apt-get update` => `sudo apt-get dist-upgrade` => `sudo apt-get upgrade` => `sudo apt-get autoclean`  

3. 删除清理： `sudo apt-get remove packname --purge / sudo apt-get autoremove --purge`  

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

---------------------------------------------------------------------

#### 4 关于linux 中的解压与压缩  

> [-v ='verbose', -x ='extract', -f ='file', -c ='compress', -z='gzip' ]  

1. 解压：`tar -xvf target -d destination`, `unzip target -d destination`  
2. 压缩：`tar -zcvf destination target`, `zip destination target`  

---------------------------------------------------------------------









