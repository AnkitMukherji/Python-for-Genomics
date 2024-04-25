dna=input("Enter DNA sequence\n")
pos=dna.find('gt',0) #position of donor splice site
while pos > -1: #if no 'gt' is present we will get a value of -1
    print("Donor splice site candidate at position %d"%pos)
    pos=dna.find('gt',pos+1) #In Python Indentation is very important without which code will not work properly