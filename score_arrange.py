# score_arrange-1/4/25--------------------------------------------------
score = input("enter the score：")
score = int(score)

if 0 <= score < 60:
    print("F")
elif 60 <= score < 70:
    print("D")
elif 70 <= score < 80:
    print("C")
elif 80 <= score < 90:
    print("B")
elif 90 <= score < 100:
    print("A")
elif score == 100:
    print("S")
else:
    print("plese enter the correct format!")

# followed by another condition sentence like Adverbile Clause of Condition.
level = ("F" if 0 <= score <60 else
         "D" if 60 <= score < 70 else
         "C" if 70 <= score < 80 else
         "B" if 80 <= score < 90 else
         "A" if 90 <= score < 100 else            # it is else instead of elif!
         "S" if score == 100 else
         "plese enter the correct format!")
print(level)

a = 3
b = 2
small = 0
if a > b:
    small = b
else:
    small = a
print(small)

small = a if a < b else b   ## here is b , not small = b! 
print(small)