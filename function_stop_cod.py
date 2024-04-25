def has_stop_codon(dna,frame): #frame allows us to choose from one of the three frames in which DNA gets translated
    "This function checks if given dna sequence has in frame stop codons"
    stop_codon_found=False
    stop_codons=['taa','tag','tga']
    for i in range(frame,len(dna),3): #In place of frame, 0 can also be written to start the reading frame from 0
        codon=dna[i:i+3].lower() #lower function is called to convert any upper case letters to lower case if given as input
        if codon in stop_codons:
            stop_codon_found=True
            break
    print(stop_codon_found)
has_stop_codon('atgacagacgtacgtaagtca',2)