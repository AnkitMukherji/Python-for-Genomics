def compute(n,x,y):
    if n==0: 
        print(x)
    return compute(n-1,x+y,y)
compute(-1,2,3)
#Couldn't understand the output