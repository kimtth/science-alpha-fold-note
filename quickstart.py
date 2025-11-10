"""
AlphaFold 2 / ColabFold Quick Start

This script demonstrates how to prepare inputs and run AlphaFold 2 predictions.
No biology background needed - all terms are explained!

AlphaFold 2 (2021) by DeepMind predicts protein structures using:
- 48 Evoformer blocks for evolutionary analysis
- 8-layer Structure Module with Invariant Point Attention (IPA)
- 3 recycling iterations for refinement
"""

from pathlib import Path


def explain_terminology():
    """Print key terms for beginners."""
    print("=" * 70)
    print("KEY TERMS EXPLAINED")
    print("=" * 70)
    
    terms = {
        "Protein": "Biological molecule made of amino acids that performs functions",
        "Amino Acid": "Building block of proteins (20 types: A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y)",
        "Sequence": "Order of amino acids, written as text (e.g., 'MKFL...')",
        "Residue": "Amino acid in a protein chain. When amino acids link (peptide bonds), "
                   "they lose H₂O and form residues. Used for counting: 150 residues = 150 amino acids long",
        "FASTA": "Text file format for storing sequences (starts with '>' then name)",
        "MSA": "Multiple Sequence Alignment - similar sequences found in nature",
        "pLDDT": "Confidence score (0-100) per residue. >90 = very reliable",
        "PAE": "Predicted Aligned Error - uncertainty between residue positions",
        "PDB": "File format storing 3D coordinates of atoms in a protein",
    }
    
    for term, definition in terms.items():
        print(f"\n{term:15} → {definition}")
    
    print("\n" + "=" * 70 + "\n")


def create_fasta_file(sequence: str, protein_name: str) -> Path:
    """
    Create a FASTA file for AlphaFold input.
    
    Args:
        sequence: Amino acid sequence (e.g., "MKFLKFS...")
        protein_name: Name for your protein
    
    Returns:
        Path to the created FASTA file
    """
    print(f"Creating FASTA file for: {protein_name}")
    print(f"Sequence length: {len(sequence)} residues (amino acids)\n")
    
    # Wrap sequence at 80 characters per line (standard FASTA format)
    wrapped_sequence = "\n".join(
        sequence[i:i + 80] for i in range(0, len(sequence), 80)
    )
    
    # Create FASTA content
    fasta_content = f">{protein_name}\n{wrapped_sequence}\n"
    
    # Write to file
    fasta_path = Path(f"{protein_name}.fasta")
    fasta_path.write_text(fasta_content)
    
    print(f"✅ Created: {fasta_path}")
    print("\nFASTA file content:")
    print("-" * 50)
    print(fasta_content)
    print("-" * 50)
    
    return fasta_path


def show_colabfold_options():
    """Display two ways to run ColabFold."""
    print("\n" + "=" * 70)
    print("HOW TO RUN ALPHAFOLD 2 / COLABFOLD")
    print("=" * 70)
    
    print("\n📌 OPTION 1: Google Colab (Easiest - No Installation!)")
    print("-" * 70)
    print("1. Open this link:")
    print("   https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb")
    print("\n2. Click: Runtime → Change runtime type → Select 'GPU'")
    print("\n3. Paste your sequence in the input cell")
    print("\n4. Click: Runtime → Run all")
    print("\n5. Wait for results (10-30 minutes for typical proteins)")
    print("\n6. Download results from the 'results/' folder")
    
    print("\n\n📌 OPTION 2: Local Installation (For Repeated Use)")
    print("-" * 70)
    print("Step 1: Install ColabFold")
    print("   pip install colabfold[alphafold]")
    print("\nStep 2: Run prediction")
    print("   colabfold_batch demo_protein.fasta results/")
    print("\nStep 3: Check results in 'results/' folder")


def explain_command_flags(fasta_path: Path):
    """Explain the ColabFold command and its options."""
    print("\n\n" + "=" * 70)
    print("COMMAND BREAKDOWN")
    print("=" * 70)
    
    print("\nBasic command:")
    print(f"   colabfold_batch {fasta_path} results/")
    
    print("\n\nWhat this does:")
    print("   colabfold_batch  →  Run ColabFold prediction")
    print(f"   {fasta_path}     →  Your input sequence file")
    print("   results/         →  Where to save output files")
    
    print("\n\nOptional flags you can add:")
    print("   --num-models 5      →  Run 5 different model variants (default)")
    print("   --num-recycle 3     →  Refine prediction 3 times (default)")
    print("   --amber             →  Polish geometry using Amber force field")
    print("   --use-gpu-relax     →  Speed up Amber relaxation with GPU")
    
    print("\n\nExample with options:")
    print(f"   colabfold_batch {fasta_path} results/ --num-models 5 --amber")


def describe_outputs():
    """Explain what files you'll get after running AlphaFold."""
    print("\n\n" + "=" * 70)
    print("OUTPUT FILES YOU'LL GET")
    print("=" * 70)
    
    outputs = {
        "ranked_0.pdb": "Best predicted structure (3D coordinates of all atoms)",
        "ranked_1.pdb": "Second-best structure (if multiple models run)",
        "*_plddt.png": "Chart showing confidence per residue (0-100 scale)",
        "*_pae.png": "Heatmap showing position uncertainty between residues",
        "ranking_debug.json": "Detailed scores for all model predictions",
    }
    
    print("\n📁 Files in results/ folder:")
    for filename, description in outputs.items():
        print(f"\n   {filename:25} → {description}")
    
    print("\n\n" + "=" * 70)
    print("HOW TO INTERPRET RESULTS")
    print("=" * 70)
    
    print("\n✅ GOOD PREDICTION:")
    print("   • pLDDT scores mostly > 90 (green in visualization)")
    print("   • PAE heatmap shows blue blocks")
    print("   • Structure looks compact and well-folded")
    
    print("\n⚠️  MODERATE PREDICTION:")
    print("   • pLDDT scores 70-90 (yellow/orange)")
    print("   • PAE shows some yellow/orange regions")
    print("   • Some parts may be flexible or uncertain")
    
    print("\n❌ LOW CONFIDENCE:")
    print("   • pLDDT scores < 70 (red)")
    print("   • PAE heatmap is red/orange")
    print("   • Likely disordered or insufficient data")
    
    print("\n💡 TIP: Focus on regions with pLDDT > 90 for reliable structure!")


def create_example_output_structure():
    """Create placeholder output directory so users know what to expect."""
    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)
    
    # Create README explaining what will be generated
    (output_dir / "README.txt").write_text(
        "This folder will contain AlphaFold 2 prediction outputs:\n\n"
        "After running ColabFold (which uses AlphaFold 2), you'll get:\n"
        "  - ranked_0.pdb            (Best 3D structure)\n"
        "  - demo_protein_plddt.png  (Confidence chart)\n"
        "  - demo_protein_pae.png    (Uncertainty heatmap)\n"
        "  - ranking_debug.json      (Detailed scores)\n"
    )
    
    print("\n\n📁 Created placeholder 'results/' folder")
    print("   (Run ColabFold to populate with actual predictions)")


def show_next_steps():
    """Provide guidance on what to do after getting predictions."""
    print("\n\n" + "=" * 70)
    print("NEXT STEPS")
    print("=" * 70)
    
    steps = [
        ("1️⃣  Run the prediction", "Use ColabFold (Option 1 or 2 above)"),
        ("2️⃣  Check confidence", "Look at pLDDT and PAE charts"),
        ("3️⃣  Visualize structure", "Open PDB file in PyMOL, ChimeraX, or online viewer"),
        ("4️⃣  Interpret results", "Focus on high-confidence regions (pLDDT > 90)"),
        ("5️⃣  Try your own", "Replace demo sequence with your protein of interest"),
    ]
    
    for step, description in steps:
        print(f"\n{step:25} {description}")
    
    print("\n\n🎓 LEARNING RESOURCES:")
    print("   • Diagram.md           → Visual flowcharts and AlphaFold 2 architecture")
    print("   • AlphaFold 2 paper    → https://www.nature.com/articles/s41586-021-03819-2")
    print("   • DeepMind GitHub      → https://github.com/deepmind/alphafold")
    print("   • Mol* viewer          → https://molstar.org/ (visualize PDB online)")


def main():
    """Main workflow demonstrating AlphaFold 2 usage."""
    
    # Demo protein sequence (small example)
    # This is from a real protein but shortened for demo purposes
    sequence = "MKFLKFSLLTAVLLSVVFAFSSCGDDDDTGYLPPSQAIQDLLKRMKV"
    protein_name = "demo_protein"
    
    print("\n🧬 AlphaFold 2 / ColabFold Quick Start")
    print("=" * 70)
    print("This script shows you how to predict protein 3D structures using AlphaFold 2.")
    print("No biology background needed!\n")
    
    # Step 1: Explain terminology
    explain_terminology()
    
    # Step 2: Create FASTA file
    fasta_path = create_fasta_file(sequence, protein_name)
    
    # Step 3: Show how to run ColabFold
    show_colabfold_options()
    
    # Step 4: Explain the command
    explain_command_flags(fasta_path)
    
    # Step 5: Describe expected outputs
    describe_outputs()
    
    # Step 6: Create example output structure
    create_example_output_structure()
    
    # Step 7: Next steps
    show_next_steps()
    
    print("\n\n" + "=" * 70)
    print("✅ Setup complete! You're ready to predict protein structures.")
    print("=" * 70)
    print("\n💡 Quick start: Try the Google Colab notebook (Option 1) first!")
    print("   It's the easiest way to get started with zero installation.\n")


if __name__ == "__main__":
    main()
