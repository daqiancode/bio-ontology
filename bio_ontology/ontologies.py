import bionty as bt
import pandas as pd
from functools import lru_cache

# process output of search results
def process_search_results(results: pd.DataFrame) -> dict | None:
    if len(results) == 0:
        return None
    result = results.reset_index().iloc[0].to_dict()
    if 'parents' in result: # convert parents from numpy array to list
        result['parents'] = result['parents'].tolist()
    return result

def get_organism_ontology(organism: str) -> dict | None:
    """
    Get the organism ontology from the organism name.
    """
    organisms = bt.Organism.public(organism="vertebrates").search(organism, limit=1)
    return process_search_results(organisms)

@lru_cache(maxsize=1000)
def get_cell_type_ontology(cell_type: str) -> str | None:
    """
    Get the cell type ontology from the cell type name.
    """
    results = bt.CellType.public(organism="all").search(cell_type, limit=1)
    return process_search_results(results)

@lru_cache(maxsize=1000)
def get_tissue_ontology(tissue: str) -> dict | None:
    """
    Get the tissue ontology from the tissue name.
    """
    tissues = bt.Tissue.public(organism="all").search(tissue, limit=1)
    return process_search_results(tissues)

@lru_cache(maxsize=1000)
def get_disease_ontology(disease: str) -> dict | None:
    """
    Get the disease ontology from the disease name.
    """
    diseases = bt.Disease.public(organism="all").search(disease, limit=1)
    return process_search_results(diseases)

@lru_cache(maxsize=1000)
def get_human_development_stage_ontology(stage: str) -> dict | None:
    """
    Get the human development stage ontology from the stage name.
    """
    stages = bt.DevelopmentalStage.public(organism="human").search(stage, limit=1)
    return process_search_results(stages)

def get_development_stage_by_age(age):
    """
    Return HsapDv developmental stage term (ID and label) based on human age in years.
    If age < 0, it's treated as prenatal (fetal stage and its sub-stages).
    """
    hsapdv_terms = [
        {"id": "HsapDv:0000082", "label": "newborn stage", "range": (0, 0.1)},
        {"id": "HsapDv:0000083", "label": "infant stage", "range": (0.1, 2)},
        {"id": "HsapDv:0000084", "label": "2-5 year-old child stage", "range": (2, 5)},
        {"id": "HsapDv:0000085", "label": "6-12 year-old child stage", "range": (5, 12)},
        {"id": "HsapDv:0000086", "label": "adolescent stage", "range": (12, 18)},
        {"id": "HsapDv:0000087", "label": "adult stage", "range": (18, 65)},
        {"id": "HsapDv:0000093", "label": "aged stage", "range": (65, float("inf"))},
    ]

    for term in hsapdv_terms[1:]:
        start, end = term["range"]
        if start < age <= end or (start < 0 and end == 0 and age < 0):
            return {"id": term["id"], "label": term["label"]}
    
    return {"id": hsapdv_terms[0]["id"], "label": hsapdv_terms[0]["label"]}


@lru_cache(maxsize=1000)
def get_ethnicity_ontology(ethnicity: str) -> dict | None:
    """
    Get the ethnicity ontology from the ethnicity name.
    """
    ethnicities = bt.Ethnicity.public(organism="human").search(ethnicity, limit=1)
    return process_search_results(ethnicities)

@lru_cache(maxsize=1000)
def get_cell_line_ontology(cell_line: str) -> dict | None:
    """
    Get the cell line ontology from the cell line name.
    """
    cell_lines = bt.CellLine.public(organism="all").search(cell_line, limit=1)
    return process_search_results(cell_lines)

@lru_cache(maxsize=10000)
def get_gene_ontology(gene_name: str , organism: str = "human") -> dict | None:
    """
    Get the gene ontology from the gene name.
    """
    genes = bt.Gene.public(organism=organism).search(gene_name, limit=1)
    return process_search_results(genes)

@lru_cache(maxsize=10000)
def get_protein_ontology(protein_name: str , organism: str = "human") -> dict | None:
    """
    Get the protein ontology from the protein name.
    """
    proteins = bt.Protein.public(organism=organism).search(protein_name, limit=1)
    return process_search_results(proteins)

@lru_cache(maxsize=1000)
def get_ontology_by_id(ontology_id: str) -> dict | None:
    """
    Get the ontology from the ontology id.
    """
    if ontology_id.startswith("CL:"):
        return bt.CellType.public(organism="all").df().loc[ontology_id].to_dict()
    elif ontology_id.startswith("UBERON:"):
        return bt.Tissue.public(organism="all").df().loc[ontology_id].to_dict()
    elif ontology_id.startswith("MONDO:"):
        return bt.Disease.public(organism="all").df().loc[ontology_id].to_dict()
    elif ontology_id.startswith("HP:"):
        return bt.Phenotype.public(organism="all").df().loc[ontology_id].to_dict()
    elif ontology_id.startswith("HsapDv:"):
        return bt.DevelopmentalStage.public(organism="human").df().loc[ontology_id].to_dict()
    elif ontology_id.startswith("HANCESTRO:"):
        return bt.Ethnicity.public(organism="human").df().loc[ontology_id].to_dict()
    elif ontology_id.startswith("CLO:"):
        return bt.CellLine.public(organism="all").df().loc[ontology_id].to_dict()
    else:
        raise ValueError(f"Unknown ontology id: {ontology_id}")
        
