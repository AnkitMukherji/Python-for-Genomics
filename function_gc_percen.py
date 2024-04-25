def gc(dna):
    "this function computes the gc percentage of a dna sequence"
    nbases=dna.count('n')+dna.count('N')
    gcpercent=float(dna.count('c')+dna.count('C')+dna.count('g')+dna.count('G'))*100.0/(len(dna)-nbases)
    print(gcpercent) #printing the function instead of using return
gc('AAAGTNNAGTCC') #calling the function gc
help(gc)