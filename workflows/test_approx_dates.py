import os

from gene.core.gene_dir.GeneDir import GeneDir

GENE_DIR = os.path.join('data', 'real-data', 'gene.20230828')

if __name__ == '__main__':
    gene = GeneDir.load(GENE_DIR)
    me = gene['00000759']
    print(me)
    for bya in me.get_birth_year_approx_list():
        print(bya)
    print(me.birth_year_approx)
