// ==UserScript==
// @name         谷歌搜索栏带百度按钮
// @version      1.0.0
// @description  google banner with baidu button
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
  GM_addStyle (`
     #mybtn{
         line-height:10px;
     }
   `)

  function searchByBaidu(search_content) {
    return 'https://www.baidu.com/s?wd=' + search_content;
  }
  function baiduClick() {
    var search_content = document.querySelector('.gLFyf').value;
    GM_openInTab( searchByBaidu(search_content), false);
  }
  let box = document.querySelector(".RNNXgb")
  let mybtn = document.createElement("button")
  mybtn.innerHTML="百度"
  mybtn.setAttribute("type", "button")
  mybtn.setAttribute("id", "mybtn")
  mybtn.setAttribute("class", "bttn-pill bttn-md bttn-primary")
  box.appendChild(mybtn)

  mybtn.addEventListener("click",(e)=>{
    e.preventDefault()
    baiduClick()
  })

})();
