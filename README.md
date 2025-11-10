# AlphaFold 2 Quick Start Guide 🧬

Learn how AlphaFold 2 predicts protein 3D structures from sequences. This guide is for developers and learners with no biology background required.

## 📖 What is AlphaFold 2?

AlphaFold 2 is an AI system developed by DeepMind (2021) that predicts protein structures (3D shapes) from amino acid sequences (1D strings of letters). Think of it as translating a recipe (sequence) into a finished dish (structure).

## 🚀 Quick Start

### Option 1: Google Colab (Easiest - No Installation!)

1. Open [ColabFold Notebook](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb)
2. Click Runtime → Change runtime type → Select **GPU**
3. Paste your sequence in the input cell
4. Run all cells (Runtime → Run all)
5. Download results from the `results/` folder

### Option 2: Run Example Locally

```bash
# Clone this repo
git clone https://github.com/kimtth/science-alpha-fold-3-note.git
cd science-alpha-fold-3-note

# Run the quickstart
python quickstart.py
```

This creates a demo FASTA file and shows you the command to run ColabFold locally.

## 🔄 How It Works (Simplified)

```
1. Input Sequence → 2. Find Similar Sequences (MSA) → 3. Neural Network → 4. 3D Structure + Confidence
```

**More Detail:**
1. **Input:** You provide a sequence like `MKFLKFSLLT...`
2. **MSA Search:** AlphaFold 2 finds similar sequences from other organisms (evolution hints)
3. **Neural Network:** Evoformer (48 blocks) + Structure Module (8 layers) predict 3D coordinates
4. **Output:** PDB file with coordinates + confidence scores (pLDDT, PAE)

See [`Diagram.md`](./Diagram.md) for detailed visual explanations.

## 📊 Understanding Confidence Scores

### pLDDT (per-residue confidence)
- **90-100:** ✅ Very reliable
- **70-89:** ✅ Generally good
- **50-69:** ⚠️ Use with caution
- **0-49:** ❌ Likely unreliable/disordered

### PAE (position uncertainty)
- **Blue heatmap:** ✅ Well-defined structure
- **Yellow/Orange:** ⚠️ Uncertain domain arrangement
- **Red:** ❌ Very uncertain relative positions

**Rule of thumb:** Trust regions with pLDDT > 90 and blue PAE blocks.

## 💡 Common Use Cases

- **Drug Discovery:** Find where drugs can bind to proteins
- **Disease Research:** Understand how mutations affect protein shape
- **Protein Engineering:** Design new proteins with specific functions
- **Structural Biology:** Explore protein function from structure

## 🛠️ Installation (Optional - For Local Use)

If you want to run ColabFold locally instead of using Google Colab:

```bash
# Install ColabFold
pip install colabfold[alphafold]

# Create a FASTA file (your_protein.fasta)
>my_protein
MKFLKFSLLTAVLLSVVFAFSSCGDDDDTGYLPPSQAIQDLLKRMKV

# Run prediction
colabfold_batch your_protein.fasta results/

# Results will be in results/ folder:
# - ranked_0.pdb (3D structure)
# - *_plddt.png (confidence chart)
# - *_pae.png (uncertainty heatmap)
```

## 🆕 AlphaFold 3 (2024)

### What's New in AlphaFold 3

AlphaFold 3, released by Google DeepMind in May 2024, significantly expands capabilities beyond protein-only predictions:

**New Capabilities:**
- 🧬 **Protein-DNA interactions** - Transcription factors, nucleosomes
- 🧬 **Protein-RNA interactions** - Ribosomes, CRISPR complexes
- 💊 **Protein-ligand binding** - Drug molecules, cofactors, ions
- 🔗 **Multi-component complexes** - Proteins + nucleic acids + small molecules
- 🎯 **Post-translational modifications** - Glycosylation, phosphorylation

**Architecture Changes:**
- Replaces Evoformer with **Pairformer** (improved efficiency)
- **Diffusion-based structure generation** (instead of direct coordinate prediction)
- Unified model for all biomolecules (proteins, DNA, RNA, ligands)
- Better handling of large complexes (up to thousands of atoms)

### AlphaFold 3 Server Access

```bash
# AlphaFold 3 is available through:

# 1. AlphaFold Server (Web Interface - Free for non-commercial use)
#    https://alphafoldserver.com/welcome

# 2. API Access (Coming soon for academic/commercial licensing)
```

**Current limitations:**
- No local installation available yet (as of Nov 2024)
- Limited to web server for academic use
- Commercial use requires licensing

### Comparison: AlphaFold 2 vs AlphaFold 3

| Feature | AlphaFold 2 (2021) | AlphaFold 3 (2024) |
|---------|-------------------|-------------------|
| **Proteins** | ✅ Single/Multimer | ✅ Enhanced |
| **DNA/RNA** | ❌ | ✅ Yes |
| **Small molecules** | ❌ | ✅ Yes |
| **Ions/Ligands** | ❌ | ✅ Yes |
| **Architecture** | Evoformer + IPA | Pairformer + Diffusion |
| **Local install** | ✅ Available | ❌ Web only |
| **Open source** | ✅ Full code | ⚠️ Limited access |
| **Use case** | Protein structures | Biomolecular complexes |

### When to Use AlphaFold 3

✅ **Use AlphaFold 3 when:**
- Predicting protein-DNA/RNA complexes
- Modeling drug binding sites
- Studying protein-ligand interactions
- Analyzing post-translational modifications
- Predicting multi-component biological assemblies

✅ **Stick with AlphaFold 2 when:**
- Predicting single protein structures
- Need local installation
- Require open-source code for modifications
- High-throughput protein structure prediction

## 📖 Resources

### AlphaFold 2
- **ColabFold (easiest):** [AlphaFold2 Notebook](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb)
- **AlphaFold 2 Database:** [Pre-computed structures for millions of proteins](https://alphafold.com/)
- **Original AlphaFold 2 Paper:** [Jumper et al., Nature 2021](https://www.nature.com/articles/s41586-021-03819-2)
- **DeepMind GitHub:** [alphafold](https://github.com/deepmind/alphafold)

### AlphaFold 3
- **AlphaFold Server:** [Web Interface](https://alphafoldserver.com/welcome)
- **AlphaFold 3 Paper:** [Abramson et al., Nature 2024](https://www.nature.com/articles/s41586-024-07487-w)
- **Blog Post:** [Google DeepMind Announcement](https://blog.google/technology/ai/google-deepmind-isomorphic-alphafold-3-ai-model/)

### Visualization Tools
- **PyMOL** - Professional molecular visualization
- **ChimeraX** - Interactive 3D structure viewer
- **Mol*** - Web-based viewer (no installation needed)

