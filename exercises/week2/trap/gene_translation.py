from Bio import SeqIO
from Bio.Seq import Seq
import os

# récupérer le dossier où se trouve le script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

genome_path = os.path.join(BASE_DIR, "genome.fa")
gff_path = os.path.join(BASE_DIR, "annotations.gff3")

# charger le génome
genome_record = SeqIO.read(genome_path, "fasta")
genome_seq = genome_record.seq

# lire le GFF3
with open(gff_path) as f:
    for line in f:
        if line.startswith("#") or not line.strip():
            continue

        cols = line.strip().split("\t")
        if len(cols) < 9:
            continue

        if cols[2] != "CDS":
            continue

        start = int(cols[3]) - 1  # GFF = 1-based
        end = int(cols[4])
        strand = cols[6]
        attributes = cols[8]

        # nom du gène
        gene_name = "unknown"
        for attr in attributes.split(";"):
            if attr.startswith("Name="):
                gene_name = attr.split("=")[1]

        # séquence CDS
        cds_seq = genome_seq[start:end]

        if strand == "-":
            cds_seq = cds_seq.reverse_complement()

        # traduction
        protein_seq = Seq(cds_seq).translate(to_stop=False)

        # output demandé
        print(f"{gene_name}\t{cds_seq}\t{protein_seq}")