语言特点：
    语法简洁
    类库丰富
    可扩展
    跨平台
    开放源码



1990年Python诞生
python目前主流是3.x, 2.x已经是过去了。（或许以后3.x也是这样的）
python发行版是集成了一些必要和常用的库了
?? iPython, jupyter notebook ??
python的IDE是 Pycharm



python 使用 `#` 进行单行注释
使用4个空格来进行语句缩进
使用`import`来进行导入包
使用`print`来进行输出



基本数据类型
    int
    float
      如果是js那么只有同一为 number
    str
    bool
使用 `type(...)` 来进行识别数据类型
数据类型转换
    int()
    str()



网络带宽和下载速度不是对等的
    带宽是使用bit作为单位，而下载速度是使用byte来作为单位
```python
bandwidth = input("请输入带宽: ")
bandwidth = int(bandwidth)
result = bandwidth / 8
print("下载速度是： ", result)
```
案例：根据带宽计算下载速度
变量可以直接创作而不用使用标识符
变量名要有意义而且开头必须是字母，数字，和下划线



案例： 计算生肖和星座（简版）
    确定一个生肖年份，然后根据余数来进行估算
```python
year = int(input("请输入年份： ")) # 因为input而来的变量值类型为字符
shengxiao = '豬鼠牛虎兔龍蛇馬羊猴雞狗'
standard = 2019
result = (year - standard) % 12
print("生肖是: ", shengxiao[result])
```

   星座和日期以元组一一对应，这里我是用开始日期来进行判断选择，当然也可以用结束日期来进行,
   通过这个小案例，更全面认识for和while
```python
constellations = ("水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座",
                  "天秤座", "天蝎座", "射手座", "摩羯座")
days = ((1, 20), (2, 19), (3, 21), (4, 20), (5, 21), (6, 22), (7, 23), (8, 23),
        (9, 23), (10, 24), (11, 23), (12, 22))
month = int(input("请输入月份： "))
day = int(input("请输入日份: "))
standard = (month, day)
# for n in range(len(days)):
    # if days[n] == standard:
        # print("你的星座是 ", constellations[n])
        # break
    # elif days[n] > standard:
        # print("你的星座是 ", constellations[n - 1])
        # break
    # elif month == 12 and day > 22:
        # print("你的星座是 ", constellations[11])
        # break

n = 0
while days[n] < standard:
    if month == 12 and day > 22:
        break
    n += 1
if days[n] == standard:
    print("你的星座是 ", constellations[n])
else:
    print("你的星座是 ", constellations[n - 1])
```

序列：有序，有下标, 可访问一个或多个成员
    字符串:"abcd"
        str="abcd"
        print(str[0]) # a
        print(str[-1]) # d
        print(str[0:3]) # 第一个是begin_index, 第二个是检索个数. abc
    列表([0,"abc"])
        其实数组一开始只能存放同种数据类型的数据，所以这里他遵守了这种方式。
        对比元组，他的内容一般是可变更的
        基本操作有`append(member)`和`remove(member)`
    元组都属于序列(("a", "bcd"))
        元组里面的数字成员可以进行比较
        对比列表，他的内容一般是不可变更的


序列的基本操作
    成员关系： `in`, `not in`
    连接： `+`
    重复： `*`
    切片： `[start_index:sum]`
我们还可以使用`len(...)`来计算序列的长度(个数)



filter函数：
    `filter(lambda x: x ...条件..., 放入过滤的序列)`
    fileter处理过的对象会变成: filter object
    `list=[1,2,3,4,5,6]; list(filter(lambda x:x>2, list))`
for控制流：
```python
for 迭代变量 in 可迭代对象:
    代码块
```
while条件控制流:
```python
while 条件:
    语句块
```
if条件控制流：
```python
if 条件:
    语句块
elif 条件
    语句块
else:
    语句块
```


字典其实就是哈希表：
    `{key:value}`
    字典增加值直接是填写就行
        `dict["name"]=Jane`

列表推导式， 字典推导式 python 独有啊
```python
alist=[]
for i in range(1:10):
    if (i % 2 == 0):
        alist.append(i*i)
print(alist)

# 可简洁为
alist=[i*i for i in range(1:10) if i%2 == 0]
```

所以前面的例子可以综合为：
```
shengxiao = '豬鼠牛虎兔龍蛇馬羊猴雞狗'
constellations = ("水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座",
                  "天秤座", "天蝎座", "射手座", "摩羯座")
days = ((1, 20), (2, 19), (3, 21), (4, 20), (5, 21), (6, 22), (7, 23), (8, 23),
        (9, 23), (10, 24), (11, 23), (12, 22))

# 使用字典来存储生肖和星座的统计情况
shengxiaoSum = {}
for i in shengxiao:
    shengxiaoSum[i] = 0
constellationSum = {i: 0 for i in constellations} # 推导式

# 假设输入次数为3次
num = 0
while num < 3:
    year = int(input("请输入年份: ")) # 因为input而来的变量值类型为字符
    month = int(input("请输入月份: "))
    day = int(input("请输入日份: "))
    standard1 = 2019
    standard2 = (month, day)

    result1 = (year - standard1) % 12
    print("你的生肖是: ", shengxiao[result1])

    n = 0
    while days[n] < standard2:
        if month == 12 and day > 22:
            break
        n += 1
    if days[n] == standard2:
        result2 = n
        print("你的星座是: %s" % constellations[result2])
    else:
        result2 = n-1
        print("你的星座是: ", constellations[result2])

    shengxiaoSum[shengxiao[result1]] += 1
    constellationSum[constellations[result2]] += 1
    num += 1

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx结果如下xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
for key in shengxiaoSum.keys():
    print("生肖%s 有%d个" % (key, shengxiaoSum[key])) # %s 为字符的占位符， 而%d为整数的占位符
for key in constellationSum.keys():
    print("星座%s 有%d个" % (key, constellationSum[key]))
```



文件的内建函数和方法：
    open() 打开文件  # 与其说打开文件，不如说是获取文件然后把它赋给变量以便操作
    read() 读取 
    readline() 读取一行
    readlines() 逐行读取
    seek() 文件内移动
    write() 输入
    close() 关闭文件
```python
# 无论怎样处理都要必须有两个： `open()` 和 `close()`
file1 = open("name.txt", "w")
file1.write("Janemon")
file1.close()

file2 = open("name.txt", "w")  # 必须打开可写权限才能写入
file2.write("Harray")  # 覆盖了前面的内容了
file2.close()

file3 = open("name.txt", "a")  # 不覆盖，在后面添加
file3.write("Jane")
file3.close()

file4 = open("name.txt")
for line in file4.readlines():
    print(line)

file5 = open("name.txt")
print("当前指针的位置: %s" % file5.tell())  # 如果使用%s等等， 那么就必须不在使用逗号而使用%来隔开
file5.read(2)  # 默认是读取文件所有内容，现在是设置为读取两个字符
print("当前指针的位置: %s" % file5.tell())
file5.seek(5, 0)  # 第一个参数是偏移量，第二个参数是标识偏移的方式：0 是开头，1 是相对位置， 2 是结尾
print("当前指针的位置: %s" % file5.tell())
file5.seek(0, 0)
print("当前指针的位置: %s" % file5.tell())
```



墨菲定理： 会出错的地方一定会出错，不论概率有多么少
所以我们必须对错误有一个检查和处理，那么Python的方法是：
错误不等于异常：
    异常是在出现错误时采用正常控制流以外的动作
    异常处理一般流程是：检测到错误，“引发”异常，对异常进行捕获处理的操作
```python
try:
    监控的代码
except Exception[, reason]:
    处理代码
finally:
    无论异常是否发生都会执行

例子：
try:
    i = j
except Exception as e:
    print("检测到错误： %s" % e)
finally:
    print("continue...")
```



案例：统计统计小说中的内容
```python
import re


def findName(hero):
    with open("../Test/book.txt") as book:
        book = book.read().replace("\n", "")  # 这里的read()是必须的, 而且处理成一行文本，比较好分析
        name_sum = len(re.findall(hero, book))  # 这里处理后的对象不能直接使用，需要转换
        print("主角 %s 在书中出现了 %s 次" % (hero, name_sum))
    return name_sum


name_statistics = {}
with open("../Test/name.txt") as f_name:
    # 第一步打开获取(必须)，第二步是读取(处理文本时). 文本好像是自动加上分隔符号的，尽管edit时候是不显示的. read()之后变成了str
    f_name = f_name.read().replace("\n", "").split("|")
    for name in f_name:
        name_sum = findName(name)
        name_statistics[name] = name_sum

# 把排序时候的key替换数字，这样才能得出按数字排序的结果
reverse_list = sorted(name_statistics.items(), key=lambda item: item[1], reverse=True)
print("==============次数表如下： ==============")
for item in reverse_list:
    print(item)
```

函数：
```
def function_name():
    code_chunk
    return
```
关键字参数: 除了可以不按顺序来进行输入还能明确他的作用
    其实JS里面也有类似的，我们叫做默认参数
```python
def keyParam(a,b,c):
    print("a= %s", %a)
    print("b= %s", %b)
    print("c= %s", %c)
keyParm(1,2,3)
keyParm(1,c=2,b=3)
```
可变长参数： 就是参数的个数可以灵活
```
def dynamic_parm(must, *other):
    print(must)
    print(other)
    print(1 + len(other))


dynamic_parm("chen", 1995, "0518")
```



在函数内部使用外部的全局变量，我们可以在变量前面加一个`global`

迭代器和生成器(带有yield的迭代器, 其实yield就是产生的意思,所以他才叫做生成器)
    包头不包尾，步长
```python
list = [1, 2, 3]
it = iter(list)
print(next(it)) # 和JS的迭代器用法一样但是写法就不同了,这个更直接方便
print(next(it))
print(next(it))
print(next(it))
```



一些简单的计算其实不用定义函数，可以使用lambda表达式
`lambda(params): return_exe_code`



内建函数：
    filter()
    map()
    reduce()
    zip()
```python
# map
lt = [1, 2, 3]
lt2 = map(lambda x: x**2, lt)  # 这个是乘方
print(type(lt2))
lt3 = list(lt2)
print(lt3)

# reduce
from functools import reduce  # 这个是必须得有的，真是每种语言都有他自己的毛病啊
result = reduce(lambda x, y: x + y, [1, 2, 3], 8)
print(result)

# 其实zip就是矩阵置换
dicta = {"a":"aa", "b":"bb"}
dictb = zip(dicta.values(), dicta.keys())
print(dictb)

a = [1, 2, 3]
b = [4, 5, 6]
for i  in zip(lista, listb):
    print(i)



```



闭包
    闭包：使用了函数传递，可以减少函数调用,使代码更抽象和优雅

装饰器：用来“装饰”函数，主要是对于函数的辅助功能.他也是一个函数，但是具有语法糖而已, 所以也是可以函数使用的功能的，我们可以像闭包一样做很多东西。
```python
import time

def timmer(func):
    def wrap():
        start = time.time()
        func()
        stop = time.time()
        print("The process costs %s 秒" % (stop - start))

    return wrap

def sp():
    time.sleep(3)

sp = timmer(sp)
sp()


# 用 @ 那么其实这就是省略掉了 最后一步的赋值过程
def timmer(func):
    def wrap():
        start = time.time()
        func()
        stop = time.time()
        print("The process costs %s 秒" % (stop - start))

    return wrap

@timmer
def sp():
    time.sleep(3)

sp()


# 参数一个一个传递下去，接着一个一个return到核心
def tips(agrv):
    def wraper(func):
        def counter(a, b):
            print("The running model is %s, and the running function is %s" %
                  (agrv, func.__name__))
            func(a, b)

        return counter

    return wraper

@tips("加法")
def add(a, b):
    print("The result is %d" % (a + b))

@tips("减法")
def sub(a, b):
    print("The result is %d" % (a - b))

add(1, 2)
sub(2, 1)
```



上下文管理器(with):
    简洁try的调错
```
file= open("name.txt")
try:
    for i in file:
        print(i)
except exception as e:
    print("The error is %s" % e)
finally:
    file.close()

with open("name.txt") as f:  # 检测语句如何使用
    for i in f:
        print(i)
```
需要知道with只是一个try的简洁版，所以包围的代码块该如何组织就如何组织



模块，其实也就是相对于C语言的库，JavaScript的包，库，模块.
    作用： 一个可供重复使用的一个功能集合
    使用如下
```python
1 import module_name
2 import module_name as petname  # 不过这个引用他的工具的时候需要带一个点
3 from module_name as petname  # 这个不像上面那个，但是可能会覆盖原本的名字，所以不建议

# my_module.py
def print_me():
    print("Hi, I'm Janemon")

# other.py
import my_module.py
my_module.print_me()

```



面向对象编程
    类，其实只是一个特征归纳而已, 一旦有了归纳和抽象概括，那么就具有不错的可扩展性，而不像面向过程的思考方式，更针对某个问题而不具有高度拓展性。
```python
# 类的首字母需要大写
# __init__ 是类的特殊方法，在类实例化的时候会自动执行
# self 代表实例化的本身, 不像 js中的this那样杂乱不明 （必须）
# 每个方法都需要self这个参数，以便使用实例 （必须）
class Player():
    def __init__(self, name, hp):
        self.__name = name  # 加上双下划线代表是使用属性，那么在外部直接通过属性来改属性值就不行了
        self.hp = hp

    def print_role(self):
        print("%s: %s" % (self.name, self.hp))

user1 = Player("janemon", 100)
user2 = Player("jack", 90)
user1.print_role()
user2.print_role()
```

   类的继承及多态
```python
# 如果子类要复用父类的属性，为了避免性能的损耗，我们可以使用： super().__init__(...)
# 判断类的类型，也是用type， 如果想辨别每个对象是否是某个类，我们可以使用 isinstance(obj, type)
# 继承就是沿用父类的属性方法，而多态就是扩展父类的属性和方法，以增加子类的丰富性
class Monster():
    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print("移动到某个位置")

class CommonM(Monster):
    def __init__(self, hp=80):
        super().__init__(hp)

class BossM(Monster):
    def __init__(self, hp=1000):
        super().__init__(hp)

    def skill(self):
        print("I am the best!!")

origin = Monster()
print(origin.hp)
origin.run()

commoner = CommonM()
print(commoner.hp)
commoner.run()

boss = BossM()
print(boss.hp)
boss.skill()

print("origin 的类型: %s" % type(origin))
print("commoner的类型: %s" % type(commoner))
print("boss的类型: %s" % type(boss))
print(isinstance(origin, Monster))
print(isinstance(origin, CommonM))
```



多线程（并发）编程
```python
# 主要的多线程工具库是 threading
# 将函数纳入多线程中，需要 threading.Thread(target=function, args=...)

import threading
import time
from threading import current_thread  # 查看当前线程

print(current_thread().getName(), "start")  # 注意这里不是 current_thread.getName()

def func(arg1, arg2):
    print(current_thread().getName(), "start")
    time.sleep(2)
    print("%s, %s" % (arg1, arg2))
    print(current_thread().getName(), "stop")

for i in range(1, 6, 1):
    thread = threading.Thread(target=func, args=(i, i + 1))
    thread.start()  # 这代表启动多线程

print(current_thread().getName(), "stop")


# 对象写法
print(current_thread().getName(), "start")
class Myfunc(threading.Thread):
    def run(self):
        print(current_thread().getName(), "start")
        time.sleep(2)
        print(current_thread().getName(), "stop")

for i in range(1, 6, 1):
    thread = Myfunc()
    thread.start()

print(current_thread().getName(), "stop")
```


生产者与消费者问题
    其实就是数据写入和读出的问题
```python
import queque
q = queque.Queue(num)  # 生成队列
q.put()  # 放
q.get()  # 取
```

```python
from threading import Thread, current_thread
import time
import random
from queue import Queue

que = Queue(5)  # 产生了5个线程

class Productor(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global que
        while True:
            n = random.choice(nums)
            que.put(n)  # 往该队列放进数据
            print("线程： %s 产生了 %s " % (name, n))
            t = random.randint(1, 3)
            time.sleep(t)
            print("线程： %s 休眠了 %s秒 " % (name, t))

class Consumer(Thread):
    def run(self):
        name = current_thread().getName()
        global que
        while True:
            n = que.get()  # 从队列中取出数据
            que.task_done()  # 在队列中取出数据后，发出信号进行一个确定
            print("线程： %s 消费了 %s " % (name, n))
            t = random.randint(1, 3)  # 从1到3中随机取出一个数
            time.sleep(t)
            print("线程： %s 休眠了 %s秒 " % (name, t))

g1 = Productor(name="g1") # name = "..." 是必须的
g2 = Productor(name="g2")
c1 = Consumer(name="c1")
c2 = Consumer(name="c2")
g1.start()
# g2.start()
c1.start()
c2.start()
```



标准库
    文字处理： re
    日期处理： time, datetime
    数字处理:  math, random
    文件和目录访问： pathlib, os.path
    数据压缩和归档： tarfile
    操作系统： os, logging, argparse
    多线程： threading，queue
    网络数据处理： base64, json, urllib
    结构化标记处理工具： html, xml
    开发工具： unitest
    调试工具： timeit
    软件发布： venv
    运行服务： __main__

re(regular express operations)
    正则表达式操作
```python
import re
pattern = re.compile("...")
pattern.match(str)
# . 代表任意字符
# ^ 代表开始
# $ 代表结束
# * 代表前面字符出现零次或者多次
# + 代表前面字符出现一次或者多次
# ? 代表前面的字符出现零次或者一次
# {m} 代表前面的字符出现指定次数
# {m, n} 代表前面的字符出现m到n次
# [] 表示出现里面的一个或多个符号： [123abc]
# () 表示分组
```

文字，时间日期
```python
import re
import time
import datetime


# 模式前面的 r 代表使用 row， 不对特殊字符(\n...)进行转义
# pattern = re.compile(r'\d-\d-\d')
p = re.compile(r'(\d+)-(\d+)-(\d+)')
result = p.match('2018-5-11')
print(type(result))
print(result)
print(type(str(result)))

print(p.match('2018-5-11').group())
print(p.match('2018-5-11').groups())
print(p.match('2018-5-11').group(1))

year, month, day = p.match("2018-5-11").groups()
print(year, month, day)


# 这是在搜索功能，并不是完全匹配
result2 = p.search("aa2015-5-11")
print(result2)


# 这是替换功能
phoneNumber = "123-456-78 # 这是备注信息"
result3 = re.sub(r"#.*$", "", phoneNumber)  # python 的数据源喜欢放在最右边
print(result3)
result4 = re.sub(r"\D", "", result3)
print(result4)


print(time.time())
print(time.localtime())
# Y: 2019, y: 19, 小时，分钟， 秒 分别是： %H, %M, %S
print(time.strftime('%Y-%m-%d %H:%M:%S'))

now = datetime.datetime.now()  # 特殊的写法
print(now)
new = datetime.timedelta(minutes=10)  # 时间偏移量： timedelta(...)
print(datetime.datetime.now()+new)  # 直接相加
current = datetime.datetime(2008,8,8)  # 设定一个日期
new2 = datetime.timedelta(days=10)
print(current)
print(current+new2)
```

文件夹操作
    path 和 pathlib 的大部分内容相似，但是pathlib的用法较繁杂，不过pathlib可以创建新目录,而path不能

```python
form os import path
print(path.abspath(".."))
print(path.abspath("."))
print(path.exists("/users"))
print(path.isdir("./note.md"))
path.join("...", "...")

from pathlib import Path
p = Path(".")  # 使用前必须先解析路径
print(p.resolve())
print(p.is_dir())
pt = Path("/tmp/chenn/a/b")
Path.mkdir(pt,parents=True)  # 必须得有parents才有多级目录
```



机器学习，人工智能
    通用步骤： 数据采集，数据的预处理， 数据的清洗(过滤)， 数据的建模，数据的测试

机器学习库: numpy库, 用于高性能科学计算和数据分析, 是常用的高级数据分析库的 "基础包"
    这个库不是Python的内建库，所以我们需要使用下载:`pip install numpy`
```python
import numpy as np

arr1 = np.array([1, 2, 3])  # 这里和Python的Array不同，是经过优化的
arr2 = np.array([1.1, 2.2, 3.3])
arr3 = np.arange(10)
arr3[3:6] = 3
arr3_slice = arr3[3:6].copy() # 这个可以看成是切片
arr3_slice[:] = 1
parr1 = [1, 2, 3]
parr2 = [1.1, 2.2, 3.3]

print(arr1)
print(arr1.dtype)  # 显示的 int64 而不是 list
print(arr2)
print(arr2.dtype)
print(arr1 + arr2)  # 这是相应位置进行累加
print(arr3)
print(arr3_slice)
print(arr2 * 10)  # 这里显示在 numpy 中是可以直接对数组进行操作
print(parr1 + parr2)  # 这是进行连接


# 对矩阵的操作
data = [[1, 2, 3], [4, 5, 6]]
matrix1 = np.array(data) # 对列表的转换
print(matrix1)
print(matrix1.dtype)

matrix2 = np.zeros((3,5))  # 三行五列
matrix3 = np.ones((4,6))
matrix4 = np.empty((2, 3, 4))  # 矩阵中间两个矩阵，然后都是三行四列的形式
print(matrix2)
print(matrix3)
print(matrix4)
```


数据预处理和清洗常用库(也就是删除和填补)
    安装： `pip install pandas`
```python
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from numpy import nan as NA

# 以下的是一维数组(忽略掉索引）多行两列带有索引(索引是其中一列)的数组
arr = Series([11, 22, 33])
print(arr)
print("arr_index: %s" %(arr.index))
print("arr_value: %s" %(arr.values))
print("arr_dtype: %s" %(arr.dtype))  # int64
print("arr_type: %s" %(type(arr)))  # Series

# 索引可以改变
arr2 = Series(["Beijing", "Shangehai", "Guangzhou"], index=["b", "s", "G"])
print(arr2)
print("arr2_dtype: %s" %(arr2.dtype))  # Object, 这是根据内容项来改变的, 注意：一旦其中一项不是数字，都不会是 数字类型
print("arr2_type: %s" %(type(arr2)))  # Series

# 可以重新排序(手动)和填补空置(原来属于那个索引的还是原来的值, 填补的是没有值的索引)
re_arr = Series([111, 222, 333], index=["e", "f", "a"])
print(re_arr)
re_arr = re_arr.reindex(["a", "e", "f", "d"], fill_value=0)
print("re_arr is \n%s" %(re_arr))

rr_arr = Series(["blue", "yellow", "red"], index=[1, 3, 4])
rr_arr = rr_arr.reindex(range(6), method="bfill")  # 代表拿后面的来填充
print("rr_arr is \n%s" %(rr_arr))

# 把字典改成 Pandas 中的多行两列数组
dataD = {"Beijing": 1100, "Shanghai": 2100, "Guangzhou": 3100}
arr3 = Series(dataD)
print("arr3 is:\n%s" %(arr3))
arr3.index = ['bj', 'sh', 'gz']
print("new arr3 is:\n%s" %(arr3))

# NA 占了这个索引，但是之后可以把这个索引拿出来
arr4 = Series([1, NA, 2])
none_arr4 = arr4.dropna()
print("none_arr4 is \n%s" %(none_arr4))
fill_arr4 = arr4.fillna(0)
print("fill_arr4 is \n%s" %(fill_arr4))

# 二级索引
arr5 = Series(np.random.randn(10), index=[["a", "a", "a", "b", "b", "b", "c", "c", "d", "d"], [1, 2, 3, 1, 2, 3, 1, 2, 1, 2]])
print("arr5 is \n%s" %(arr5))
print("arr5 is \n%s" %(arr5["b":"c"]))


# DataFrame 是多维数组, 更像是电子表格, 依旧带有索引
# 内容项个数一定要对上
dataD2 = {"Year": [2015, 2016, 2017, 2018],
          "City": ["Beijing", "Shanghai", "Guangzhou", "Shengzhou"],
          "Pop": [1.1, 2.2, 3.3, 4.4]}
frame1 = DataFrame(dataD2)
print("frame1 is: \n%s" %(frame1))
frame2 = DataFrame(dataD2, columns=["Pop", "City", "Year"])
print("frame2 is: \n%s" %(frame2))
# 可以直接新增
frame2["New"] = "new add"
frame2["Cap"] = frame2.City == "Beijing"
print("new frame2 is \n%s" %(frame2))

dataD3 = {"Beijing": [11, 22],
          "Shanghai": [33, 66]}
frame3 = DataFrame(dataD3)
# 转置, 就是把“标题”互换
new_frm3 = frame3.T
print("frame3 is:\n%s" %(frame3))
print("new_frm3 is:\n%s" %(new_frm3))
```


绘图库(把数据绘制成图，更加直观便于人观看)
    安装：`pip install matplotlib`
    dpi 是绘图精度，越高越准确
    seaborn 是更好的描述散点图的库： `pip3 install seaborn`

机器学习的自动和分类需要的算法和数学支持: tensorflow 库(著名)
    安装: `pip install tensorflow`



网络库：
    主要有三种：urllib(http)(内建), requests(http), BeautifulSoup(xml格式处理`pip3 install bs4，lxml`)
```python
from urllib import as request
url = "www.baidu.com"
response = request.urlopen(url, timeout=1)
response = response.read().decode("utf-8")
print(response)
```
    `httpbin.org 是测试的一个网站`

    有时网站为了防止用户恶意获取数据，所以我们用浏览器和其他工具获取的数据用的http头是不一样的. 所以我们可以头部伪装：
```python
from urllib import request, parse

url = "http://httpbin.org/post"  # 这是个模拟请求的测试网站

headers = {
    ....
    这是伪装的头部信息
}

data = {
    ...
}

data = bytes(parse.urlencode(data), encoding="utf-8")  # 字典形式的数据需要经过字节处理
new_url= request.Request(url=url, data=data, headers=headers, method="post")
response = request.urlopen(new_url)
print(response.read().decode("utf-8"))
```
```python
# 伪装请求头这个库比较好
from fake_useragent import UserAgent
import requests


ua = UserAgent()
url = "https://www.baidu.com"
headers = {"User-Agent": ua.random}

response = requests.get(url=url, headers=headers)

print(response.text)
print(response.status_code)
print(response.headers)


```


    urllib库有时候太过繁琐了，所以一般我们使用 requests 库
```python
import requests
url = "http://httpbin.org/post"
data = {"key":"value", "abc":"xyz"}
response =requests.post(url, data)
print(response.text)
print(response.json())
```
```python
from bs4 import BeautifulSoup as bys

content = requests.get("http://www.cnu.cc/discoveryPage/hot-人像").text
# print(content)
soup = bys(content, 'lxml')  # 解析之后才能被使用
print(soup.prettify())
print("webpage_title %s" %(soup.title.string))
print("all a %s" %(soup.find_all('a')))

```

爬虫学习
```python
import requests
import re

content = requests.get("http://www.cnu.cc/discoveryPage/hot-人像").text
print(content)


pattern = re.compile(r'<img src="(.*?)".*alt="(.*?)">')  # 这里是关键
results = re.findall(pattern, content)
print(results)
arr = {}
for result in results:
    url, name = result
    print(url, re.sub("\s", "", name))
    arr[name] = url

for link in arr.values():
    print(link)


import requests
import re
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bys
from threading import Thread

ua = UserAgent()
headers = {"User-Agent": ua.random}

# dict = {}
# def get_img(url):
    # response = requests.get(url, headers).text
    # soup = bys(response, "lxml")
    # for img in soup.find_all("a", class_="thumbnail"):
            # # print(img)
            # for item in img.find_all("img"):
                # name = item.get("alt")
                # dict[name] = item.get("src")

# for i in range(1, 6, 1):
    # url = "http://www.cnu.cc/discoveryPage/hot-人像?page=" + str(i)
    # get_img(url)

# print(dict)

dict = {}
class GetImg(Thread):
    def run(self):
        response = requests.get(url, headers).text
        soup = bys(response, "lxml")
        for img in soup.find_all("a", class_="thumbnail"):
            for item in img.find_all("img"):
                name = item.get("alt")
                dict[name] = item.get("src")


for i in range(1, 6, 1):
    url = "http://www.cnu.cc/discoveryPage/hot-人像?page=" + str(i)
    run = GetImg()
    run.start()
    run.join()  # 判断线程结束

print(dict)

```
反爬虫
    这是一个爬失败的例子
```paython
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup as bys


ua = UserAgent()
url = "https://www.infoq.cn/"
# headers = {"User-Agent": ua.random}
headers ={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
response.encoding = "utf-8"
soup = bys(response.text, "lxml")
print(soup)


def get_title(soup):
    for box in soup.find_all("body"):
        print(box)
        print(headers)

get_title(soup)
```
