# set_note-7/12/25--------------------------------------------------
{"hello","大象",123}
{s for s in "hello"}     # 集合的形式类似于字典，没有冒号,但集合是 无序的
s = set("hello")         # 正因为是无序的，因此无法使用下标访问
"h" in s                 # 可判断是否存在元素
for each in s:
    print(each)

set([1,1,2,3,5])         # 集合具有唯一性，因此可以去除重复元素
s = [1,1,2,3,5]
len(s) = len(set(s))     # 通过集合来判断源列表是否具有重复元素

t = s.copy()                    # 浅拷贝
s.isdisjoint(set("hallow"))     # 判断两个集合是否毫不相干（没有交集）
s.issubset(set("hello world"))  # 判断s是否为另一集合子集
s < set("***")    # 真子集
s <= set("***")
s.issuperset(set("he"))         # 判断s是否为另一集合超集
s > set("***")    # 真超集
s >= set("***")
s.unin({1,2,3})                 # 并集
s | {1,2,3} | set("***")
s.intersection(set("he"))       # 交集
s & set("he")
s.difference(set("he"))         # 差集
s - set("he")
# 以上均支持多参数，而且不加set()也可以
s.symmetric_difference(set("ha")) # 对称差集，去除相同元素后，剩余元素集合
s ^ set("ha")
# 注意，使用运算符时左右两侧都是集合，基本方法则可以用可迭代对象

# 集合细分为可变与不可变
s = set("hello")
s.update([1,1],"23")          # 可以更新多个参数(并集)
t = frozenset("hello")
t.update([1,1],"23")          # 不可update

s.intersection_update("2")    # 交集
s.difference_update("l")      # 差集
s.symmetric_difference_update("h")  # 对称差集

s.add("45")                   # 单独添加元素，add方法传入整个字符串作为元素
s.remove("45")                # 删除元素，若无则抛出异常
s.discard("45")               # 不会抛出异常
s.pop()                       # 随机弹出一个元素
s.clear()                     # 清空集合

# 集合的元素与字典的键都要求 可哈希
hash(1.0)                     # 通过此方法求得哈希值
hash("hello")
hash([1,2,3])                 # 可变内容，无法求哈希值
hash((1,2,3))                 # 不变内容，可计算
u = dict({[1,2,3]:"666"})     # 所以这个会报错
u = dict({"666":[1,2,3]})     # 而这个键不会，集合元素也是同样的道理
# set不可嵌套，frozenset就可嵌套
# 集合的查找效率要高于列表