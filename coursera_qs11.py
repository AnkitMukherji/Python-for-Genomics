def count(dna,base):
    print(len([i for i in range(len(dna)) if dna[i] == base]))
count("TAAACGCGCGAACT","A")