# AlphaFold 2 Pipeline Diagrams

Visual guide to understanding how AlphaFold 2 predicts protein structures.

---

## 📚 Key Terms

| Term | Definition |
|------|------------|
| **Amino Acid** | Building block of proteins (20 types: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y) |
| **Residue** | Amino acid in a protein chain (after losing H₂O during peptide bond formation) |
| **Sequence** | Order of amino acids: `MKFLKFS...` |
| **MSA** | Multiple Sequence Alignment - similar sequences from evolution |
| **pLDDT** | Confidence score (0-100) per residue. >90 = very reliable |
| **PAE** | Predicted Aligned Error - uncertainty between residue pairs |
| **PDB** | File format for 3D protein structures |
| **Template** | Known structure used as reference |
| **Domain** | Distinct structural/functional region within a protein |

---

## 1. Pipeline Overview

```mermaid
flowchart TD
    subgraph Input ["1. Input Phase"]
        A[("Protein Sequence<br/>(FASTA)")]
    end

    subgraph Core ["2. Processing Phase (Iterative)"]
        B["MSA Search<br/>(Evolutionary Context)"] --> C["Feature Extraction"]
        C --> D["Neural Network<br/>(Evoformer)"]
        D --> E["Structure Module<br/>(3D Coordinates)"]
        E --> F{"Recycle?<br/>(Refine 3x)"}
        F -->|Yes| D
    end

    subgraph Result ["3. Output Phase"]
        F -->|No| G[("Final PDB Structure")]
        G --- H["Confidence Metrics<br/>(pLDDT + PAE)"]
    end

    A --> B

    style Input fill:#e3f2fd,stroke:#1565c0
    style Core fill:#fff9c4,stroke:#fbc02d
    style Result fill:#c8e6c9,stroke:#2e7d32
```

## 2. Confidence Scores (pLDDT)

```mermaid
graph LR
    subgraph Scale ["Confidence Spectrum (pLDDT)"]
        direction LR
        A[0] --- B["🔴 Low / Disordered<br/>(< 50)"]
        B --- C["🟠 Low Confidence<br/>(50 - 70)"]
        C --- D["🟡 Good<br/>(70 - 90)"]
        D --- E["🟢 Very High<br/>(> 90)"]
        E --- F[100]
    end

    style B fill:#ffcdd2,stroke:#b71c1c
    style C fill:#ffe0b2,stroke:#e65100
    style D fill:#fff9c4,stroke:#fbc02d
    style E fill:#c8e6c9,stroke:#1b5e20
```

## 3. PAE Matrix Interpretation

```mermaid
graph TD
    subgraph Matrix ["PAE Matrix (Predicted Aligned Error)"]
        A["Blue Region 🟦"] -->|Indicates| B["Rigid Relative Position<br/>(Fixed Domain)"]
        C["Red/Yellow Region 🟥"] -->|Indicates| D["Uncertain Relative Position<br/>(Flexible / Separate Domains)"]
    end
    
    subgraph Decision ["Analysis"]
        B --> E[Trust the domain structure]
        D --> F[Do not interpret relative orientation]
    end

    style A fill:#bbdefb,stroke:#0d47a1
    style C fill:#ffccbc,stroke:#bf360c
```

## 4. AlphaFold 2 Architecture

```mermaid
flowchart TD
    subgraph Data ["Data Preparation"]
        A["Input Sequence"] --> B["MSA (Evolution)"]
        A --> C["Templates (Known Structures)"]
    end

    subgraph Network ["Deep Learning (Evoformer)"]
        D["MSA Representation"] <-->|Exchange Info| E["Pair Representation"]
        D --"48 Layers"--> D
        E --"48 Layers"--> E
    end

    subgraph 3D ["Structure Generation"]
        F["Structure Module"] --> G["Backbone Frames"]
        G --> H["Side Chains"]
    end

    B --> D
    C --> E
    E --> F
    H --> I[Final Coordinates]

    style Data fill:#f3e5f5,stroke:#4a148c
    style Network fill:#fff3e0,stroke:#e65100
    style 3D fill:#e0f7fa,stroke:#006064
```

## 5. AlphaFold 3 Architecture (Unified)

```mermaid
flowchart TD
    subgraph Inputs ["Unified Input"]
        A[Protein] & B[DNA/RNA] & C[Ligands/Ions]
    end

    subgraph Model ["Deep Learning Core"]
        D[Input Embedder] --> E[Pairformer Stack]
        E --"Replaces Evoformer"--> E
    end

    subgraph Gen ["Generative Module"]
        F[Diffusion Module] -->|Noise -> Structure| G[Denoising Steps]
        G --> H[Final Assembly]
    end

    Inputs --> D
    E --> F
    H --> I[Complex Structure]

    style Inputs fill:#e1f5fe,stroke:#01579b
    style Model fill:#fff9c4,stroke:#fbc02d
    style Gen fill:#fbe9e7,stroke:#bf360c
```

## 6. Comparison: AF2 vs AF3

```mermaid
flowchart LR
    subgraph AF2 ["AlphaFold 2 (2021)"]
        A[Protein Only] --> B[Evoformer]
        B --> C[Structure Module]
        C --> D[Single/Multimer PDB]
    end

    subgraph AF3 ["AlphaFold 3 (2024)"]
        E[Protein + DNA/RNA + Ligand] --> F[Pairformer]
        F --> G[Diffusion Module]
        G --> H[Complex Structure]
    end

    style AF2 fill:#e3f2fd,stroke:#1565c0
    style AF3 fill:#e8f5e9,stroke:#1b5e20
```

## 7. Decision Guide: When to Trust?

```mermaid
flowchart TD
    Start[Prediction Complete] --> Check_pLDDT{Check pLDDT}
    
    Check_pLDDT -->|"High (>90)"| Check_PAE{"Check PAE"}
    Check_pLDDT -->|"Low (<50)"| Discard["❌ Disordered / Unreliable"]
    
    Check_PAE -->|"Blue (Low Error)"| Trust["✅ High Confidence Structure"]
    Check_PAE -->|"Red (High Error)"| Partial["⚠️ Trust Domains, Not Orientation"]

    style Trust fill:#c8e6c9,stroke:#1b5e20
    style Discard fill:#ffcdd2,stroke:#b71c1c
    style Partial fill:#fff9c4,stroke:#fbc02d
```

---

## Additional Resources

### Interactive Notebooks in This Repository
- **`alphafold2.ipynb`** - Complete AlphaFold 2 workflow with ColabFold
- **`alphafold3.ipynb`** - AlphaFold 3 preparation and analysis

### Online Resources
- **Try it online:** [ColabFold AlphaFold2 Notebook](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb)
- **AlphaFold Server:** [alphafoldserver.com](https://alphafoldserver.com) (for AlphaFold 3)
- **AlphaFold Database:** [alphafold.ebi.ac.uk](https://alphafold.ebi.ac.uk/) - Pre-computed structures
- **Original Paper:** [Jumper et al., Nature 2021](https://www.nature.com/articles/s41586-021-03819-2)
- **AlphaFold 3 Paper:** [Abramson et al., Nature 2024](https://www.nature.com/articles/s41586-024-07487-w)
- **DeepMind Blog:** [AlphaFold announcements](https://www.deepmind.com/research/highlighted-research/alphafold)
- **Visualization:** PyMOL, ChimeraX, py3Dmol, or Mol* viewers
