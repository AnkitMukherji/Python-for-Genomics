from Bio.Blast import NCBIWWW
fasta_string = open("coursera_qs12.fasta").read()
result_handle = NCBIWWW.qblast("blastn","nt",fasta_string)
print(result_handle)
with open("results_bio_python.xml","w") as save_file:
    blast_results=result_handle.read()
    save_file.write(blast_results)