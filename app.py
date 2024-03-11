import sys
from Bio import Entrez

Entrez.email = sys.argv[1]
handle = Entrez.efetch(db="nucleotide", id=sys.argv[2:], rettype="fasta")
records = handle.read
print(records)
