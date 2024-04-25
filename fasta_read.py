try:
    f=open("fasta_file.fa")
except IOError:
    print("the file fasta_file does not exist")
seqs={}
for line in f:
    #let's discard the newline at the end(if any)
    line=line.rstrip() #Returns a copy of the string with trailing characters removed
    #To distinguish header from the sequence
    if line[0]=='>': # or line.startswith('>')
        #Initializing a dictionary containing the name and the sequence
        #name of the sequence
        words=line.split() #splitting each character of the line containing '>'
        name=words[0][1:] #Ignore the character at the 0th position i.e. '>' and start from the 1st position
        seqs[name]=''
    else: #sequence, not header
        seqs[name]=seqs[name]+line
f.close()
for name,seq in seqs.items():
    print(name,seq)