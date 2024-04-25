protein='SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'
corrected_protein='' #empty variable for string allocation needs to be initiated
for i in range(len(protein)):
    if(protein[i]) not in 'GAVLIMPYFWSTNQHDERCK':
        print("Protein contains invalid amino acid %s at position %d"%(protein[i],i))
        continue #This function helps in skipping the current loop and continuing with the next iteration of the nearest enclosing loop
    corrected_protein=corrected_protein+protein[i]

print("The corrected protein sequence is:\n%s"%corrected_protein) #see carefully that this print statement is outside the loop
#break function can be used to break out of a loop