1. @name：脚本名称
2. @namespace：相同命名空间的脚本运行在同一个上下文（共享变量）
3. @version：当前脚本的版本号，值得注意的是Tampermonkey支持脚本自动更新
4. @author：脚本作者
5. @contributor：脚本部分代码的贡献者，支持多值
6. @description：该脚本的简单功能和原理描述
7. @include：类似于@match，即打开的页面地址符合该通配规则，便自动运行该脚本，它们都支持多值
8. @exclude：与@match的功能刚好相反，当URL匹配成功时绝不运行该脚本
9. @require：被指定的JS脚本，需要先被加载并执行，然后才能开始执行该脚本
10. @resource：类似于上面的@require，但它指定的是一般的资源文件，加载后便可以在脚本中通过GM_getResourceURL和GM_getResourceText进行访问。
11. @run-at：脚本的运行时机，一般为document-start、document-body、document-end其中之一
12. @user-agent：重写所有的匹配成功URL的HTTP请求报文的头部为指定的值，具体取值可以参考
13. @grant 即是引入 API 的依赖，如：
JS 代码中需要使用GM_log，就需要引入依赖：// @grant GM_log

14. 自己的脚本实践:
```js
// ==UserScript==
// @name         谷歌搜索带百度
// @version      1.0.0
// @description  google with baidu button
// @author       Janet
// @grant        GM_openInTab
// @grant       GM_addStyle
// @grant       GM_getResourceText
// @resource    customCSS https://lib.baomitu.com/bttn.css/0.2.4/bttn.css
// @include      https://www.google.com/*


// ==/UserScript==
(function() {
    'use strict';
   var newCSS = GM_getResourceText ("customCSS");
   GM_addStyle (newCSS);

   function searchByBaidu(searchText) {
       return 'https://www.baidu.com/s?wd=' + searchText;
   }
   function baiduClick() {
       var searchText = document.querySelector('.gLFyf').value;
       GM_openInTab( searchByBaidu(searchText), false);
   }
   let box = document.querySelector(".RNNXgb")
   let mybtn = document.createElement("button")
   mybtn.innerHTML="百度"
   mybtn.setAttribute("type", "button")
   mybtn.setAttribute("class", "bttn-pill bttn-md bttn-primary")
   box.appendChild(mybtn)


   mybtn.addEventListener("click",(e)=>{
       e.preventDefault()
       baiduClick()
   })

})();
```
