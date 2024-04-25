gene_expression=['gene',5.16e-08,0.000138511,7.33e-08] #This is called list and different types of values can be put in here
print(gene_expression[2])
gene_expression[0]='brca'
print(gene_expression)
motif='nacgcgacgcatctca'
#motif[0]='a' #String elements cannot be replaced so strings are immutable data types while lists are mutable data types
print(gene_expression[-3:])
gene_expression[1:3]=[6.09e-07] #This replaces 1st and 2nd element of the list by the new element
print(gene_expression)
gene_expression[:]=[] #This clears the list
print(gene_expression)
expression=gene_expression+['thfk',5.16e-08,0.0001358111] #This concatenates two lists and therefore has to be stored in another variable
print(len(expression))
del(expression[1]) #Deleting any element from the list which shifts the next element to the position of the deleted element
print(expression)
expression.extend([5.16e-08]) #Extends the same list therefore is stored in the same variabe. Extend takes a list as an argument
print(expression)
print(expression.count('thfk'),expression.count('gene')) #Gives the count of certain elements in the list
expression.reverse() #Reverse the elements of the list
print(expression)
#help(list)
stack=['a','b','c','d']
stack.append('e') #Append takes only one element as an argument as compared to extend. If we try to append a list, it will become a single element in the list
elem=stack.pop() #To retrieve/remove an element from the top of the stack
print(stack)
mylist=[3,31,123,1,5]
print(sorted(mylist)) #1st way of sorting lists
mylist.sort()
print(mylist) #2nd way of sorting lists
myvar=['c','g','T','a','A'] #In sorting, upper case letters always come first then the lower case
print(sorted(myvar))
myvar.sort()
print(myvar)
print("Lets learn about tuples")
t=1,2,3 #All operations of lists can be applied on tuples until it doesn't change the value of the tuple
print(t)
brca1={'DNA Repair','Zinc Ion Binding','DNA Repair','Protein Ubiquitylation'}
brca2={'protein binding','DNA Repair','Histone transferase'}
print(brca1) #Removes all the repeated values
print(brca1 | brca2) #Prints the union of the two sets
print(brca1 & brca2) #Prints the intersection of the two sets
print(brca1 - brca2) #Prints the difference between the two sets
tf_motif={'SP1':'acgcaag','ATF':'ttaagac'} #Represents a dictionary where the key is SP1 and their corresponding value is acgcaag
print("The recognition sequence of the ATF transcription factor is %s" % tf_motif['ATF']) #Key within square bracket displays the value
print('SP1' in tf_motif) #To check whether a key is present in our dictionary or not
tf_motif['AP-1']='aaacccgta' #Adding a key:value pair to the dictionary
tf_motif['AP-1']='aaac(c/g)gta' #Modifying a value of a key in the dictionary
del tf_motif['SP1'] #Deleting a key along with its value from the dictionary
tf_motif.update({'SP1':'ggcgggc','ATF':'ttaagag'}) #Adding multiple key value pairs to the current dictionary
print(tf_motif)
print(len(tf_motif)) #Lists the length of the keys in the dictionary
print(list(tf_motif.keys())) #List the keys of the dictionary, Similarly values can be displayed by replacing the key term by values
print(sorted(tf_motif.keys())) #Sorts the keys, Similarly the values can be sorted Note: Sorting occurs in ascending order(in case of numbers) and in alphabetical order(in case of alphabets)