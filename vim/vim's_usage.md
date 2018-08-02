1 <mark>**replace**</mark>  
　Using <mark>'r'</mark> in normal and we can replace it in new one. But if you want change more, you can't do that with <mark>'r'</mark> which only replace one letter. So you can use <mark>'cw'</mark> to replace more letter, and this is used in the 'insert' model. Of cousre, you can use <mark>'c$'</mark> to replace the whole line, **and the <mark>'cc'</mark> can really replace the whole line rather than replace the *'whole line'* which beginnig from the current cursor.** And we can combind some characters to use it, for example: <mark>'c2w'</mark>, <mark>'ce'</mark>, <mark>'cc'</mark> and etc.

--------------------------------------------

2 <mark>**Insert front of the cursor**</mark>  
　Using <mark>'i'</mark>, by contrary, using the <mark>'a'</mark> is insert after the cursor. 

-------------------------------------------

3 <mark>**undo**</mark>  
　Using <mark>'u'</mark>, if you want to undo the whole line, you can use the <mark>'U'</mark>

-------------------------------------------

4  the **begin** of word is <mark>'b'</mark>
　the **end** of word is <mark>'e'</mark>  
　the begin of whole line is <mark>'0'</mark>  
　the end of whole line is <mark>'$'</mark>, but i map it using <mark>'LE'</mark>  

5  the copy is <mark>'y'</mark>  
　the paste is <mark>'p'</mark>, but paste will create a new next null line  

------------------------------------------

6 delete a word(text word) no matter where the current cursor in the word is <mark>'daw'</mark> and it not only delete a word but aslo delete a space!

-------------------------------------------


7 *when you use the vim editor, you should <mark>distinguish</mark> serveral module in work. And now, i know that if i wanna <mark>write somthing</mark>, i should in the insert module. And if i wanna <mark>check and delete someting</mark>, i should return the normal module*

------------------------------------------

8 the dot <mark>'.'</mark> is the macro in vim, using it we can repeat the last change before the <esc> but it change **the command which are not the motion and it change in the normal module not the insert module. If you understand it, you will find that it meet the rule "Don't repeat yourself"

------------------------------------------

9 there is a lot of compound commands can be replaced in a singal command. For example: the 'c$' can be replace with 'C' and the '$a' can be replace with 'A'.  
　**#_#**, So? What their usage?  

-----------------------------------------

10 <mark>f{char}</mark> can move cursor to where the *char* is. And the <mark>';'</mark> will repeat find the char which <mark>'f'</mark> find last time and the <mark>','</mark> wil return reverse direaction to find the char but note that the find pattern just in line not in the whole file. For example:  
```javascript 
var foo"("+"argument1+","+argument2+")";
```
the Concatenating strings in JavaScript never looks pretty, but we could make this a litter easier on the eye by padding each + sign around with spaces using the above instructions.  
> 1. **f+**  
> 2. **s{space}+{space}<esc>** (<mark>'s'</mark> will delete the letter under current cursor then change in insert module)  
> 3. **;.**  
If we use the above instructions, we will reduce a lot of repeative activities.
<mark>ote</mark>: here is a instrunction is similar to <mark>f</mark>, it is <mark>t</mark> but the only one difference from <mark>f</mark> is that the cursor just appeal to in front of the right char.**<mark>f and t</mark>** is very useful to find what you want!

----------------------------------------

11 <mark>'%s/original/replacement/g'</mark> just find the original words and then replace it in the general  
**Note:** the __%__ means the whole file, and the __g__ means the whole line match rather than the only one match in one line. So the combination of these mean the whole file all match.  

---------------------------------------

12 <mark>`'*'`</mark> means it will find all the word under a current cursor and highlight them. Of course, then we could do something for these words! And the revise direaction is <mark>'#'</mark>, and we can add number in front of the command to show it will find which order of the thing, for example: <mark>3*</mark>. **So what usage do they have, when we have the similiar command of '/'.**  
**So as the Noraml modd in vim, the painter does not rest with a brush on the canvas**

---------------------------------------

13 The <mark><C-a></mark> and <mark><C-x></mark> commands performs addition and subtraction on numbers. But there are some specialties. If our cursor on a number, we running *10<C-a>* could modify it to read 15. However, if the cursor is not positioned on a numeric digit, the <mark><C-a></mark> will look ahead for a digit on the current line. For example:
```css {.line-numbers}
.blog {background: 0px 0px}
```
> 1. yyp
> 2. cw.news<Esc>
> 3. 180<C-x>

**the result is**
```css 
.news {background: -180px 0px}
```
**note**: the `<c-a>` and `<c-b> mean 'plus' and 'substract'.

---------------------------------------

14 <mark>**oprator + motion = action**</mark>,but it under a rule called **'operator pending mode'**, that means a state only accepts motion commands and then it is activated, but the pending state only keep within one second. we can use *:h operator* to see the whole list of operators. but in this mode, the instruction have to execute two times, then it work! for example:  
1. the <mark>dd</mark> means delte the whole line  
2. the <mark>gUgU</mark> means make the whole line uppcase.(*in my eye, i don't like this since it has 4 letters and mix lowwercase and uppercase*)  
3. the <mark>daw</mark> means delete a word  
4. the <mark>di(</mark> means delete the content in the parentness  
5. the <mark>yt.</mark> means copy the content till the dot.  
So geneally the operator are **d**,**c**,**y**. 

<mark>NOTE:</mark> vim **allow** you create any new movements, and these movement could work with any operator, Like:  
1 **:onoremap p i(**　　:delete the parameter in the parentness.  
2 **:onoremap tr /return<cr>**　　:delete the content till the word-'return'.  
**NOTE:** the *o* means any operator and the *p*, the *tr* mean the motion behind operator what you enter.  

But the problem is coming, the first step of a series of operation is the current cursur's position, so if we want more setout position of command execution, what can we do? we can like the fllowing:  
> 1. :onoremap np :<c-u>normal! f(vi(<cr>  
    yep, it has some complicated, but it is also realized esay. Let's do it:  
 >> 1. the mapping is select the next parameter and selet all the content in it, so it setout position is not the current cursor.  
 >> 2. <c-u> is used to clear the commands in the command line.
 >> 3. :normal! can let the content of command can execute like in the normal model. 
 >> 4. so the mapping is f(vi(  
> 2. :onoremap ih :<c-u>execute "normal! ?^\\+$\r:nohlsearch\rkvg_"<cr>  
 >> 1. the <mark>execute "..."</mark> will execute the content in **"..."**, and it will replace the special character in the **""** like:_\r, and \\ and etc._   
 >> 2. the <mark>normal!</mark> can recognize the special character so we add the execute in front of it, both them work together!  
 >> 3. so the mapping is actually the 1)?^\+$<cr> 2):nohlsearch<cr> 3)kvg and the last <cr> to return the instruction.  

----------------------------------

15 _Here we maybe feell something is simple, but actually we don't know how to use it when we meet them. For example, we keystroke the ':help' then we get into the help file! Then we see some files like <mark>'usr_90.txt'</mark> but we doo't know how to get access to it? Now, we can use <mark><C-]></mark> to down into and use <mark><C-o></mark> to get back!_

---------------------------------

16 Sometime, if the nest struct is complex, we will lost in it. Now, the command <mark>%</mark> is very useful. When our cursor is on one **(** or other. we can keystroke <mark>%</mark> then it will show the related **)**. Of course, it also work in **[]** and **{}**. We can use **matchpairs** to set it.

--------------------------------

17 we can use, in instance, <mark>33j</mark> to go the line 33.

-------------------------------

18 Ok, I know maybe it seem so esay for you, but you probably don't know how to use it! Now **ROLLING it**:  

1. <mark>< C-U ></mark> means rolling up half of screen (note: it is different from the <c-u> in the command mode)  
   <mark>< C-d ></mark> means rolling down half of screen

2. <mark>< C-f ></mark> means rolling down full of screen  
   <mark>< c-b ></mark> means rooling up full of screen

3. <mark>< C-e ></mark> means rolling up a line  
   <mark>< C-y ></mark> means rolling down a line

4. <mark>'zz'</mark> means set current line to the centrial in the screen.  
   <mark>'zt'</mark> means set current line to the top in the screen.  
   <mark>'zb'</mark> means set current line to the bottom in the screen.  

5. <mark>NOTE:</mark> What we talk about is the move of screen not the cursor.  

------------------------------

19 If we want to find the single entire word, not the relative key word. we can use <mark> \< word \> </mark>, the **\\<** and **\\>** design the beginnig and endding of the words.  

<mark>NOTE</mark>: Sometime we use **/** to find special character, commonly we find the first or last of a string of this characters. Take a instance: <mark>/^the</mark> or <mark>/$the</mark>

------------------------------

20 we can mark some specail line, then when we finish other jobs we can return to it. The command is that <mark>m[a-z]</mark> then when we want to go back to it we can use <mark>`[a-z]</mark>.

<mark>NOTE</mark>: **D** meanas delete the content from current cursor to the end of '__actual line__'. **C** means change the content from current cursor to the end of line.  

<mark>NOTE</mark>: if we want to use the square visual chunk, we don't simply use the *v*, we should use <mark><C-v></mark>.  

<mark>NOTE</mark>: the command **xp** means exchange the letter under current cursor and the leter behind it in each.  

<mark>NOTE</mark>: the **cc** is change the whole line. The <mark>cas</mark> is to change a sentence and <mark>cis</mark> also change a sentence but it don't change even the white space. The other thing is that <mark>~</mark> uupcase the current letter underthe cursor but the *u* is uppcase the select block in visual.

-------------------------------------------------

21 Let's think about such a situation that we have so many instrucions in conflict beacuse we have a lot of plugins in our vim! How can we improve it? Let's do it:  
In different files, we set different local setting which avoid conflits with others plugin's settings.  
The global setting are:  
(1) <mark>:nnremap <buffer> <leader>x dd</mark>  
(2) <mark>:setlocal nonumber</mark>  
But sometimes in the same file, we will get similiar setting like fllowing:  
<mark>:nnoremap <buffer> Q x</mark>  
<mark>:nnoremap Q dd</mark>  
The result is that the vim don't know how to use which settings.

-----------------------------------          

22 The <mark>autocmd</mark> just like his name! It's automatically! The form just like fllowing:  
<mark>:autocmd "listening_event" "fliter_pattern" :"execute_instruction"</mark>. Example:  
　**:autocmd FileType javascritp nnoremap <buffer> <leader>c i//<esc>**  
　**:autocmd BufWrite,BufRead *.html :normal gg<mark>**  
If we want to group thees autocmd'instructions conviently, we could use this:  
```
　　:augroup testgroup  
　　　:autocmd! // just delete it after used.  
　　　........  
　　:augroup END  
```
 It's not only conviently but also improve vim's run efficiency.  
Else: we can input <mark>:message</mark> to see vim's messages'file!

---------------------------------------

23 <mark>:set statusline</mark>... is the setting of the meaning of the words. And we must konw two points one is the **%** which will translate different meaning according to the fllowing charater, for example: the __%f__ means file_address and the __%y__means the fileType. And the other one is the whiteSpace should translate the semantic by **\**. And more meaning what you want to know, please see :help.

-----------------------------------------

24 <mark>vim -O file1 file2 ...</mark> can open in vertical meanwhile serval files

-----------------------------------------

25 <mark>ddp</mark> means exchange the up and down line And the <mark>xp</mark> means exchange the word front and back.

----------------------------------------

26 <mark><S-Tab></mark> means in *:split * command modole, we can select different files in current directory.

---------------------------------------


27 <mark>:normal command</mark> means that no matter in every module we can use this comman line to execute the operation of normal module. And it doesn't look esay at surface. we can combind it with other operator. For exmaple:
If we want add the _;_ in the end of line in the select zone, what can we do it? Fist, it is a repeat action, so we can combine with dot operator-<mark>.</mark>. The step of this operation are fllowing:
1. <mark>A;<Esc></mark>
2. <mark>jv</mark>
3. <mark>:'<,'>normal</mark> .(note:the '<,'> is auto appear when you in V-module,)
Note: Using v-module to execute the micro is the way of parallel. If we using this way 0f 5@a which called serial. And usually using micro by prallel is more fault-tolerant than serial.
And the <mark>%</mark> means all zone of the workPlace. For eample: <mark>%normal A;</mark>  
And actually, we sometime want to review some commands but we cover it by repeat the operation! And we can use uppername of the register to add it behind before pattern! 
*NOTE:* <mark>r</mark> means replace but when you key *r*, it will keep the before word when replace. But it just only replace one character if you want to replace a word using the <mark>s</mark>. 

-----------------------------------

28 <mark>:n</mark>, if we want to go to the special line-nth, we can use `:n`. For exmaple: we want to go to 12th line, we can type: ':12'

------------------------------------

29 <mark>m [a-zA-Z]</mark>, this command will mark some special line, when we want to reurn this line we can use <mark>'a</mark> or other you mark flag.

-----------------------------------

31 In vim's visual module, we can use the crow select but the worlds number must all same.
![picture](/home/janemon/图片/列编辑vim.png)

-----------------------------------

32 <mark><C-o></mark> means return the last editor position

---------------------------------

33 In vim, the <cr> means **carriage return** and sasme as <Enter> and <Return>. And you should note that the <cr> is different from <c-r>

----------------------------------


