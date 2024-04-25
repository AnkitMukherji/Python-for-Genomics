def function1(length):
    if length > 0:
        print(length)
        function1(length-1)
function1(3)

def function2(length):
    while length > 0:
        print(length)
        function2(length-1)
function2(3)
#See why the while loop runs infinitely