# sequence_note-7/9/25--------------------------------------------
# 列表，元组，字符串统称为序列，根据是否可更改分为可变与不变序列
[1,2,3] + [4,5,6]    # 拼接
(1,2,3) + (4,5,6)
"123" + "456"

[1,2,3] * 3          # 重复
(1,2,3) * 3          # 前两个的元素会自己分开，字符串写什么就是什么
"1,2,3" * 3
s = [1,2,3]
s *= 2
id(s)                # id保持不变，元组在变换后会变

x = "11"             # is和not is判断
y = "11"
x is y               # 返回True说明两者是同一个对象

x = [1,2,3]
y = [1,2,3]
x is y               # 返回False说明两者虽然列表一样，但不是同一个对象

"o" in "hello"       # in和not in判断包含关系
# 返回True说明序列中包含元素

x = "hello"
y = [1,2,3,4,5]
del x,y              # 删除指定对象
del y[1:4]           # 删除y中1号到4号（左闭右开所以是123号）
y[1:4] = []          # 也可以用这种方式写，将空列表赋予给切片区域
del y[::2]           # 从0号开始步长为2进行删除，输出为[2，4]
y[::2] = []          # 这个用切片做不到
y.clear()            # 清空列表
del y[:]             # 类似地可以这么写

# 与序列相关的一些函数,面向可迭代对象
# 转换函数
list("hello")        # 分别转换为列表，元组，字符串
tuple("hello")
str("hello")         #  输入什么转换为什么字符串

# 最大值与最小值
a = [1,1,2,3,5]
min(a)
max(a)
# 若输入为字符串，则比较字符串编码值，规律如下:A < Z < a < z
b = []
min(b,default="输入戳啦")   # 当传入为空迭代对象，可加入报错提醒

# len函数
len(range(2 ** 100))       # 返回报错
# 这是由于len函数直接读取C语言中该对象长度，而超过某一数值时则会溢出
# 该数值对于32位平台位2**31-1，64位则为2**63-1

# 求和函数，起始基值
sum(a,start=100)           # python3.7以前直接写100，不加start

# 排序函数sorted可用于任何类型可迭代参数
sorted(a)                  # 从小到大排序，源列表不受影响
a.sort()                   # 这个会改变源列表
sorted(a,reverse=True)     # 反向
c = ["Saber","Lancer","Archer","Rider","Caster","Assassin","Berserker"]
sorted(c)                  # 默认字母排序
sorted(c,key=len)          # 以长度排序

reversed(c)                # 返回一个迭代器(是可迭代对象)
list(reversed(c))          # 返回了c.reverse()的值
list(reversed(range(0,10)))# 和上边效果相同

d = (1,1,0)
all(d)                  # 是否所有元素都为True
any(d)                  # 是否有True

seasons = ["Spring","Summer","Fall","Winter"]
enumerate(seasons)      # 创建一个枚举对象
list(enumerate(seasons),10) # 从10开始依次加序号，不写默认从0开始

e = [1,2,3]
f = [4,5,]
zipped = zip(e,f)       # 一一对应组合,长度不对应部分不组合
list(zipped)

import itertools        # 解决上述问题可以采用此方法
i = itertools.zip_longest(e,f)
list(i)                 # 未对应部分填充会为None

mapped = map(ord,"hello")    # ord求出Unicode编码，后面为输入对象
list(mapped)                 # 输出了每一个字母的Unicode编码
# 再输入多个对象也可以,起到多重执行函数的作用
mapped1 = map(pow,[2,3,5],[2,2,2])
list(mapped1)
# 起到的效果与[pow(2,2),pow(3,2),pow(5,2)]相同
mapped2 = map(pow,[2,3,5],[2,2])
list(mapped2)                # 同样，长度不对应部分不组合

# 判断是否小写，两者对比输出
list(map(str.islower,"HEllo"))        # 输出判断结果True和False
list(filter(str.islower,"HEllo"))     # 过滤出True的对象

# 总结：zip进行一一组合，map执行函数输出结果，filter输出结果为真的源元素
# 迭代器(iterator)是一次性的，以上函数返回均为迭代器，需要list等转换函数还原
# 迭代器都是可迭代对象，有些函数在使用前需看文档得知其返回内容
# 可以通过iter函数把可迭代对象转为迭代器
g = [1,2,3]
h = iter(g)
type(g)           # 返回list，形式为列表
type(h)           # 返回list_iterator,形式为列表迭代器

next(h)           # 将迭代器内元素挨个提取出，全部提取完成后会输出 异常
next(h,"hollow")  # 通过加入后置参数解决以上问题以决定输出什么