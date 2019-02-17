1 首先自己本地得有一个仓库
  `mkdir Test_git`
> 或者使用第二步的操作 (git init Test_git)
       
-------------------------

2 让git来管理你仓库里面的工程
  `git init`

-------------------------

3 创建你的工程.这里假设你的工程现在只做出一个 readme.txt 文件
  `vim reademe.txt`

-------------------------

4 把这个readme.txt 文件追踪起来(这是第一步,我们要做的版本控制当然是得把他添加进来git的控制中),添加到 working dictionary(另一些资料称为:Index)
  `git add .`
  (注意: 我们没修改一次都要add一下用于追踪)

-------------------------
         
5 检查情况
  `git status`
  
-------------------------

6 如果此时,你还想在修改一次的话,那么修改完后,可以查看前后有什么不同的地方
  `git diff`(工作区和暂存区的区别)

-------------------------

7 最后,如果确认无误后,我们就可以真正地去保存他了(Head).
  `git commit -m 'des'`

-------------------------

8 当然如果我们是团队开发的话,那么我们必须建一个中心仓库来管理整个团队的工程项目.
> 所以我们得链接上这个远端的中心仓库(提交到远程github 上的仓库, 你也得要在上面有才行啊 #_#!).  

`git remote add name referenced-address`
> remote add 表示了和本地的 add有所不同  
> 当我们不需要了，我们可以：`git remove name`  
> 如果我们把当地的仓库push到一个完全没有联系的远程仓库中去的话，那么我们99%会失败，所以我们必须把上游和我们产生冲突的分支拉下来,一般用`git fetch branch`. 不用`pull`是因为他直接两步走了： 先fetch下来，再merge掉, 会有一定风险。[其实我们]  
> `fast-foward` 表示树没有共同的祖先  
> 如果一开始**add**的时候出现了`fast-forward`的情况，那么这个情况会更加复杂，我们在**fetch**后的merge时会有出现**merge unrelated histories**所以我可可以添加**--allow-unrelated-historries**到**merge**中去[其实这个选项太长了，我们可以在 `git --help` 中 cut下来]  
> 其实用**改基**也可以解决种鸽冲突问题  

<mark>NOTE:</mark>  
当然有些时候我们是直接在github上直接clone 那个中心仓库的工程项目,而不用自己建一个.
  `git clone referenced address`

-------------------------

9 那么和remote链接上了之后,我们可能被分配创建一个新的分支
       `git branch branch_name`
 
-------------------------

10 如果我们想要切换到另一个分支的时候那么我们可以这样做:
        `git checkout otherBranch_name`

 -------------------------

11 当我们完成了自己所完成的功能时候,我们就要把他提交到中心仓库上了
        `git push origin<1> master<2>`
> 1 假设是提交到remote的分支,默认是主机上的master)  
> 2 假设是当前要提交的分支,默认的也是这个  

  ![git_origin_otherExplain](../datapi/git_origin_ohterExplain.png)  
  ![git_origin_otherExplain2](../datapi/git_origin_otherExplain2.png)  
<mark>NOTE:</mark> 有时候这个分支(可能是master也可能是branch)与多个主机存在追踪关系,可以用 -u 选项指定一个默认的主机, 这样后面就不用加任何参数了  
   `git push -u origin master`  
> 第一次上传有可能会遇到push失败的情况，那是因为跟SVN一样，github上有一个README.md 文件没有下载下来 。我们得先`git pull --rebase origin master`，然后执行`git push -u origin master`就可以成功啦.  
> 如果你提交的是分支那么就不是 **master**了，就是你提交的那个分支名:`branchName`  
> 这个时候需要提交密码.  

-------------------------

12 查看当前有那些remote链接:
        `git remote -v`

-------------------------

13 如果我们提交上去的branch已经被管理者所merge了,那么我们可以在本地上merge该分支,然后删除这个已经merge 的分支,如果可以顺便把remote的该分支也删了.
        `git checkout master(假设是主分支)`
        `git merge required_branch`
        `git branch -d required_branch`[这就是删除分支]
        `git push origin(假设是远端的主分支) --delete required_branch`

-------------------------

14 当然不止你一个在打理一个分支功能,那么你也要吧别人的修改的东西拉到自己的本地分支了:  
        `git pull origin request_branch`  
> 1 如果就是合并到这个分支的话,那就不用再打名字了, 其实如果出来工作了的话, 这是不是经常做的事  
> 2 如何你在之前已经设定了默认主机,那么根据情况, 你可以像 'git push' 那样直接: `git pull`

-------------------------

15 如何我们想删除每个文件, 我们可以  
        'git rm file_name`  
> 1 其实直接在工作区中 `rm ...` 那么还得 `git add .` 把情况**add**进去, 而 这个这不用。  
> 2 这样就把文件从git仓库中删除了(也就是说不再被git追踪了), 并且连工作区中的文件也一并删除了  
> 3 如果我们只想把他从git仓库中删除但是不在工作区内删除的话,  
        `git rm --cached file_name`  
    Note: 最后,我们如果想要在github上也一并删除的话那么就得要 'git commit -> git push'

-------------------------

16 如何我们想要重命名,那么 status 会显示出这样的操作吗?  
        `git mv olafilename new filename`  
   答案是: 会的

-------------------------

17 如果我们想要查看提交的日记,我们可以  
        `git log`  
    如果我们想要查看提交的内容差异:  
        `git log -p`  
    如果我们想要查看所有分支的提交内容:  
        `git log --all`  
    如果我们想要查看简洁的提交内容:  
        `git log --oneline`  
    如果我们想要查看最近几次的提交内容:  
        `git log -n2`[这里表示最近2次]  
    如果我们想要查看某个分支提交的内容:  
        `git log branchName`  
    如果我们想要查看提交的内容层级:  
        `git log -graph`  

-------------------------

<mark>NOTE:</mark>
1. 我们知道在git下有三个区:  
首先, 是我们的**暂存区(Index)** 这是我们 **'git add'** 后的区  
其次, 是我们的**完成区(Head)** 这是我们 **'git commit'** 后的最终区  
最后, 是我们的**工作区**, 就是我们实际上操作的区域但没有被git跟踪,换句话来说其实他和git没有什么关系.  

2. **`git config --list`**  
    这个是查看配置信息的  
    ![git_config_setting1](../datapi/git_config_setting1.png)  
> 1. `git config --global`[当前用户的所有仓库]  
> 1. `git config --system`[所有登陆的用户]  
> 1. `git config --local`[仅仅是针对当前仓库]  

3. **`.gitignore`**
    这个是在git中可被忽略的文件:  
>> 1 '#' 表示注释  
>> 2 '/' 表示这个忽略的是目录  

4. **git status** 是仅仅显示了那些文件做了修改, 有没有被 add 或者 commit,  
   而**git diff** 这是显示了那些还没被add的文件做了什么样的修改,  
   而**git diff --cached**这是显示了还在暂存区和上次提交的区别,做了那些修改.  

5. **`git commit -am'...'`**  
   是可以不用'add' 就可直接提交file了.But the file must be 'add' before  

6. 如果想要知道如何设置SSh秘钥, 上网搜索吧!  

-------------------------

18 换行: 在行末加两个空格键和一个回车键. (<c-Enter>)
    分段: 段落之间空一段

-------------------------

19 如何解决冲突, 选择一个你真正想修改的而放弃另一个.  
![git_solveConflict1](../datapi/git_solveConfict1.png)  
![git_solveConflict2](../datapi/git_solveConflict2.png)  
![git_solveConflict3](../datapi/git_solveConflict3.png)  
如我们看到的, 在 `========` 上方的是我们当前仓库所在与远程仓库同一行的修改, 那么下方当然是远程仓库的修改咯.  

-------------------------

20 I don't know???  
![git_log1](../datapi/git_log1.png)  

-------------------------

21 现在, 让我们来谈谈关于分支合并和处理冲突的东西吧:  
> 1 正如前面所说, 我们可以通过 `branch` 命令来创建分支, eg: `git branch issue1`. 如果我们不指定参数而执行的话, 那么他就会显示分支列表.  

> 2 切换分支, 也如之前所说的, 可以用到`checkout`, `git checkout issue1`. 不过值得注意的是, 我们如果切换到那个工作区工作, 那么我们的 **Head**(用我自己的话来说这个是**完成区**), 就在那个分区.  

> 3 如果我们切换到了issue1中, 并且有内容提交了. 那么流程图是这样的:  
    ![git_branch3](../datapi/git_branch3.png)  

> 4 如果我们想合并分支了, 那个我们可以使用`merge`, 先切换到 `master` 分支,确认一下内容是否已经合并了, 没有的话, 那么我们就可以合并他,eg: `git merge issue`  
    ![git_branch4](../datapi/git_branch4.png)  
完成之后, 打开文档, 确认内容是否已经更改.如果更改了的话, 你又不再需要这个分支, 那个可以把他delete: `git branch -d <branchname>`.  

> 5 假如我们多个分支进行工作的话, 那么可能会出现以下情况:  
    ![git_branch5](../datapi/git_branch5.png)  
    ![git_branch6](../datapi/git_branch6.png)  
    ![git_branch7](../datapi/git_branch7.png)  
我们开始可以合并issue2, 但是合并issue3就会出现冲突, 那么就是说有某处这两个分支是做出了不同的修改.  
    ![git_branch8](../datapi/git_branch8.png)  
    ![git_branch2](../datapi/git_branch2.png)  
    ![git_branch1](../datapi/git_branch1.png)  
那么做出了修改之后, 解决冲突部分, 重新提交, 比如像这样:  
    ![git_branch9](../datapi/git_branch9.png)  
上面这种是其中一种合并分支的方法, 但是这种合并分支的方法, 会让历史记录看起来有点乱啊(但是我觉得挺好的啊), 接下来介绍第二种方法:  
>> 1 ![git_branch10](../datapi/git_branch10.png)  
 
>> 2 比如,现在我们回到`issue3`, 并把它合并到 `master`上.=> `git checkout issue3`, `git rebase master`, 此时我们就像上面那种方法一样, 冲突依旧存在, 我们像之前一样, 修改内容就行.  

>> 3 最后, 把修改过后的文件 `add` 好, 并且将rebase进行到底: `git rebase --continue`  
   ![git_branch11](../datapi/git_branch11.png)  
   
>> 4 最后, 尽管这个合并主要都是在分支上进行, 但是我们最后还是得要回到master上进行合并: `git checkout master`, `git merge issue3`  
      ![git_branch12](../datapi/git_branch12.png)  

<mark>最后, 总结两个办法的不同:</mark>  
> 1 **_第一种_**: 我觉得操作比较直观而且历史记录比较详细,但是多过头的话, 这种方法就会显得记录的比较'复杂难看'. 这种方法:**全部操作都是在master上进行的**  

> 2 **_第二种_**: 这种的话操作如果你懂的话也是比较简单直观的, 相比上一种方法, 他的记录不会那么详细, 因为最后他都不会记录分支的'路径记录', 但是这样在流程图上就看起来比较直观, 即使是多个分支时, 也一样.这种方法:**他的前期操作都是在分支上, 到最后需要合并的时候才会回到master**.  

-------------------------

22 现阶段我们一般是使用 `pull` 来更新数据, 但是其实如果说安全一点还是用 `fetch` 比较好. 因为 **fetch** 他是不会**自动合并**的, 你可以在merge前, 查看更新情况, 然后在决定是否合并, 当然 **pull**也有他的好处, 就是比较方便和省事.  

-------------------------

<mark>NOTE:</mark> **额外知识点： .git**  
1. **HEAD**文件里面的内容是表示当前工作分支, 例如： `ref: refs/heads/dev`  
2. **config**文件就是配置内容，比如用户信息，分支情况等等  
3. **refs**目录里面存放的是，分支：`heads`，远程主机：`remotes`，标签：`tags`  
4. **objects**目录里面存放的是，各类文件，主要类型有 **commit**[提交], **tree**[树], and **blob**[文件]  
> 我们使用 `git cat-file -t name`来查看文件类型, `git cat-file -p name`来查看文件内容  

**那么commit，tree，blob三者的关系是什么呢？**  

![commit_tree_blob](../datapi/commit_tree_blob.png)  

![commit_tree_blob](../datapi/commit_tree_blob2.png)  

> HEAD 虽然指向的是分支但是分支最终的工作还是提交“commit”  
> 一个commit类型的文件里面有两种类型的文件，一个是对应文件夹的 **tree**, 另一个是对应文件(文本文件)的 **blob**  

-------------------------

23 分离头指针（detached HEAD)  
> 就是指分离 HEAD, 就是直接 checkout 某个 commit  
> 本质上就是工作在没有分支上的情况,没有和branch挂钩  
> 所以如果一段时间后你没有把它向某个分支挂钩，那么git就会把它当做垃圾从而抛弃他  
> 而当你切换的时候会提示让你 `git branch <new-branch-name> commitName`, 来保存变更下来  
**按我的理解就是，这是一个极具实验性和随意性的方法，随意是指他对这个改动可有可没，实验性就是心血一来想实验一下**  
<mark>NOTE:</mark> **变基** 是离不开 datached HEAD

-------------------------

24 修改提交记录"commit"  

1. **修改最新的提交记录**  
> `git commit -m"desc" --amend`  

2. **修改某个提交记录**  
> 必须是修改他的父级提交  
> `git rebase -i commitName`  
> 提交记录是不同 `log` 给出的，他是最下面的是最新的，最上面的是最旧的  
> 要去读懂git弹出窗口给你的提示，`pick` 指的是 **pick out** 不受改变的提交, **reword** 指的是只改提交的描述信息。  
> 注意第一次改的是前面的命令，比如改成 `r`[reword], 第二次改的才是内容  

3. **整合连续的提交记录**  
> `git rebase -i commitName`  
> **s[squash]**，在选中的连续的commit的前面改成 **s**, 就是把这些commites合并到他们的前面一个commit  
> 最好在后一个弹窗上写上合并的理由  

4 **整合不连续的提交记录**  
> `git rebase -i commitName`  
>  其实只需要把需要合并的那些commits剪切到那个依附的父级commit下, 然后在重复"整合连续提交记录"的操作  
> 需要注意的是，我们可能有时候会出现一些警告，这时候我们可以按他的提示来进行操作比如 `git rabase --continue`, 就可以继续操作了  

-------------------------

24 diff 命令的使用   

1. `git diff --cached` : 比较INDEX和HEAD之间文件的差别(就是比较暂存区和已提交的区别)  

2. `git diff` ： 比较的是工作区和暂存区之间的文件差别(主要是看有有哪些文件没有被被add和文件中有那些修改)  

3. 我们可以 `git diff -- f1 f2 ...`, 后面加多个命令，比较单个或者多个命令的区别  

4. 比较不同分支、不同提交，不同分支的指定文件的区别：  
   `git diff branch1 branch2` : 这是指向该目录最近的一次提交  
   `git diff branch1_commit_code branch2_commit_code` : 直接比较分支某次提交  
   `git diff branch1 branch2 -- pointed_file`

-------------------------

25 不想要变更了怎么办？  

1. Index 里面的全部变更都不要了, 让INDEX保持和HEAD一样的进度：  
> `git reset HEAD`:  之后我们可以通过 `git diff --cached` 来暂存区和HEAD之间的区别，判定是否生效。  
> 如果只想不要其中部分只需要： `git reset HEAD f1 f2 ...`  

2. 工作区中的变更不想要了(使用情况： 觉得自己的工作区的变更还不如已经在暂存区中的变更好，想要作废掉)  
> `git checkout -- file`

-------------------------

26 如何消除**最近**提交的几次commit记录？  
<mark>这个我觉得很少能用得到，没必要消除记录，而且这种操作具有一定的风险性</mark>  

1. `git checkout 到需要删除记录的分支`  
2. `git reset --hard 到不需要删除的分支commit代码`(注意这种操作只能是消除最近几次的commit记录, 分支变成到这个状态)  

-------------------------

27 如果在开发中当前分支之前的提交在线上出问题了，我们怎么办？  

1. 我们需要把当前所做的更改保存下来，并且还原回提交时的版本： `git stash`  
2. 现在我们有一个干净的目录了，可以修复bug了  
3. 修复完bug之后，我们需要把之前保存下来的修改在拿回来： `git stash apply`  
> 还可以用`git stash pop`, 不过之后 `git stash list` 的内容就清空了  
4. 最后我们要注意的是，因为修改后的代码和现在拿回来的代码肯定会有不同的所以会产出出冲突，所以我们要好好清除掉冲突就可以了  

-------------------------

28 ![常用传输协议](../datapi/常用传输协议.png)  

之前有个误解，就是git只能和网络上的远程主机一起使用，其实本地的也可以: 你可以在一个终端中建立一个git仓库，然后在另一个终端中clone或者push到这个“远程仓库”(`git remote add name[代替的是后面那一个大串地址] ip`)中去, 使用的是一般是只能协议： `file://path/.git`( .git 是必须得加的)  

-------------------------

29 不同的人修改了不同的的文件该如何处理？

<mark>情况:</mark> 在github上新建了一个分支, 不同的两个人修改不同的文件  

1. 在其中一个开发者的工作目录下，checkout这个新的分支：`git checkout -b branch_path remote_host/branch_path`(表明这是基于远端而在本地产生的新的分支)  
2. 我们另一个开发者也可以直接`fetch`下来，但是这个新增的只是远端的分支，本地还是没有，所以还是像上一个分支那样branch一个分支，最好还是和远端的分支同名，这样不会混淆。  
3. 后来两个人修改了不同的文件内容，所以我们要每天上班后必须`fetch` ，我们可以看fetch后面显示的信息看看到底是那个分支产生了变化，还可以`git branch -av`来看看分支和远端的差异：**ahead 1, behind 2**这样代表比远端多了一个变化，和少2个变化  
4. 我们 `push` 文件产生了冲突  
5. 最后我们可以 merge 这个远端的分支，`git merge host_name/....`(commit_code is ok too), 因为是不同文件的内容，所以merge是比较简单的  

<mark>注意：</mark> 我们都可以通过同一分支的commit来看看是否产生了变化，如果是，那么就可以确定是发生了变化。

-------------------------

30 不同的人修改了同样的文件的不同区域该如何处理？

其实和上面那个一样的处理，这时候字节`git merge`就可以了。自动就合并。  

-------------------------

31 不同的人修改了同样的文件的同样的区域该如何处理？  

当我们push的时候出现警告,我们可以:  
1. `git pull`  
2. 出现冲突了，和同事沟通编辑解决冲突  
3. 添加修改后的文件，commit后再push  

-------------------------

32 不同的人修改了同样的文件的文件名该如何处理？  

1. 首先push的时候肯定会有冲突，那么我们可以pull下来，然后和另外改文件的那个人沟通  

2. 沟通成功后，删除不要的那些名字，然后(可以 `git status` 来看建议)我们我们把留下来的那个add后再提交push就行了  

-------------------------

31 协同合作时，有那些禁止项?   

1. 不能 `git push -f ...`  
> 但是如果是自己的话，那么可以把历史记录恢复到某个commit阶段  
> examples: `git push -f host_name commit_code:branch_name`  

2. 公共分支不能 `git rebase ...`  

-------------------------

32 github是有高级搜索的:

1. in:readme 是可以提高搜索质量的  

2. stars:>1000 搜索stars多余1000的  

3. filename:... 在代码中搜索资料(注意他显示结果是代码块)  

<mark>我可可以在 advanced search里面学习</mark>

-------------------------

33 如何创建一个团队(organization)项目管理?  

1.  **setting** => **organizations** => **new**  
2.  合并的时候，合并主分支是**base**, 即将被merge掉的分支是**compare**a  
> 现在github上也可以编辑解决冲突了  

<mark>改变历史的三种方法：</mark>  
> 1 **pull : 就是直接合并**  
![git_pull_merge](../datapi/git_pull_merge.png)  

> 2 **squash：不改变分支，只是把历史合并后放进主枝上(线性)**  
![git_squash_merge](../datapi/git_squash_merge.png)

> 3 **rebase：不改变分支，只是把每个历史放进主枝上(线性)**  
>> 这个是最线性的，但是比上面两个麻烦，因为rebase会不断让你修复冲突  
>> `git config --global rerere.enable true` 听说这个可以自动解决，但还是不断的 `git rebase --continue`  

![git_rebase_merge1](../datapi/git_rebase_merge1.png)  
![git_rebase_merge2](../datapi/git_rebase_merge2.png)  

