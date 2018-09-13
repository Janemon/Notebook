# Introduce: bootstrap is font-end component library and toolkit for developing with HTML, CSS, and JS. And it is responsive, mobie-first.

## Bootstrap use normalize.css to keep the consistency of various browsers.

## How to mobie-first:
> add <meta name='viewport' content='width=device-width, initial-scale=1.0, user-scalable=no'>
1. **responsive img**
`<img src='...' class='img-responsive' alt='responsive-pic'>`
- the machanism:
```css
.img-responsiv{
   display: block;
   width:100%; // no auto
   height:auto; // no 100%
}
```
2. **Grid system**
- what is grid?
> Simply, the grid used to oganize the content to let the website easily browser!

- Since the mobie-first, the responsive grid system will assign 12 cols mostly autolly with the viewport size increase.

- Machanism:
  1. the rows must nest into the elements which class is '.container' which get the appropriate alignment and padding
  2. the core is the *.row* and _.clo-*-*_
  3. we use the media require rule to find the appropriate rule to fit the screen of different devices and the rule is set in less file.
  - note: the numbers of cols must less than the 12 and we have 4 types of clos which are *.col-xs*, *.col-sm-*, *.col-md-*, *col-lg-*
  - the simple example:
```html
<div class="container">
    <h1>Hello, world!</h1>
    <div class="row" >
        <div class="col-md-6 col-md-offset-3" 
        style="background-color: #dedef8;box-shadow: 
        inset 1px -1px 1px #444, inset -1px 1px 1px #444;">
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing 
            elit.
            </p>
        </div>
    </div>
</div>
```
3. Typesetting
- inline chid headline
`<h1>我是标题1 h1. <small>我是副标题1 h1</small></h1>`

- emphasis class
```html
<small>本行内容是在标签内</small><br>
<strong>本行内容是在标签内</strong><br>
<em>本行内容是在标签内，并呈现为斜体</em><br>
<p class="text-left">向左对齐文本</p>
<p class="text-center">居中对齐文本</p>
<p class="text-right">向右对齐文本</p>
<p class="text-muted">本行内容是减弱的</p>
<p class="text-primary">本行内容带有一个 primary class</p>
<p class="text-success">本行内容带有一个 success class</p>
<p class="text-info">本行内容带有一个 info class</p>
<p class="text-warning">本行内容带有一个 warning class</p>
<p class="text-danger">本行内容带有一个 danger class</p>
```

- list
```html
<h4>内联列表</h4>
<ul class="list-inline">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
  <li>Item 4</li>
</ul>
<h4>水平的定义列表</h4>
<dl class="dl-horizontal">
  <dt>Description 1</dt>
  <dd>Item 1</dd>
  <dt>Description 2</dt>
  <dd>Item 2</dd>
</dl>
```
4. table
```html
<div class="table-responsive">
	<table class="table table-bordered">
		<caption>响应式表格布局</caption>
		<thead>
			<tr>
				<th>产品</th>
				<th>付款日期</th>
				<th>状态</th>
			</tr>
		</thead>
		<tbody>
			<tr class='active'>
				<td>产品1</td>
				<td>23/11/2013</td>
				<td>待发货</td>
			</tr>
			<tr class='success'>
				<td>产品2</td>
				<td>10/11/2013</td>
				<td>发货中</td>
			</tr>
			<tr class='warning'>
				<td>产品3</td>
				<td>20/10/2013</td>
				<td>待确认</td>
			</tr>
			<tr class='danger'>
				<td>产品4</td>
				<td>20/10/2013</td>
				<td>已退货</td>
			</tr>
		</tbody>
</table>
</div>  	
```
```html
<table class="table table-hover table-striped table-condensed">
	<caption>悬停表格布局</caption>
	<thead>
		<tr>
			<th>名称</th>
			<th>城市</th>
			<th>邮编</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Tanmay</td>
			<td>Bangalore</td>
			<td>560001</td>
		</tr>
		<tr>
			<td>Sachin</td>
			<td>Mumbai</td>
			<td>400003</td>
		</tr>
		<tr>
			<td>Uma</td>
			<td>Pune</td>
			<td>411027</td>
		</tr>
	</tbody>
</table>
```
5. Form
- **Rule**
> 1. we should add _role='form'_ to the element of `<form>`
> 2. In order to get the best effection, we should put the label and controllers into the `<div>` with class name of *.form-group*.
> 3. the `<input>, <textarea>, <select>` should be added the class name of *form-control*.
- **the basic form**
```html
<form role="form">
  <div class="form-group">
    <label for="name">名称</label>
    <input type="text" class="form-control" id="name" placeholder="请输入名称">
  </div>
  <div class="form-group">
    <label for="inputfile">文件输入</label>
    <input type="file" id="inputfile">
    <p class="help-block">这里是块级帮助文本的实例。</p>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox">请打勾
    </label>
  </div>
  <button type="submit" class="btn btn-default">提交</button>
</form>
```
- **the inline form**
```html
<form class="form-inline" role="form">
  <div class="form-group">
    <label class="sr-only" for="name">名称</label>
    <input type="text" class="form-control" id="name" placeholder="请输入名称">
  </div>
  <div class="form-group">
    <label class="sr-only" for="inputfile">文件输入</label>
    <input type="file" id="inputfile">
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox">请打勾
    </label>
  </div>
  <button type="submit" class="btn btn-default">提交</button>
</form>
```
- **the horizontal form**
> Note: the `<label>` should be added a class called *.control-label*
```html
<form class="form-horizontal" role="form">
  <div class="form-group">
    <label for="firstname" class="col-sm-2 control-label">名字</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="firstname" placeholder="请输入名字">
    </div>
  </div>
  <div class="form-group">
    <label for="lastname" class="col-sm-2 control-label">姓</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="lastname" placeholder="请输入姓">
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <div class="checkbox">
        <label>
          <input type="checkbox">请记住我
        </label>
      </div>
    </div>
  </div>
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10">
      <button type="submit" class="btn btn-default">登录</button>
    </div>
  </div>
</form>
```

6. **Component** 
- *dropDowns*
> Rule: if we want to use the dropDown menu, we must embed it into a parent's element with class:'dropdown'
> and we add class:'dropdown-menu' and role:'menu' into the `<ul>`
example:
```html
<div class="dropdown">
    <button type="button" class="btn dropdown-toggle" id="dropdownMenu1" data-toggle="dropdown">主题
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">Java</a>
        </li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">数据挖掘</a>
        </li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">数据通信/网络</a>
        </li>
        <li role="presentation" class="divider"></li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">分离的链接</a>
        </li>
    </ul>
</div>
```
> Note: the data-toggle='dropdown' which is server for the javascript and it means the change based what events.
> here, we use 'dropdown' to toggle. And we always use data-target sametime, which means the target of event.



- *nav elements*
> Rule: first add '.nav' in the list=> `<ul>,<ol>,<dl>`
> 1. standard nav tabs:
```html
<p>标签式的导航菜单</p>
<ul class="nav nav-tabs">
  <li class="active"><a href="#">Home</a></li>
  <li><a href="#">SVN</a></li>
  <li><a href="#">iOS</a></li>
  <li><a href="#">VB.Net</a></li>
  <li><a href="#">Java</a></li>
  <li><a href="#">PHP</a></li>
</ul>
```
> 2. (1)standard capsule nav:
```html
<p>基本的胶囊式导航菜单</p>
<ul class="nav nav-pills">
  <li class="active"><a href="#">Home</a></li>
  <li><a href="#">SVN</a></li>
  <li><a href="#">iOS</a></li>
  <li><a href="#">VB.Net</a></li>
  <li><a href="#">Java</a></li>
  <li><a href="#">PHP</a></li>
</ul>
```
     (2) vertical capsule nav:
```html
<p>垂直的胶囊式导航菜单</p>
<ul class="nav nav-pills nav-stacked">
  <li class="active"><a href="#">Home</a></li>
  <li><a href="#">SVN</a></li>
  <li><a href="#">iOS</a></li>
  <li><a href="#">VB.Net</a></li>
  <li><a href="#">Java</a></li>
  <li><a href="#">PHP</a></li>
</ul>
```
> 3. the nav with dropDown
```html
<p>带有下拉菜单的标签</p>
  <ul class="nav nav-tabs">
    <li class="active"><a href="#">Home</a></li>
    <li><a href="#">SVN</a></li>
    <li><a href="#">iOS</a></li>
    <li><a href="#">VB.Net</a></li>
    <li class="dropdown">
      <a class="dropdown-toggle" data-toggle="dropdown" href="#">
        Java <span class="caret"></span>
      </a>
      <ul class="dropdown-menu">
        <li><a href="#">Swing</a></li>
        <li><a href="#">jMeter</a></li>
        <li><a href="#">EJB</a></li>
        <li class="divider"></li>
        <li><a href="#">分离的链接</a></li>
      </ul>
    </li>
    <li><a href="#">PHP</a></li>
```

- *nav bar*
> Rule: First=> add class:'.navbar', '.navbar-default' and the role:'navigation' into the `<nav>`. Second=> Inorder to add the links,
> we should add class:'.nav','.navbar-nav' into the `<ul>` 
> 1. the standard nav-bar:
```html
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">菜鸟教程</a>
    </div>
    <div>
        <ul class="nav navbar-nav">
            <li class="active"><a href="#">iOS</a></li>
            <li><a href="#">SVN</a></li>
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                    Java
                    <b class="caret"></b>
                </a>
                <ul class="dropdown-menu">
                    <li><a href="#">jmeter</a></li>
                    <li><a href="#">EJB</a></li>
                    <li><a href="#">Jasper Report</a></li>
                    <li class="divider"></li>
                    <li><a href="#">分离的链接</a></li>
                    <li class="divider"></li>
                    <li><a href="#">另一个分离的链接</a></li>
                </ul>
            </li>
        </ul>
    </div>
    </div>
</nav>
```
> Note: class:'container-fluid' is different to class:'container'. one is take up the 100% of view port
> but other is dynamically assign the screens

> 2. the collapse nav-bar 
> Rule: Actually, the collapse nav is a button with class:'.nav-toggle', and data-toggle='collapse', data-target='...'
example:
```html
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid"> 
    <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse"
                data-target="#example-navbar-collapse">
            <span class="sr-only">切换导航</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="#">菜鸟教程</a>
    </div>
    <div class="collapse navbar-collapse" id="example-navbar-collapse">
        <ul class="nav navbar-nav">
            <li class="active"><a href="#">iOS</a></li>
            <li><a href="#">SVN</a></li>
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                    Java <b class="caret"></b>
                </a>
                <ul class="dropdown-menu">
                    <li><a href="#">jmeter</a></li>
                    <li><a href="#">EJB</a></li>
                    <li><a href="#">Jasper Report</a></li>
                    <li class="divider"></li>
                    <li><a href="#">分离的链接</a></li>
                    <li class="divider"></li>
                    <li><a href="#">另一个分离的链接</a></li>
                </ul>
            </li>
        </ul>
    </div>
    </div>
</nav>
```

3. the form in nav-bar
> Rule: class:'.navbar-form'
```html
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid"> 
    <div class="navbar-header">
        <a class="navbar-brand" href="#">菜鸟教程</a>
    </div>
    <form class="navbar-form navbar-left" role="search">
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Search">
        </div>
        <button type="submit" class="btn btn-default">提交</button>
    </form>
    </div>
</nav>
```

4. the links with pic in nav
> Rule: class:'glyphicon glyphicon-*'
example:
```html
<nav class="navbar navbar-default" role="navigation"> 
    <div class="container-fluid"> 
        <div class="navbar-header"> 
            <a class="navbar-brand" href="#">菜鸟教程</a> 
        </div> 
        <ul class="nav navbar-nav navbar-right"> 
            <li><a href="#"><span class="glyphicon glyphicon-user"></span> 注册</a></li> 
            <li><a href="#"><span class="glyphicon glyphicon-log-in"></span> 登录</a></li> 
        </ul> 
    </div> 
</nav>
```


# last. We know that in Bootstrap, the various kinds of effection by adding the special class name to achive! Althought, there are lots of thing we haven't talk about, but we already realize how to use the appropriate rules to build the beautiful style according the above information.
