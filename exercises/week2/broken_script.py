"""Small intentionally broken FASTA summarizer for Week 2.

Use an agentic IDE to fix this script one issue at a time. The intended
behavior is: read a FASTA file, print one row per sequence, and report sequence
length plus GC percentage.
"""

from pathlib import Path


def read_fasta(path):
    records = {}
    current_name = None
    current_seq = []

    for line in Path(path).read_text().splitlines():
        line = line.strip()

        if line.startswith(">"):
            if current_name is not None:
                records[current_name] = "".join(current_seq)

            current_name = line[1:]
            current_seq = []
        else:
            if line:
                current_seq.append(line)

    # dernier record
    if current_name is not None:
        records[current_name] = "".join(current_seq)

    return records


def gc_percent(sequence):
    if len(sequence) == 0:
        return 0.0

    gc = sequence.count("G") + sequence.count("C")
    return (gc / len(sequence)) * 100


def main():
    # fichier dans le même dossier que le script
    fasta_path = Path(__file__).parent / "example.fa"

    if not fasta_path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {fasta_path}")

    records = read_fasta(fasta_path)

    for name, sequence in records.items():
        print(f"{name}\t{len(sequence)}\t{gc_percent(sequence):.2f}%")


if __name__ == "__main__":
    main()
