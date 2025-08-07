# function_note3-8/4/25----------------------------------------------------------
# //装饰器-----------------------------------------------------------------------
def myfunc():
    print("正在调用myfync函数")

def report(f):           # 函数作为变量引用过来，为防止混淆定义些简单变量名
    print("准备调用函数")
    f()                  # 调用所引用函数
    print("调用函数完成")
report(myfunc)

# 案例0 测试函数运行时间
import time
def time_master(fu):
    print("开始运行程序")
    start = time.time()
    fu()                 # 调用所引函数，前后为获取的时间差
    end = time.time()
    print("时间测试结束")
    print(f"运行时间为{(end-start):.10f},打败了0.001%的同类函数")

def myfunc():            # 欲测试函数为防止运行过快可以先delay2秒
    time.sleep(2)
    print("hello world")

time_master(myfunc)

# 在与闭包结合后可以在不调用timemaster情况下运行出结果
import time
def time_master(fu):
    def call_func():
        print("开始运行程序")
        start = time.time()
        fu()                 # 调用所引函数，前后为获取的时间差
        end = time.time()
        print("时间测试结束")
        print(f"运行时间为{(end-start):.10f},打败了0.001%的同类函数")
    return call_func

def myfunc():
    time.sleep(2)
    print("hello world")

myfunc = time_master(myfunc)    # 注意前边的myfunc是变量名，后边为引用函数名，之前说的混淆就是这样
myfunc()

# 对于40-44行的语句可以有语法糖写法，改写为：
@time_master
def myfunc():
    time.sleep(2)
    print("hello world")        # 意在表示把myfunc函数作为参数塞入@装饰器外层中，并调用装饰器

# 案例1 多重装饰器
def add(func):
    def inner():
        x = func()
        return x + 1
    return inner

def square(func):
    def inner():
        x = func()
        return x * x
    return inner

def cube(func):
    def inner():
        x = func()
        return x * x * x
    return inner

@add
@square
@cube
def test():                # 装饰器的执行由近及远，先cube再square
    x = 2
    return x

print(test())              # 返回65

# 对案例0继续修饰
import time
def logger(msg):
    def time_master(fu):
        def call_func():
            print("开始运行程序")
            start = time.time()
            fu()                 # 调用所引函数，前后为获取的时间差
            end = time.time()
            print("时间测试结束")
            print(f"函数{msg}运行时间为{(end-start):.10f},打败了0.001%的同类函数")
        return call_func
    return time_master           # 不要忘记return

@logger(msg="myfunc")        # 在装饰器外再包一层，为其传送更多元素，参数直接写在里面
def myfunc():
    time.sleep(2)
    print("hello world")

@logger(msg="myfunc1")
def myfunc1():
    time.sleep(3)
    print("hello world")

# myfunc = logger(message="mycunc")(myfunc)  # 语法糖展开的写法
myfunc()
myfunc1()

# 总之是添加一次调用，多放进去一次参数