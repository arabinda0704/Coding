def Fib(n):
    if n==2 or n==1:
        return 1;
    return Fib(n-1)+Fib(n-2)
    
def Square(n):
    if n//10==0:
        return n**2
    return Square(n//10)+(n%10)**2

print(Fib(7))
print(Square(24318))

for i in range(10):
    for j in range(i):
        if j<=i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(1,5):
    for j in range(1,8):
        if j>=4-i+1 and j<=4+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print("----------------------------")

for i in range(1,5):
    for j in range(1,8):
        if j>=i and j<=8-i:
            print("*", end="")
        else:
            print(" ", end="")
    print()