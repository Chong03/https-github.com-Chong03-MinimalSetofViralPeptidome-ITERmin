from Bio import SeqIO
import pandas as pd

fileA = list(SeqIO.parse("dengueprotseq","fasta"))
fileB = pd.read_csv("nr_kmers",header = None)

a = 0
while len(fileB) != 0: 
    output = open("matchingOut"+str(a)+".txt","w")
    n = len(fileA)
    for i in range (0,n):
            kmercount = 0
            fullseq = fileA[i].seq
            for kmer in fileB[0]:
                    if (fullseq.count(kmer) == 1):
                            kmercount+=1
            output.write(fileA[i].id + ';' + str(kmercount) + '\n')

    output.close()

    unsortedcp_fileC = pd.read_csv("matchingOut"+str(a)+".txt",header=None)
    output = open("sortedcplist_fileD"+str(a)+".txt","w")

    split_data = pd.DataFrame(unsortedcp_fileC[0].str.split(';',1).tolist(), columns=['acc_no','cp_count'])
    split_data.cp_count = pd.to_numeric(split_data.cp_count)
    sortedcplist_fileD = split_data.sort_values(by='cp_count',ascending=False)
    output.write(sortedcplist_fileD.to_string())

    output.close()

    highestCPSeq = sortedcplist_fileD.iloc[0,0]
    fileZ = open("fileZ"+str(a)+".txt","w")
    for seq in fileA:
            if(seq.id == highestCPSeq):
                fullseq_highestCPid = seq.id
                fileZ.write(seq.id + '\n')
                fullseq_highestCP = seq.seq

    fileZ.close()

    fileY = open("fileY"+str(a)+".txt","w")
    len(fileB[0])
    for index, kmer in enumerate(fileB[0]):
        if (kmer in fullseq_highestCP):
            fileY.write(kmer + '\n')
            fileB.drop(index, inplace = True)

    fileY.close()
    fileB.reset_index(drop = True, inplace = True)
    fileB.to_csv("fileX"+str(a), index = None, header = None)
    a += 1
