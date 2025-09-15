Methionine = "AUG"
Phenylalanine = "UUU", "UUC"	
Leucine = "UUA", "UUG"	
Serine = "UCU", "UCC", "UCA", "UCG"	
Tyrosine = "UAU", "UAC"	
Cysteine = "UGU", "UGC"	
Tryptophan = "UGG"	
STOP = "UAA", "UAG", "UGA"	

def proteins(strand):
    RNA = strand
    aminos = []
    proteins = []
    while len(RNA) > 0:
        aminos.append(RNA[:3])
        RNA = RNA[3:]

    for protein in aminos:
        if protein in Methionine and "Methionine" not in proteins:
            proteins.append("Methionine")
        if protein in Phenylalanine and "Phenylalanine" not in proteins:
            proteins.append("Phenylalanine")
        if protein in Leucine and "Leucine" not in proteins:
            proteins.append("Leucine")
        if protein in Serine and "Serine" not in proteins:
            proteins.append("Serine")
        if protein in Tyrosine and "Tyrosine" not in proteins:
            proteins.append("Tyrosine")
        if protein in Cysteine and "Cysteine" not in proteins:
            proteins.append("Cysteine")        
        if protein in Tryptophan and "Tryptophan" not in proteins:
            proteins.append("Tryptophan")
        if protein in STOP:
            break
    return proteins

print(proteins("UUUUUU"))