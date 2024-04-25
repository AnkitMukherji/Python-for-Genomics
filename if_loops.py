dna=input('Enter a DNA sequence\n')
nbases=dna.count('N')+dna.count('n')
if 'N' in dna or 'n' in dna: #Similarly 'and' and 'not'(true if condition is false) operator can be used
    print("DNA sequence has %d undefined bases "%nbases)
else : #else if condition can be given by 'elif'
    print("DNA sequence has no undefined bases")