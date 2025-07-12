# -list_note_2-1/14/25-------------------------------------------
x = [[1,2,3],[4,5,6],[7,8,9]]
y = x.copy()                # shallow copy: y is a cite of x
y = x[:]                    # shallow copy: as the last one

import copy                 # deep copy: the real copy,but have a low efficiency
y = copy.deepcopy(x)        # do not change features follow by x

x = [1,2,3]
for i in range(len(x)):
    x[i] = 2 * x[i]
print(x)

x = [i * 2 for i in x]      # //List conprehension//
print(x)                    # [expression for target in iterable] <----

y = [i * 2 for i in "Hello"]
code = [ord(i) for i in "Hello"]
print(y)
print(code)

A = [[0] * 3] * 3    # false
A = [0] * 3
for i in range(3):
    A[i] = [0] * 3   
S = [[0] * 3 for i in range(3)]
even = [i for i in range(10) if i % 2 == 0]

words = ["great","Fantastic","excellent"]        #find abc
fwords = [w for w in words if w[0] == "F"]
print(fwords)

# [expression for target1 in iterable1
#             for target2 in iterable2
#             for target3 in iterable3]  <-------

matrix = [[1,2,3],[4,5,6],[7,8,9]]
flatten = [col for row in matrix for col in row]  # like||
flatten = []
for row in matrix:
    for col in row:
        flatten.append(col)

[x + y for x in "hello" for y in "hello"]     #Cartesian product
# _ as a temporary variable