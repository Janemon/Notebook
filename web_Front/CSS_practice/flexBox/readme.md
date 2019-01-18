采用 Flex 布局的元素，称为 Flex 容器（flex container），简称"容器"。它的所有子元素自动成为容器成员，称为 Flex 项目（flex item），简称"项目"。

无论什么布局，都是空间上考虑： 一是水平（默认为主）二是垂直

但是container是分水平轴和垂直轴的，而在这个空间里面的分布的元素则是按照水平轴和垂直轴分布，而主轴默认是水平，也是项目默认排列的方向。那么他占据的空间叫main-size 和 cross-size.

如果我们要用flex布局，那么就必须把某个元素的display 改成 `display=flex`,改完后我们可以允许里面的元素有 `absolute, relative, but not float`.
<mark>Note;</mark> 我们可以有 `display:inline-flex;`

容器上的属性：  
**[其实用 `flex-flow` 是下面两个的short-hand]**  
1- `flex-direction`, 规定了主轴的方向：水平是主轴（默认）还是垂直是主轴。  
> `row|column|row-reverse|column-reverse`  

2- `flex-wrap`, 规定能否换行  
> `wrap|nowrap|wrap-reverse(i第一行在最下面)`  

<mark>3-</mark> `justify-content`, 调整主轴上的项目对齐排列  
> `flex-start(left)|flex-end|center|space-between(最边没空间, 但是中间的项目间隔有且等间距)|space-around(最边有空间,且等间隔,但是还是中间项目的间隔大)`  

<mark>4-</mark> `align-content`, 调整垂直轴上的项目对齐排列，当可`wrap`可换行时，就是多行时，那么这个"垂直的调整用这个"，而不是`align-items`.  
> `flex-start(top)|flex-end|center|space-between|space-around|stretch`  
5- `align-items`, 调整垂直轴上的项目对齐排列(单列)   
> `flex-start|flex-end|center|baseline(项目的第一行文字的基线对齐)|stretch`(no `space-between and space-around`)  
**Note**: `align-self` 是为单独项目设置的，可与其他项目不一样，覆盖`algin-items`的值  
> 他的值和 align-items 一样  


项目上的属性：  
1- `order`, 项目的排列顺序，数值越小约靠前  
**[flex属性是下面三个属性的short-hand(默认值为 `0 1 auto`[不扩大，可缩小，width/height为原本值])]**  
> 一般是这两个快捷值: `auto(1 1 auto)` and `none(0 0 auto)`  

2- `flex-grow`, 项目的等比例方法，默认为zero  
3- `flex-shrink`, 项目的等比例缩小，默认为1, 如果空间不够就将项目缩小  
4- `flex-basis`, 项目的主轴空间(main-size)根据主轴是水平还是垂直分别为 width 或 height  

