import pytest
from bio_ontology.ontologies import (
    get_cell_type_ontology,
    get_tissue_ontology,
    get_disease_ontology,
    get_human_development_stage_ontology,
    get_development_stage_by_age,
    get_ontology_by_id
)


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


def test_get_tissue_ontology():
    # Test with a known tissue
    result = get_tissue_ontology("lung")
    assert result is not None
    assert isinstance(result, dict)
    assert "ontology_id" in result
    assert result["ontology_id"].startswith("UBERON:")

    # Test with a non-existent tissue
    result = get_tissue_ontology("NonExistentTissue")
    assert result is None


def test_get_disease_ontology():
    # Test with a known disease
    result = get_disease_ontology("lung cancer")
    assert result is not None
    assert isinstance(result, dict)
    assert "ontology_id" in result
    assert result["ontology_id"].startswith(("DOID:", "EFO:"))

    # Test with a non-existent disease
    result = get_disease_ontology("NonExistentDisease")
    assert result is None


def test_get_human_development_stage_ontology():
    # Test with a known development stage
    result = get_human_development_stage_ontology("embryonic")
    assert result is not None
    assert isinstance(result, dict)
    assert "ontology_id" in result
    assert result["ontology_id"].startswith("HsapDv:")

    # Test with a non-existent stage
    result = get_human_development_stage_ontology("NonExistentStage")
    assert result is None


def test_get_development_stage_by_age():
    # Test with various ages
    test_cases = [
        (0, "newborn stage"),
        (0.1, "infant stage"),
        (1, "infant stage"),
        (3, "2-5 year-old child stage"),
        (4, "2-5 year-old child stage"),
        (6, "6-12 year-old child stage"),
        (10, "6-12 year-old child stage"),
        (13, "adolescent stage"),
        (17, "adolescent stage"),
        (20, "adult stage"),
        (50, "adult stage"),
        (70, "aged stage"),
    ]
    
    for age, expected_stage in test_cases:
        result = get_development_stage_by_age(age)
        assert result is not None
        assert isinstance(result, dict)
        assert result["label"] == expected_stage
        assert result["id"].startswith("HsapDv:")

    # Test with negative age
    result = get_development_stage_by_age(-1)
    assert result is not None
    assert result["label"] == "newborn stage"


def test_get_ontology_by_id():
    # Test with different types of ontology IDs
    test_cases = [
        ("CL:0000084", "T cell"),  # cell type
        ("UBERON:0002048", "lung"),  # tissue
        ("DOID:1324", "lung cancer"),  # disease
        ("HsapDv:0000087", "adult stage"),  # development stage
    ]
    
    for ontology_id, expected_name in test_cases:
        result = get_ontology_by_id(ontology_id)
        assert result is not None
        assert isinstance(result, dict)
        assert "name" in result
        assert expected_name.lower() in result["name"].lower()

    # Test with invalid ontology ID
    with pytest.raises(ValueError):
        get_ontology_by_id("INVALID:123") 