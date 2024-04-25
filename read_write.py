try:
    f=open('my_file.txt') #The entire path of the file can also be given
except IOError:
    print("the file my_file does not exist")
for line in f: #Reads the file line by line
    print(line)
print(f.read()) #Read function reads the file all at once but nothing gets printed here as we have already read the file and nothing is there to read 
#To adjust this
f.seek(0) #Go to the position 0 of the file
print(f.read())
f.seek(0)
print(f.readline()) #Reads the first line of the line only
print(f.read())
f.close()
g=open('D:\Learning Skills\Learning Programming\Learning Python\Coursera\my_file.txt','a')
g.write("This is the third line")
g.close()