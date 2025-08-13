def to_rna(dna_strand):
    RNA = {'G' : 'C', 'C':'G', 'T':'A', 'A':'U'}
    strand = ''
    for nucleotid in dna_strand:
        strand += RNA[nucleotid]
    return strand
