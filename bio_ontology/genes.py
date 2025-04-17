from pyensembl import EnsemblRelease
import gget
from functools import lru_cache
ensembls = {}
@lru_cache(maxsize=10000)
def get_gene_by_name(gene_name: str, species: str = "human") -> dict | None:
    """
    Get the gene by name.
    """
    if species not in ensembls:
        ensembls[species] = EnsemblRelease(species=species)
    release = ensembls[species]
    try:
        rs=  release.genes_by_name(gene_name)
        if len(rs) == 0:
            return None
        else:
            return rs[0].to_dict()
    except Exception as e:
        return None


@lru_cache(maxsize=10000)
def get_gene_by_id(gene_id: str, species: str = "human") -> dict | None:
    """
    Get the gene by id.
    """
    if species not in ensembls:
        ensembls[species] = EnsemblRelease(species=species)
    release = ensembls[species]
    try:
        return release.gene_by_id(gene_id).to_dict()
    except Exception as e:
        return None

@lru_cache(maxsize=1000)
def get_gene_sequence(ens_ids: list[str]|str, translate: bool = False) -> str | None:
    """
    Get the gene sequence.
    """
    try:
        return gget.seq(ens_ids, translate=translate)
    except Exception as e:
        return None


if __name__ == "__main__":
    print(get_gene_by_name("TSPAN6"))
    print(get_gene_by_name("TSPAN-6"))
    print(get_gene_by_name("T245"))
