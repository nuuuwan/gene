import os

from gene.book.GeneBook import GeneBook


def main():
    GeneBook().write(os.path.join('book', 'gene.tex'))


if __name__ == '__main__':
    main()
