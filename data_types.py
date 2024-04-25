print("Hello"[0]) #Subscript
print("123"+"345") #String
print(123+345) #Integer
3.145 #Float which is same as real number
True or False #Boolean
123_345 #This is also read as 123345
"False" #This is not Boolean but String
num_char=len("1234")
print(type(num_char)) #type function displays the data type2
new_num_char=str(num_char) #converts the data type of num_char into string
#print("The length of the number is"+num_char) #Gives an error as number cannot be concatenated to string
print("The length of the number is "+new_num_char)
print(type(new_num_char))
a=float(123)
print(type(a))
print(70+float("100.5"))
print(str(70)+str(100))
print(type((3+2j)*2))