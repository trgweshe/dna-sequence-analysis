#after searching for a solution, i think using regular expressions would be the way forwars but i am open to ideas and i would appreciate all the help i can get


new_records= open("dna.example.fasta").read()
for frame in range(len(new_records)):
    result = re.findall(r"[ATGC]{3,5}", new_records)
    print(result)
