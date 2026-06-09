# Week 3 Exercise Starters

This folder contains small starter assets for the Week 3 foundation-model exercises.

## Exercise A: Structure Prediction

There is no course-specific Colab notebook for this week yet. Use one of these public notebooks rather than starting from a blank Colab:

- [ColabFold AlphaFold2 notebook](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb)
- [ColabFold batch notebook](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/beta/AlphaFold2_advanced.ipynb)

Keep inputs small. The Week 3 page suggests 1-3 proteins or domains under roughly 200 amino acids.

## Exercise B: Protein Embeddings

Build the starter FASTA from UniProt:

```bash
python3 fetch_proteins.py
```

This reads `protein_accessions.tsv` and writes `proteins.fasta`. The list is grouped by coarse protein family so you can check whether embedding-space clusters recover the labels.

In Colab, compute one embedding per protein, calculate cosine similarities, and make a PCA or UMAP plot colored by the family labels encoded in the FASTA headers.

Useful notebooks and references:

- [ESM variant prediction notebook](https://colab.research.google.com/github/facebookresearch/esm/blob/main/examples/variant_prediction.ipynb)
- [ESM inverse folding notebook](https://colab.research.google.com/github/facebookresearch/esm/blob/main/examples/inverse_folding.ipynb)
- [ESM model examples](https://github.com/facebookresearch/esm/tree/main/examples)

## Exercise C: Optional Genomic Benchmarks

Use a fresh notebook or script. These links are useful starting points:

- [Genomic Benchmarks repository](https://github.com/ML-Bioinfo-CEITEC/genomic_benchmarks)
- [Nucleotide Transformer v2 50M multi-species model card](https://huggingface.co/InstaDeepAI/nucleotide-transformer-v2-50m-multi-species)
- [HuggingFace Transformers notebooks](https://huggingface.co/docs/transformers/notebooks)

Write your final numbers and short interpretation in `results.md`.
