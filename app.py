import sys
from Bio import Entrez
from Bio import SeqIO

arguments = sys.argv[1:]
if len(arguments) > 11:
    print('Error: please, search for a maximum of 10 IDs')
    sys.exit()
Entrez.email = sys.argv[1]
handle = Entrez.efetch(db="nucleotide", id=sys.argv[2:], rettype="fasta")
records = list (SeqIO.parse(handle, "fasta"))
result = float('inf')
for record in records:
    if result > len(record.seq):
        result = len(record.seq)
        resultSeq = record
print(resultSeq)
