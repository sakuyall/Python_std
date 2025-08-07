# function_note2-8/4/25-------------------------------------------------
# //闭包函数--------------------------------------------
def funA():
    x = 880
    def funB():
            print(x)
    return funB  # 不带括号叫做函数的引用

print(funA())    # 返回<function funA.<locals>.funB at 0x000001CCA701EDD0>，类似于之前的迭代器
funA()()         # 这样就可以直接调用funB

funny = funA()   # 另一种方式
funny()

def power(exp):
      def exp_of(base):
            return base ** exp      # 幂运算
      return exp_of
square = power(2)           # power(2)--->base**2本体(类似于迭代器)
cube = power(3)             # square=base**2本体，base**2本体(base)----->base ** 2
square(2)                   # 所以square(2)---->2 ** 2，返回4
cube(2)                     # 返回8
# 实现了预设外部参数，自定义内部参数

# 案例
def outer():
    x = 0
    y = 0
    def inner(x1,y1):
        nonlocal x,y     # 使嵌套内部可更改外部
        x += x1
        y += y1
        print(f"当前坐标为{x1,y1}")
    return inner         # 返回的inner本体

move = outer()
move(1,1)                # 移动坐标

# 总结：
# 第一、利用嵌套函数的外层函数作用域及有记忆功能的特性，将数据保存在外层函数的参数或变量中
# 第二、将内层函数作为返回值返回，实现从外部间接调用内部函数