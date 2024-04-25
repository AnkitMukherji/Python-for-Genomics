def valid_dna1(dna):
    for c in dna:
        if not c in 'acgtACGT':
            print (False)
    print (True)
valid_dna1("CATACA")