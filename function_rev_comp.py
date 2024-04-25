def reverse_complement(seq):
    "Return the reverse complement of the DNA"
    base_complement= {'A':'T', 'C':'G', 'G':'C','T':'A', 'N':'N', 'a':'t', 'c':'g', 'g':'c', 't':'a', 'n':'n'}
    letters=list(seq)
    letters=[base_complement[base] for base in letters]
    complement=''.join(letters)
    print(complement[::-1])
reverse_complement("CGAACTAC")
#Alternate way
def rev_comp(seq):
    complement= {'A':'T', 'C':'G', 'G':'C','T':'A', 'N':'N', 'a':'t', 'c':'g', 'g':'c', 't':'a', 'n':'n'}
    t=''
    for base in seq:
        t=complement[base] + t
    print(t)
rev_comp("CGAACTAC")