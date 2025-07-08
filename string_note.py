# --1/27/25&7/7-8/25-string_note------------------------------------------
x = "12321"
"palindrome number true" if x == x[::-1] else "false"

# another x.etc menifested in 46 ways in pydoc. 
# a typical example is x.center x.ljust x.rjust
# x = "hello world"---->and x.center(15,"6") == "66hello world66"

y = "上海自来水来自海上"    # 字符串查找
y.count("海")
y.count("海",0,5)         # Scan range:from the first to the fifth

y.find("海")              # Find the location,followings are from l2r & r2l
y.rfind("海")             # No object will output -1
y.index("龟")             # Instead of "find",output error

"婴儿应尽早进行追视训练".replace("应","不应") # 字符串替换
# 使用过程中应尽量避免空格与制表符混用。
code = """    print("hello")
    print("world")"""
new_code = code.expandtabs(4)  # 将制表符替换为长度为4的空格（不过这边默认制表符是四个空格的）
print(new_code)

table = str.maketrans("abcdefg","1234567")  # 建立表格作为转换规则(据说以后有其他用途)
"hello world".translate(table)              # 字符一样的对应转换（注意大小写）

table = str.maketrans("abcdefg","1234567","helo")
"hello world".translate(table)              
# 第三个参数用于忽略指定字符,使其不参与替换（helo字母当作没有，汉字同理）

# 字符串判断
z = "这是hello world"
z.startswith("这")       # 判断是否以对应子字符串开头，是则返回True
z.startswith("这",1,4)   # 这代表从1位置开始索引，即从“是”开始找到第一个“l”
# 应注意，大多数下标索引都是包头不包尾，从下标1开始到下标4结束，不包括下标4
z.endswith("e",0,4)      # 返回为True，表明索引了“这是he”，以e结尾
# 也可以理解为从下标1开始往后找4个字符
z.endswith("d")
z.endswith("world")      # 这两句返回的都是True，推测为从后往前的完整字符都可以
z.endswith("o world")    # 的确是这样

if z.startswith(("这是","那是","也是")):   # 将索引内容改为元组进行判断
    print("都是Hello world")
else:
    print("并非Hello world")

a = "i Love Python"
a.istitle()                # 用于判断字符串首字母是否全为大写
a.isupper()                # 用于判断全部字母是否都为大写,小写用islower
a.upper().isupper()        # 运算规则为从左往右，所以输出True
a.isalpha()                # 判断是否全为字母，这里有空格，所以返回False
a.isspace()                # 判断是否为空白字符串，包括制表符，空格，转义字符/n等
a.isprintable()            # 判断是否为可打印字符，转义字符不可打印
a.isidentifier()           # 判断是否为标识符（不可以数字开头）
# 写点不一样的
import keyword             # 导入keyword模块
keyword.iskeyword("if")    # 调用iskeyword函数判断目标是否为保留标识符，返回True
