# function_note1-7/14-19/25-------------------------------------------------
def myfunc():                         # 使用此方法定义
    pass       # pass为空语句，作为占位符
myfunc()       # 实现调用

def myfunc1(name,times):              # 定义带参数的函数
    for i in range(times):
        print(F"hello{name}")
myfunc1("world",3)                    # 调用时传入参数,name占位这种叫形参,"world"传入数值叫实参

def div(a,b):
    if b == 0:                        # 判断除数是否为0
        print("除数不能为0")
        return None                   # 返回None表示没有返回值,不写return也会返回none
    else:
        c = a / b
        return c                      # return返回值，调用时可以接收返回值
div(4,0)                              # 调用函数，传入实参

def myfunc2(s,vt,o):
    return "".join((o,vt,s))           # 字符串添加元素
myfunc2("我","吃","饭")                # 这种叫做位置参数，传入实参要按照顺序
myfunc2(o="饭",vt="吃",s="我")         # 这种则采用关键字参数，无需考虑顺序
                                       # 混合使用时，位置参数要放在关键字参数之前
def myfunc3(s,vt,o="饭"):
    return "".join((o,vt,s))
myfunc3("我","吃")                     # 未给参数o则使用默认值“饭”

# 在使用help()查看说明时，函数内会有/分割
# 这表明左侧应为位置参数，右侧位置参数和关键字参数都行
# 因此定义函数时也可加入此限制：

def abc(a,/,b,c):
    print(a,b,c)
abc(12,1,c=2)                          # 实现效果

def ABC(A,*,B,C):
    print(A,B,C)
ABC(A=1,B=2,C=3)                       # 而用*分割则表明左侧随意，右侧只能用关键字

print("我","吃","饭")                   # print就支持参数可多可少
def myfunc4(*args):                    # 定义为收集参数要加*
    print("有{}个参数。".format(len(args)))
    print("第二个参数是{}".format(args[1]))
    print(type(args))                  # <------其实是收集为一个元组打包
myfunc4("我","吃","饭")

def myfunc5(**kwargs):                 # **打包为字典
    print(kwargs)
myfunc5(a=1,b=2,c=3)

def myfunc6(a,*b,**c):
    print(a,b,c)
myfunc6(1,2,3,4,x=5,y=6)               # 混合输出为：1 (2, 3, 4) {'x': 5, 'y': 6}

help(str.format)                       # 可以看出S.format(*args, **kwargs) -> str

args = (1,2,3,4)
kwargs = {"a":1,"b":2,"c":3,"d":4}
def myfunc7(a,b,c,d):
    print(a,b,c,d)
myfunc7(args)                    # 返回需要四个参数
myfunc7(*args)                   # 实现作为整体解包
myfunc7(**kwargs)

x = 100
def myfunc():
    x = 200
    print(x)
myfunc()                    # 返回局部变量x
print(x)                    # 返回全局变量x
# 由于作用域不同，两者同时出现时是不同变量，id不同，全局变量作用优先
# 那么如何在函数内部修改全局变量
x = 300
def myfunc():
    global x                # 告诉python这是全局变量的x
    x = 400
    print(x)                # 为避免bug应少使用此方法

# 函数嵌套
def funA():
    x = 500
    def funB():
        nonlocal x           # 实现内部更改外部x值，与global类似
        x = 600              # 区别在于，global可用于定义新变量，而nonlocal只能作用于原有变量
        print("in funB,x=",x)
    funB()                   # 想使用内部函数定义完就要调用，在外部无法调用内部函数
    print("in funA,x=",x)    # 内部两个x互不干涉

# LEGB规则：local,enclosed,global,build-in.....简而言之本地优先
# 分别表示 局部作用域 嵌套函数外层函数作用域 全局作用域 内置作用域,优先级递减