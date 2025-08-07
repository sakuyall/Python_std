# function_note4-8/5/25-----------------------------------------------------------------------
# //lambda表达式 匿名函数----------------------------------------------------------------------
def squarex(x):
    return x ** 2
squarex(3)
# |
# | 用lambda表达式写法
# V
squarey = lambda y : y ** 2   # 这个东西是函数的引用(一长串)，调用加()
squarey(3)

y = [lambda z : z * z,2,3]    # 将其作为元素放入，实际过程不建议这么写
y[0](y[1])                    # 返回4

mapped = map(lambda x : ord(x) + 10,"hello")   # 序列内每个元素转为Unicode并加10返回
print(mapped)

# //生成器 函数yeild表达式----------------------------------------------------------------------
def counter():
    i = 0
    while i <= 5:
        yield i
        i += 1
counter()                     # 返回<generator object counter at 0x000001E1A3772B90>生成器对象
                              # 属于一种特殊的迭代器，在每次调用中提供一个数据
                              # 在函数调用中执行完yield后，i+1-->yield-->i+1-->yield
                              # 而return是每次都从头开始嘛
for i in counter():           # for语句从可迭代对象中每次获取一个数据
    print(i)                  # 返回0 1 2 3 4 5

# 而其他可迭代对象是一个容器，存储着已准备好的所有数据
# 与列表元组等区别在于，生成器每次只提供一个数据，现用现生成，不走回头路且支持next函数，比如：
c = counter()
next(c)                       # 使其输出下一个内容
# 正因如此它不支持随机访问的下标索引方式，列表有推导式而元组没有，把[]替换为()后实际上叫做生成器表达式

# //递归 recursion 函数调用自身的过程-------------------------------------------------------------
def funC(i):
    if i > 0:
        print("已调用")
        i -= 1
        funC(i)
funC(10)                      # 加入合适条件使递归在恰当时刻回归，重点为设定结束条件

# 案例0 阶乘
def jie_cheng(num):
    if num == 1:
        return 1
    else:
        return num * jie_cheng(num - 1)
    
print(jie_cheng(5))

# 案例1 斐波那契数列
def fib(i):
    if i == 1 or i == 2:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)
    
print(fib(6))

# //难 汉诺塔-----------------------------------------------------------------------------------
# 以n=3为例，从左到右分别为ABC柱，最下层记作 地板，地板以上整体记作 上边部分
def hanoi(n,x,y,z):
    if n == 1:                          # 返回内容
        print(x,"-->",z)                # A --> C        1
    else:                               # A --> B        2
        hanoi(n - 1,x,z,y)              # C --> B        3
        print(x,"-->",z)                # A --> C        4
        hanoi(n - 1,y,x,z)              # B --> A        5
                                        # B --> C        6
hanoi(3,"A","B","C")                    # A --> C        7

# 当n为1时，地板从A移动到C
# 当n为2时，上边部分移到B  地板移到C  上边部分移到C
# 当n为3时，上边部分移到B  地板移到C  上边部分移到C  向下细分为：
#                |           |           |
#                V           |           V
#         BC调换时n=2情况     |     AB调换时n=2情况
#                |           |           |
#                V           V           V
#               123          4          567