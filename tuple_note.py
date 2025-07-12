# --1/21/25-tuple_note------------------------------------------
# list[,],tuple(,) or tuple ,  
# tuple data cannot be modified, only support count & index
s = (1,2,3)
t = (4,5,6)
# as a result, w = s,t = ((1,2,3),(4,5,6))    #nesting

for i in w:
    for each in i:
        print(each)
r = (1,2,3,4,5)
[each * 2 for each in r]
x = ('helloworld',)        # to generate a certain tuple that include one feature

t = (123,"hello",3.14)       # packing & unpacking 
x,y,z = t                    # also available in list

s = [1,2,3]
t = [4,5,6]
w = (s,t)
w[0][0] = 0      # the feature in tuple can be replaceed when its feature is a list
