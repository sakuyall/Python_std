# figure_type_notes-1/3/25-------------------------------------------------------
import decimal
a = decimal.Decimal('0.1')                #实例化对象,精确打印浮点数
b = decimal.Decimal('0.2')
print(a + b)

x = 1 + 2j                                #复数表达
print(x.real)
complex(1 + 2j)

divmod(x,y)                                #返回地板除商与余数
abs()                                      #绝对值
pow(x,y)                                   #x的y次方,等同于‘x**y’

bull(250)                                  #布尔类型，仅有true&false，用于分支循环判断
bull('false') == true,bull(false) == false 
# 应区分字符串与空,等值于0才为false
# 如none,false,0，0.0,demical(0),fraction(0),空的序列与集合(){}[],set(),range()

# 总之，true可理解为1，false可理解为0，可用与and或or非not运算

# 短路原则：3 and 4 == 4，3 or 4 == 3，
# 如果第一个值直接确定结果就输出第一个结果，第二个直接不看，当第二个值决定结果时才输出第二个

# 运算符优先级not > and > or
