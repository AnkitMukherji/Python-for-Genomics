import random
#random.seed(5) #seed function with an integer gives the same choice every time
print(random.choice('ACGT')) #gives different nucleotides every time
#Generating a random sequence of nucleotides having length 10
seq=''
for _ in range(10): #'_' means that the indexing is not necessary
    seq+=random.choice('ACGT')
print(seq)
#Using join to generate random strings
seq=''.join((random.choice('ACGT')) for _ in range(10))
print(seq)