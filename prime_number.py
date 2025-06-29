i = 0
while i < len("hello"):
    print("hello"[i])
    i += 1

# practiciable method _range(start,stop,step),from start to stop-1
sum = 0
for i in range(1001):     
    sum += i
print(sum)

# find prime numbers
for n in range(11):
    for i in range(2,n):
        if n % i == 0:
            print(n,"=",i,"*",n // i)
            break
    else:
        print(n,"is a prime number")