


new_records= open("dna.example.fasta").read()
for frame in range(len(new_records)):
    result = re.findall(r"[ATGC]{3,5}", new_records)
    print(result)