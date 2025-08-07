# function_note5-8/7/25-----------------------------------------------------------------------
# //函数文档 类型注释 内省
def exchange(dollar,rate=6.32):
    """
    这一部分是作为函数文档被保存起来的\n
    功能：汇率转换，美元 -> 人民币\n
    参数：
    - dollar 美元数量
    - rate 汇率，默认为 7.18 (2025-08-07)
    返回值：
    - 人民币的数量
    - 此时使用help(exchange)就可以访问这部分文档了,鼠标悬停于函数上方也可以显示。\n
    """
    return dollar * rate
exchange(20)

def times(s:list[int] = [1,2,3],n:int = 3) -> list:
    """
    变量后的冒号是作为类型注释以及默认值，表明这个参数建议使用该数据类型\n
    后边的箭头表示输出内容会是一个列表类型\n
    - 因为只是函数作者的 建议
    - 所以具体赋值依然是操作者说了算
    - 而且这部分内容并非给机器而是给人看的
    """
    return s * n
times("hello",5)

times.__name__        # 返回函数名
times.__annotations__ # 返回类型注释{'s': list[int], 'n': <class 'int'>, 'return': <class 'list'>}
times.__doc__         # 返回函数文档，用print可以解析出转义字符