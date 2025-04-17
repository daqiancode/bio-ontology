# bio_ontology

A Python package for working with biological ontologies and gene information.

## Installation

```bash
git clone https://github.com/daqiancode/bio-ontology.git
cd bio-ontology
# uv should be installed
uv venv
source .venv/bin/activate
uv sync

# Initialize the environment
# go to https://lamin.ai/ to register an account and get api key
# uv pip install lamindb
lamin login
lamin init --storage lamin-data --modules bionty
lamin connect lamin-data
lamin settings

# numpy version should be less than 2 if confliction occurs
uv pip install "numpy<2" 

# Install dependencies
uv pip install setuptools
pyensembl install --release 111 --species homo_sapiens
```

## Usage

### Gene Information

```python
from bio_ontology.genes import get_gene_by_name, get_gene_by_id, get_gene_sequence

# Get gene information by name
gene = get_gene_by_name("TP53")
print(f"Gene ID: {gene['gene_id']}")
print(f"Gene Name: {gene['gene_name']}")

# Get gene information by ID
gene = get_gene_by_id("ENSG00000141510")
print(f"Gene Name: {gene['gene_name']}")

# Get gene sequence
sequence = get_gene_sequence("ENSG00000141510")
print(f"Sequence length: {len(sequence)}")

# Get protein sequence
protein = get_gene_sequence("ENSG00000141510", translate=True)
print(f"Protein sequence: {protein}")

# Work with different species
mouse_gene = get_gene_by_name("Tp53", species="mouse")
print(f"Mouse gene ID: {mouse_gene['gene_id']}")
```

### Ontology Information

```python
from bio_ontology.ontologies import (
    get_cell_type_ontology,
    get_tissue_ontology,
    get_disease_ontology,
    get_human_development_stage_ontology,
    get_development_stage_by_age,
    get_ontology_by_id
)

# Get cell type ontology
cell_type = get_cell_type_ontology("T cell")
print(f"Cell type ID: {cell_type['ontology_id']}")
print(f"Cell type name: {cell_type['name']}")

# Get tissue ontology
tissue = get_tissue_ontology("lung")
print(f"Tissue ID: {tissue['ontology_id']}")
print(f"Tissue name: {tissue['name']}")

# Get disease ontology
disease = get_disease_ontology("lung cancer")
print(f"Disease ID: {disease['ontology_id']}")
print(f"Disease name: {disease['name']}")

# Get human development stage
stage = get_human_development_stage_ontology("embryonic")
print(f"Stage ID: {stage['ontology_id']}")
print(f"Stage name: {stage['name']}")

# Get development stage by age
age_stage = get_development_stage_by_age(25)
print(f"Age 25 stage: {age_stage['label']}")

# Get ontology by ID
ontology = get_ontology_by_id("CL:0000084")  # T cell
print(f"Ontology name: {ontology['name']}")
```

## Testing

The package includes comprehensive test cases to ensure functionality. Here's how to run and write tests:

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_genes.py
pytest tests/test_ontologies.py

# Run with verbose output
pytest -v tests/

# Run with coverage report
pytest --cov=bio_ontology tests/
```

### Test Examples

#### Gene Tests

```python
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
```

#### Ontology Tests

```python
def test_get_cell_type_ontology():
    # Test with a known cell type
    result = get_cell_type_ontology("T cell")
    assert result is not None
    assert isinstance(result, dict)
    assert "ontology_id" in result
    assert result["ontology_id"].startswith("CL:")

    # Test with a non-existent cell type
    result = get_cell_type_ontology("NonExistentCellType")
    assert result is None

def test_get_development_stage_by_age():
    # Test with various ages
    test_cases = [
        (0, "newborn stage"),
        (0.1, "infant stage"),
        (1, "infant stage"),
        (3, "2-5 year-old child stage"),
        (6, "6-12 year-old child stage"),
        (13, "adolescent stage"),
        (20, "adult stage"),
        (70, "aged stage"),
    ]
    
    for age, expected_stage in test_cases:
        result = get_development_stage_by_age(age)
        assert result is not None
        assert isinstance(result, dict)
        assert result["name"] == expected_stage
        assert result["ontology_id"].startswith("HsapDv:")
```

### Writing New Tests

When adding new functionality, follow these guidelines for writing tests:

1. Create a new test file in the `tests/` directory
2. Import the necessary functions from the package
3. Write test functions with descriptive names
4. Include both positive and negative test cases
5. Test edge cases and error conditions
6. Use assertions to verify expected behavior

Example of a new test file:

```python
# tests/test_new_feature.py
import pytest
from bio_ontology.new_feature import new_function

def test_new_function():
    # Positive test case
    result = new_function("valid_input")
    assert result is not None
    assert isinstance(result, dict)
    assert "expected_key" in result

    # Negative test case
    result = new_function("invalid_input")
    assert result is None

    # Edge case
    result = new_function("")
    assert result is None
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
