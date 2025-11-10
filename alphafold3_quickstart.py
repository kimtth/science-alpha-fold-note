"""
AlphaFold 3 Examples

Demonstrations of AlphaFold 3's extended capabilities for protein-DNA, 
protein-RNA, and protein-ligand predictions.

Note: AlphaFold 3 is currently only available via the AlphaFold Server web interface.
These examples show the input format and expected use cases.
"""

from typing import Dict


def explain_alphafold3_capabilities():
    """Overview of AlphaFold 3 features."""
    print("=" * 70)
    print("ALPHAFOLD 3 CAPABILITIES (2024)")
    print("=" * 70)
    
    capabilities = {
        "Proteins": "Enhanced accuracy for protein structures and complexes",
        "DNA/RNA": "Predict protein-nucleic acid interactions (e.g., transcription factors)",
        "Ligands": "Small molecule binding (drugs, cofactors, metabolites)",
        "Ions": "Metal ions and their coordination (Mg²⁺, Ca²⁺, Zn²⁺, etc.)",
        "Modifications": "Post-translational modifications (glycosylation, phosphorylation)",
        "Complexes": "Multi-component assemblies (protein + DNA + ligands)",
    }
    
    for feature, description in capabilities.items():
        print(f"\n{feature:15} → {description}")
    
    print("\n" + "=" * 70 + "\n")


def create_protein_dna_example() -> Dict:
    """
    Example: Transcription factor binding to DNA.
    
    Use case: Understanding how proteins recognize specific DNA sequences.
    """
    print("EXAMPLE 1: Protein-DNA Complex (Transcription Factor)")
    print("-" * 70)
    
    example = {
        "name": "Transcription_Factor_Complex",
        "description": "Zinc finger protein binding to DNA promoter region",
        "components": [
            {
                "type": "protein",
                "sequence": "MKLKFSLLTHVKLPVPGDKVEVRCPHYTCPVCGKSFSQKSDLVKHQRTHTG",
                "name": "ZincFingerProtein"
            },
            {
                "type": "dna",
                "sequence": "ATGCTAGCTAGCTAGCTA",  # DNA sequence (double-stranded)
                "name": "PromoterDNA"
            }
        ],
        "expected_output": "Structure showing zinc finger motifs inserted into DNA major groove"
    }
    
    print(f"\nProtein: {example['components'][0]['name']}")
    print(f"  Sequence: {example['components'][0]['sequence'][:30]}...")
    print(f"\nDNA: {example['components'][1]['name']}")
    print(f"  Sequence: {example['components'][1]['sequence']}")
    print(f"\nExpected: {example['expected_output']}")
    
    return example


def create_protein_rna_example() -> Dict:
    """
    Example: CRISPR-Cas9 with guide RNA.
    
    Use case: Gene editing complex structure prediction.
    """
    print("\n\nEXAMPLE 2: Protein-RNA Complex (CRISPR-Cas9)")
    print("-" * 70)
    
    example = {
        "name": "CRISPR_Cas9_Complex",
        "description": "Cas9 protein bound to guide RNA",
        "components": [
            {
                "type": "protein",
                "sequence": "MDKKYSIGLDIGTNSVGWAVITDEYKVPSKKFKVLGNTDRHSIKKNLIGAL...",  # Shortened
                "name": "Cas9_Protein",
                "note": "Full sequence ~1300 residues"
            },
            {
                "type": "rna",
                "sequence": "GUUUUAGAGCUAGAAAUAGCAAGUUAAAAUAAGGC",  # guide RNA
                "name": "GuideRNA"
            }
        ],
        "expected_output": "Cas9 with RNA guide in the active site channel"
    }
    
    print(f"\nProtein: {example['components'][0]['name']}")
    print(f"  Note: {example['components'][0]['note']}")
    print(f"\nRNA: {example['components'][1]['name']}")
    print(f"  Sequence: {example['components'][1]['sequence']}")
    print(f"\nExpected: {example['expected_output']}")
    
    return example


def create_protein_ligand_example() -> Dict:
    """
    Example: Enzyme with drug molecule.
    
    Use case: Drug discovery and binding site analysis.
    """
    print("\n\nEXAMPLE 3: Protein-Ligand Complex (Drug Binding)")
    print("-" * 70)
    
    example = {
        "name": "Kinase_Inhibitor_Complex",
        "description": "Protein kinase bound to ATP-competitive inhibitor",
        "components": [
            {
                "type": "protein",
                "sequence": "MENFQKVEKIGEGTYGVVYKARNKLTGEVVALKKIRLDTETEGVPSTAIRE...",
                "name": "Protein_Kinase"
            },
            {
                "type": "ligand",
                "smiles": "CC1=C2C(=NC=C1)N(C3=C(C=CC=C3)C2=O)CC4=CC=CC=C4",  # Example SMILES
                "name": "Kinase_Inhibitor",
                "note": "SMILES notation for small molecule"
            }
        ],
        "expected_output": "Inhibitor in ATP binding pocket with key H-bonds"
    }
    
    print(f"\nProtein: {example['components'][0]['name']}")
    print(f"  Sequence: {example['components'][0]['sequence'][:40]}...")
    print(f"\nLigand: {example['components'][1]['name']}")
    print(f"  {example['components'][1]['note']}")
    print(f"  SMILES: {example['components'][1]['smiles'][:40]}...")
    print(f"\nExpected: {example['expected_output']}")
    
    return example


def create_multi_component_example() -> Dict:
    """
    Example: Nucleosome core particle.
    
    Use case: Chromatin structure and epigenetics.
    """
    print("\n\nEXAMPLE 4: Multi-Component Complex (Nucleosome)")
    print("-" * 70)
    
    example = {
        "name": "Nucleosome_Core_Particle",
        "description": "Histone octamer wrapped by DNA with modifications",
        "components": [
            {
                "type": "protein",
                "chains": ["H2A", "H2B", "H3", "H4"],
                "copies": "2 copies each (8 total histones)",
                "note": "Histone octamer core"
            },
            {
                "type": "dna",
                "length": "147 base pairs",
                "note": "DNA wrapped 1.65 turns around histones"
            },
            {
                "type": "modifications",
                "sites": ["H3K4me3", "H3K27ac"],
                "note": "Post-translational modifications on histones"
            }
        ],
        "expected_output": "DNA superhelix around histone octamer with modification sites"
    }
    
    print("\nComponents:")
    print(f"  - {example['components'][0]['copies']}")
    print(f"  - DNA: {example['components'][1]['length']}")
    print(f"  - Modifications: {', '.join(example['components'][2]['sites'])}")
    print(f"\nExpected: {example['expected_output']}")
    
    return example


def show_alphafold_server_workflow():
    """Demonstrate how to use AlphaFold Server for AF3 predictions."""
    print("\n\n" + "=" * 70)
    print("HOW TO USE ALPHAFOLD 3 SERVER")
    print("=" * 70)
    
    print("\n📌 STEP-BY-STEP WORKFLOW:")
    print("-" * 70)
    
    steps = [
        ("1. Access", "Go to https://golgi.sandbox.google.com/"),
        ("2. Sign in", "Use Google account (free for academic use)"),
        ("3. Create job", "Click 'New Prediction'"),
        ("4. Add protein", "Paste sequence or upload FASTA"),
        ("5. Add DNA/RNA", "(Optional) Add nucleic acid sequences"),
        ("6. Add ligands", "(Optional) Add SMILES strings or select from library"),
        ("7. Configure", "Set job name and parameters"),
        ("8. Submit", "Run prediction (takes ~10-30 minutes)"),
        ("9. Download", "Get PDB file + confidence scores + visualizations"),
    ]
    
    for step, description in steps:
        print(f"\n   {step:15} {description}")
    
    print("\n\n💡 INPUT FORMAT TIPS:")
    print("-" * 70)
    print("   • Proteins: Standard amino acid sequence (FASTA)")
    print("   • DNA: A, T, G, C (automatically paired with complement)")
    print("   • RNA: A, U, G, C")
    print("   • Ligands: SMILES notation or PubChem CID")
    print("   • Ions: Select from dropdown (Mg, Ca, Zn, Fe, etc.)")


def show_confidence_interpretation_af3():
    """Explain confidence metrics specific to AlphaFold 3."""
    print("\n\n" + "=" * 70)
    print("ALPHAFOLD 3 CONFIDENCE METRICS")
    print("=" * 70)
    
    print("\n📊 NEW METRICS:")
    print("-" * 70)
    
    metrics = {
        "pLDDT": "Per-residue confidence (same as AF2, 0-100)",
        "pAE": "Position error between pairs (same as AF2)",
        "pTM": "Predicted TM-score (overall structure similarity, 0-1)",
        "ipTM": "Interface pTM (confidence in protein-protein interfaces)",
        "Ligand confidence": "Binding pose reliability (contact probability)",
        "Interface contact": "Probability of correct molecular interface",
    }
    
    for metric, description in metrics.items():
        print(f"\n{metric:20} → {description}")
    
    print("\n\n✅ GOOD PREDICTION INDICATORS:")
    print("   • pLDDT > 70 for protein regions")
    print("   • pTM > 0.5 for overall fold")
    print("   • ipTM > 0.5 for interface contacts")
    print("   • High contact probability for ligand binding")
    
    print("\n\n⚠️  CAUTION ZONES:")
    print("   • Low pLDDT (<50) indicates disorder or uncertainty")
    print("   • Low ipTM (<0.3) suggests uncertain complex orientation")
    print("   • Weak ligand contacts may indicate multiple binding modes")


def compare_use_cases():
    """When to use AlphaFold 2 vs AlphaFold 3."""
    print("\n\n" + "=" * 70)
    print("WHICH VERSION SHOULD YOU USE?")
    print("=" * 70)
    
    print("\n🔬 USE ALPHAFOLD 2 FOR:")
    print("-" * 70)
    use_af2 = [
        "Single protein structure prediction",
        "Protein-protein complexes (multimer)",
        "High-throughput structure generation",
        "Local installation required",
        "Need full code access for modifications",
    ]
    for use in use_af2:
        print(f"   ✓ {use}")
    
    print("\n\n🧬 USE ALPHAFOLD 3 FOR:")
    print("-" * 70)
    use_af3 = [
        "Protein-DNA/RNA interactions",
        "Drug binding predictions",
        "Protein-ligand complexes",
        "Multi-component assemblies",
        "Post-translational modifications",
        "Most accurate protein structures (improved over AF2)",
    ]
    for use in use_af3:
        print(f"   ✓ {use}")


def main():
    """Run all AlphaFold 3 examples and explanations."""
    
    print("\n🧬 AlphaFold 3 Examples and Guide")
    print("=" * 70)
    print("Demonstrations of AlphaFold 3's extended capabilities.")
    print("Note: Currently available only via AlphaFold Server (web interface)\n")
    
    # Overview
    explain_alphafold3_capabilities()
    
    # Examples
    examples = []
    examples.append(create_protein_dna_example())
    examples.append(create_protein_rna_example())
    examples.append(create_protein_ligand_example())
    examples.append(create_multi_component_example())
    
    # Usage guide
    show_alphafold_server_workflow()
    
    # Confidence interpretation
    show_confidence_interpretation_af3()
    
    # Comparison
    compare_use_cases()
    
    print("\n\n" + "=" * 70)
    print("✅ AlphaFold 3 examples complete!")
    print("=" * 70)
    print("\n🌐 Get started: https://golgi.sandbox.google.com/")
    print("📖 Read paper: https://www.nature.com/articles/s41586-024-07487-w")
    print("\n💡 For protein-only predictions, see quickstart.py (AlphaFold 2)\n")


if __name__ == "__main__":
    main()
