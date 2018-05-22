#!/usr/bin/env python
from lib import *
import argparse
import os
import time
import sys
import collections
import difflib
import fcntl
import termios
import struct
import re

class color:
    #SUB = '\033[95m'
    #WARNING = '\033[93m'
    ADD = '\033[94m'
    DEL = '\033[91m'
    SUB = '\033[92m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    from colorama import init, Back, Style
    init()
    color.DEL = Back.RED  # .YELLOW # red
    color.ADD = Back.BLUE  # .CYAN # blue
    color.SUB = Back.GREEN
    # color.END = Back.RESET#.RESET_ALL

except ImportError:
    pass

pt = re.compile('(\\\cite.{,12})(\{[^\}\{]+\})')

def terminal_size():
    h, w, hp, wp = struct.unpack('HHHH', fcntl.ioctl(
        0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
    return w, h


def getdiff(seq1list, seq2list, args, file1=file1, file2=file2, header=False):

    diff = ""
    if args.side:
        w, _ = terminal_size()
        numline = None
        if args.context:
            numline = args.lines
        diffs = difflib._mdiff(seq1list, seq2list, numline)
        width = int(w / 2.4) - 2
        if header:
            print(('\n{lside:{width}}{flag:^5}{rside:{width}}').format(
                lside=file1, rside=file2, width=width, flag=" "))

            # print(('\n{:%d.%d}{}{:%d.%d}' %
            #       (width, width, width, width)).format(file1, file2))
        for fl, tl, flag in diffs:
            flag = "!" if flag else " "

            if fl and tl:
                lside = str(fl[-1]).strip().replace('\0',
                                                    "|").replace('\1', "|").replace("\n", "")
                rside = str(tl[-1]).strip().replace('\0',
                                                    "|").replace('\1', "|").replace("\n", "")
                if args.color:
                    lside = lside.replace(
                        '|+', color.ADD).replace('|-', color.DEL).replace('|^', color.SUB).replace('|', color.END)
                    rside = rside.replace(
                        '|+', color.ADD).replace('|-', color.DEL).replace('|^', color.SUB).replace('|', color.END)

                if lside or rside:
                    line2 = ('{lside:{width}}{flag:^5}{rside:{width}}').format(
                        lside=lside, rside=rside, width=width, flag=flag)
                    print(line2)

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
    for ltx in ltxlist:
        with open(ltx) as INLATEX:
            bsname = os.path.basename(ltx)
            out = os.path.join(outdir, bsname+suffix)
            with open(out, 'w') as OUTLATEX:
                txt = ltx.read()
                cor_txt = txt
                for m1, m2 in pt.findall(txt):
                    mm2 = m2.strip('}').strip('{').split(',')
                    mm2 = [kdict.get(x.strip(), x) for x in mm2]
                    cor_txt = cor_txt.replace(m1+m2, m1+"{"+",".join(mm2)+"}")
                OUTLATEX.write(cor_txt)


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
    harmonize_parser.add_argument('--suffix', '--sfx', dest='suffix',  default="", help="Suffix to add to corrected latex files")

    parser.add_argument('bibfiles', metavar=('.bib1', '.bib2'), nargs=2, help="List of .bib files")
    parser.add_argument('--output', '-o', dest='output', help="Output file")
    parser.add_argument('--outdir', '--wdir', '-d', dest='outdir', help="Output folder")
    parser.add_argument('-i', '--ignore_tag', dest='ignoretag', action="store_true", help="Do not rely only on tag when comparing bibliography entries")

    args = parser.parse_args()

if __name__ == '__main__':
    main()