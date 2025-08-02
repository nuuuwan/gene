from gene.console.GeneConsole import GeneConsole
from gene.core.gene_dir.gene_dir_helpers import get_gene_dir

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        gene_dir = sys.argv[1]
    else:
        gene_dir = get_gene_dir()

    GeneConsole(gene_dir).run()
