# bio_ontology
------------
A Python package for working with biological ontologies and gene information.

## Installation

```bash
uv sync

# Initialize the environment
# go to https://lamin.ai/ to register an account and get api key
lamin login
lamin connect
lamin init --storage lamin-data --modules bionty
lamin settings

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

## Examples

### Finding Gene Information

```python
# Get TP53 gene information
gene = get_gene_by_name("TP53")
print(f"""
Gene Information:
- ID: {gene['gene_id']}
- Name: {gene['gene_name']}
- Chromosome: {gene['contig']}
- Start: {gene['start']}
- End: {gene['end']}
""")

# Get gene sequence
sequence = get_gene_sequence(gene['gene_id'])
print(f"Sequence length: {len(sequence)}")
```

### Working with Ontologies

```python
# Get cell type information
cell_type = get_cell_type_ontology("T cell")
print(f"""
Cell Type Information:
- ID: {cell_type['ontology_id']}
- Name: {cell_type['name']}
- Description: {cell_type.get('description', 'N/A')}
""")

# Get development stage for different ages
ages = [0, 1, 5, 15, 30, 70]
for age in ages:
    stage = get_development_stage_by_age(age)
    print(f"Age {age}: {stage['label']}")
```

### Cross-species Analysis

```python
# Compare human and mouse TP53
human_gene = get_gene_by_name("TP53")
mouse_gene = get_gene_by_name("Tp53", species="mouse")

print(f"""
Gene Comparison:
Human TP53:
- ID: {human_gene['gene_id']}
- Length: {human_gene['end'] - human_gene['start']}

Mouse Tp53:
- ID: {mouse_gene['gene_id']}
- Length: {mouse_gene['end'] - mouse_gene['start']}
""")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
