n=10
for y in range(2,n):
    for x in range(2,y):
        if y % x == 0:
            print(y," equals ",x," * ",y//x)
            break #this breaks the inner if statement once a factor is found as it is surely not prime
    else: #this breaks the inner loop without finding a factor as we don't need to iterate the inner loop if the number is prime
        print(y,"is a prime number")            
"""
n=10
c=0
for y in range(2,n):
    for x in range(2,y+1):
        if (y % x) == 0:
            c+=1
    if c > 1:
        print(y," is a composite number")
    else:
        print(y," is a prime number")
    c=0
"""