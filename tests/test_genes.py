import pytest
from bio_ontology.genes import get_gene_by_name, get_gene_by_id, get_gene_sequence


def test_get_gene_by_name():
    # Test with a known human gene
    gene = get_gene_by_name("TP53")
    assert gene is not None
    assert "gene_id" in gene
    assert gene["gene_id"].startswith("ENSG")
    assert gene["gene_name"] == "TP53"

    # Test with a non-existent gene
    gene = get_gene_by_name("NONEXISTENTGENE")
    assert gene is None

    # Test with different species
    gene = get_gene_by_name("Tp53", species="mouse")
    assert gene is not None
    assert gene["gene_id"].startswith("ENSMUSG")


def test_get_gene_by_id():
    # Test with a known human gene ID
    gene = get_gene_by_id("ENSG00000141510")  # TP53 gene ID
    assert gene is not None
    assert gene["gene_id"] == "ENSG00000141510"
    assert gene["gene_name"] == "TP53"

    # Test with a non-existent gene ID
    gene = get_gene_by_id("ENSG00000000000")
    assert gene is None

    # Test with different species
    gene = get_gene_by_id("ENSMUSG00000059552", species="mouse")  # Mouse Tp53 gene ID
    assert gene is not None
    assert gene["gene_id"] == "ENSMUSG00000059552"


def test_get_gene_sequence():
    # Test with a single gene ID
    sequence = get_gene_sequence("ENSG00000141510")  # TP53 gene ID
    assert sequence is not None
    assert isinstance(sequence, str)
    assert len(sequence) > 0

    # Test with multiple gene IDs
    sequences = get_gene_sequence(["ENSG00000141510", "ENSG00000141510"])
    assert sequences is not None
    assert isinstance(sequences, str)
    assert len(sequences) > 0

    # Test with translation
    protein_sequence = get_gene_sequence("ENSG00000141510", translate=True)
    assert protein_sequence is not None
    assert isinstance(protein_sequence, str)
    assert len(protein_sequence) > 0
    assert all(c in "ACDEFGHIKLMNPQRSTVWY" for c in protein_sequence)  # Check if it's a protein sequence 