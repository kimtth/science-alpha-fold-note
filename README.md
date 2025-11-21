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

### Option 2: Use Interactive Notebooks

This repository includes two interactive Jupyter notebooks:

1. **`alphafold2.ipynb`** - Complete AlphaFold 2 workflow with ColabFold
   - Install and configure ColabFold
   - Run actual protein structure predictions
   - Visualize 3D structures interactively
   - Analyze confidence metrics (pLDDT and PAE)
   - Compare multiple model predictions

2. **`alphafold3.ipynb`** - AlphaFold 3 preparation and analysis
   - Prepare inputs for protein-DNA, protein-RNA, and protein-ligand complexes
   - Submit jobs to AlphaFold Server
   - Analyze and visualize results

```bash
# Clone this repo
git clone https://github.com/kimtth/science-alpha-fold-note.git
cd science-alpha-fold-note

# Open notebooks in Jupyter or VS Code
jupyter notebook alphafold2.ipynb
```

## 🧬 How to Get Protein Sequences

To predict a structure, you need the amino acid sequence (FASTA format).

1. **Go to [UniProt](https://www.uniprot.org/)** (Universal Protein Resource)
2. **Search** for your protein (e.g., "Hemoglobin human")
3. **Click** on the Entry ID (e.g., `P69905`)
4. **Scroll** to the "Sequence" section
5. **Copy** the sequence of letters (e.g., `MVLSPADKT...`)
6. **Or click** "Download" → "FASTA (canonical)"

**Example FASTA format:**
```text
>sp|P69905|HBA_HUMAN Hemoglobin subunit alpha
MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHG
KKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTP
AVHASLDKFLASVSTVLTSKYR
```

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

## Installation (Optional - For Local Use)

If you want to run ColabFold locally instead of using Google Colab:

```bash
# Install ColabFold
pip install 'colabfold[alphafold-minus-jax] @ git+https://github.com/sokrypton/ColabFold'

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

## 📚 Key Terminology

| Term | Meaning |
|------|---------|
| **Protein** | Biological molecule made of amino acids that performs functions in living organisms |
| **Amino Acid** | Building block of proteins (20 types: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y) |
| **Sequence** | Order of amino acids, written as text: `MKFLKFSLLT...` |
| **Structure** | 3D shape showing where each atom is positioned in space |
| **Residue** | An amino acid when it's part of a protein chain. When amino acids link together (via peptide bonds), they lose a water molecule and what remains is called a "residue." Example: A protein with 100 amino acids = 100 residues. Used for numbering positions (e.g., "residue 42" = the 42nd amino acid in the chain) |
| **MSA** | Multiple Sequence Alignment - similar sequences from evolution |
| **pLDDT** | Confidence score (0-100) for each residue position |
| **PAE** | Predicted Aligned Error - uncertainty between residue pairs |
| **PDB** | File format for 3D protein structures |
| **Template** | Known structure used as reference (optional) |
| **Domain** | Distinct structural region within a protein |

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
#    https://alphafoldserver.com

# 2. API Access (Web interface only - programmatic access coming soon)
```

**Current limitations (as of Nov 2025):**
- **Local installation:** Code is available under CC-BY-NC-SA 4.0 license. Model parameters require approval via [Google form](https://forms.gle/svvpY4u2jsHEwWYS6) (granted at Google DeepMind's discretion)
- **Web Server:** Available at [alphafoldserver.com](https://alphafoldserver.com) for non-commercial use with daily limits
- **Commercial use:** Requires specific licensing from Google DeepMind

### Comparison: AlphaFold 2 vs AlphaFold 3

| Feature | AlphaFold 2 (2021) | AlphaFold 3 (2024) |
|---------|-------------------|-------------------|
| **Proteins** | ✅ Single/Multimer | ✅ Enhanced |
| **DNA/RNA** | ❌ | ✅ Yes |
| **Small molecules** | ❌ | ✅ Yes |
| **Ions/Ligands** | ❌ | ✅ Yes |
| **Architecture** | Evoformer + IPA | Pairformer + Diffusion |
| **Local install** | ✅ Open Source (Apache 2.0) | ⚠️ Code available (CC-BY-NC-SA 4.0), weights require approval |
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
- **AlphaFold Server:** [Web Interface](https://alphafoldserver.com)
- **AlphaFold 3 Paper:** [Abramson et al., Nature 2024](https://www.nature.com/articles/s41586-024-07487-w)
- **Blog Post:** [Google DeepMind Announcement](https://blog.google/technology/ai/google-deepmind-isomorphic-alphafold-3-ai-model/)

### Visualization Tools
- **PyMOL** - Professional molecular visualization
- **ChimeraX** - Interactive 3D structure viewer
- **Mol*** - Web-based viewer (no installation needed)
