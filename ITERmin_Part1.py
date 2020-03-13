from Bio import SeqIO

fileA = SeqIO.parse("dengueprotseq","fasta")
for record in fileA:
    nr_sequence = record.seq
    seq_len = len(nr_sequence)
    kmer = 9
    count = 0
    for seq in list(range(seq_len-(kmer-1))):
        count += 1
        my_kmer = (nr_sequence[seq:seq+kmer])
        with open('output_kmers','a') as f:
            print(str(my_kmer), file=f)

f.close()


lines_seen = set ()

outfile = open("nr_kmers", "w")
for line in open("output_kmers", "r"):
        if line not in lines_seen: 
                outfile.write(line)
                lines_seen.add(line)
outfile.close()
