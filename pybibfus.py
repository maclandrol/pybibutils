#!/usr/bin/env python
from lib import *
import argparse
import os


def main():
    args = parse_args()

def print_diff(db1, db2, sides=False, color=False):
    pass

def harmonize(bibdb1, bibdb2, ltxlist, outdir="", suffix=""):
    """Merge two bib database into a single one

    :param bibdb1: first bib record
    :type: BibDatabase
    :param bibdb2: second bib record
    :type: BibDatabase
    :param ltxlist: list of latex files
    :type: file
    :return: a list of path to the new latex files
    """
    merged_db, kdict = merge(bibdb1, bibdb2)
    pass


def parse_args():

    parser = ArgumentParser(add_help=False)
    sub_parser = parser.add_subparsers(help="List of available options")

    # diff parser
    diff_parser = sub_parser.add_parser('diff', help="Show differences between two bibtex files")
    diff_parser.add_argument('--side-by-side', '-y', dest="side",  action="store_true", default=False, help="Output differences side by side. By default it will produce a ndiff format.")
    diff_parser.add_argument("--color", dest='color', action="store_true", help='Use color in output (default false). Note that it will not always work')

    # subtract parser
    subtract_parser = sub_parser.add_parser('subtract', help="Show entries in one bibtex file but not the second")
    
    # merge parser
    merge_parser = sub_parser.add_parser('merge', help="Merge two bibtex files into a single one with distinct entries")
    
    # harmonize parser
    harmonize_parser = sub_parser.add_parser('harmonize', help="Merge two bibtex files and use the new unique tag in the provided latex files.")
    harmonize_parser.add_argument('latexfiles', metavar='.tex', nargs='+', help="List of latex files")

    parser.add_argument('bibfiles', metavar=('.bib1', '.bib2'), nargs=2, help="List of .bib files")
    parser.add_argument('--output', '-o', dest='output', help="Output file")
    parser.add_argument('--outdir', '--wdir', '-d', dest='outdir', help="Output folder")
    parser.add_argument('-i', '--ignore_tag', dest='ignoretag', action="store_true", help="Do not rely only on tag when comparing bibliography entries")

    args = parser.parse_args()

if __name__ == '__main__':
    main()