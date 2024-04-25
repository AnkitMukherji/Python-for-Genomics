records=0
try:
    f=open('D:\Learning Skills\Learning Programming\Learning Python\Coursera\Final Exam\dna.example.fasta','r')
    g=open('D:\Learning Skills\Learning Programming\Learning Python\Coursera\Final Exam\dna.example.fasta','a')
    h=open('file.txt','w')
except IOError:
    print("the file does not exist")
header_length={}
for header in f:
    if header[0] == '>':
        records=records+1
records=records-1
#print("There are %d records in this file"%records)
f.seek(0)
g.write('>')
seq=''
seq_max_min={}
seq_orf=[]
for sequence in f:
    if sequence[0] != '>':
        length_line=len(sequence)
        seq=seq+sequence[0:length_line-1]
    else:
        length=len(seq)
        if(length != 0):
            #print("The length of the sequence is %d"%length)
            seq_orf.append(seq)
            seq_max_min.update({length:seq})
            seq=''
seq_max_min=str(sorted(seq_max_min.items()))
#print(seq_max_min)
