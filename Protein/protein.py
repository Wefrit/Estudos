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
        if protein in Methionine:
            proteins.append("Methionine")
        if protein in Phenylalanine:
            proteins.append("Phenylalanine")
        if protein in Leucine:
            proteins.append("Leucine")
        if protein in Serine:
            proteins.append("Serine")
        if protein in Tyrosine:
            proteins.append("Tyrosine")
        if protein in Cysteine:
            proteins.append("Cysteine")        
        if protein in Tryptophan:
            proteins.append("Tryptophan")
        if protein in STOP:
            break
    return proteins
