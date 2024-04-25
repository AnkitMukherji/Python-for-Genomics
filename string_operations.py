print('atg'+'atagccgat') #'+' used for concatenating two strings
print('atg'*3) #'*' replicates
print('atg' in 'cgatgtcagtcatg') #'in' finds the word in the string and returns True or False depending on whether it has found the string or not
print('n' in 'agtgtacgtacgtac')
dna="atgctggggact"
print(dna[2]) #This is called Indexing
print(dna[3:8]) #This is called Slicing which gives a substring between positions x and y in a string. Starting is included but Ending is excluded
print(dna[-1]) #Indexing from the right starts from -1
print(dna[:3]) #An omitted first index defaults to zero and the ending position is excluded
print(dna[2:]) #An omitted second index extracts the entire string from the x position
#help(len) #help function
print(dna.count('c')) #'.' operator asks the dna variable to do soemthing for e.g., here it tells to count the number of 'c' characters in the dna
print(dna.count('gc'))
print(dna.upper()) #upper function changes all characters to upper case, similarly lower function can be used
print(dna.find('ag')) #find operation find the first occurence of our query
print(dna.find('ag',6)) #helps in finding our query from the 6th position itself but returns only the first hit from the 6th position
print(dna.rfind('ag')) #helps in finding our query from the end of the string and it returns a single value
#help(str)
print(dna.islower()) #checks whether our string is in lower case or not. Similarly isupper function can also be used
print(dna.replace('t','u'))
print(chr(65)) #Converts the integer to a character
print("%5.3f" % 54.63215879) #f represents that it returns a float formatting type, 5 represents the total digits and 3 represents the number of digits to be displayed after the decimal point
print("%d" % 10.6) #d represents that it returns an integer value
print("%3d" % 10.6) #3 represents the padding space 
#Similarly %o can be used to represent octal and %x for hexadecimal integer
# %e for scientific notation of powers of 10
# %s to print something as a string 
alphabet=['a','t','g','c']
new_alphabet=alphabet[:] #Slice operator creates a new list
print(alphabet == new_alphabet) 
print(alphabet is new_alphabet) #Although the elements are the same, the new list created would be allocated in a new memory space there the 'is' operator returns False