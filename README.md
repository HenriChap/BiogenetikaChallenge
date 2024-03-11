# BiogenetikaChallenge
## Automated data retrieve from Entrez

From [Rosalind](https://rosalind.info/problems/frmt/)

"Given: A collection of n (n≤10) GenBank entry IDs.

Return: The shortest of the strings associated with the IDs in FASTA format."

## To do so:
You can use Codespaces to start working right away! Just click on "Code" and create a Codespace. Then you run in the terminal: 

```bash
python app.py youremail@mail.com ID1 ID2 ...
```
Remember to use your email signed to Entrez and use up to 10 IDs each time. The shortest FASTA ID will be provided.

Attention: if more than one ID has the shortest sequence size, only the first will be output
