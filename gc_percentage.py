dna=input("Input DNA sequence\n") #The input function accepts the read input as string
dna_upper=dna.upper()
length_dna=len(dna_upper)
count_gc=int(dna_upper.count('C'))+int(dna_upper.count('G'))
print("The length of the DNA is: ",length_dna,"\nThe total number of G and C in the DNA sequence is: ",count_gc)
gc_percentage=(count_gc/length_dna)*100
print("The GC percentage of the DNA sequence is %5.3f%%: "% gc_percentage) #5 represents the total number of digits to be displayed and 3 indicates the number of digits after the decimal