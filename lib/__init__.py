import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *
from difflib import SequenceMatcher

__all__ = ['bibparser', 'diff', 'substract', 'merge']


def customize_parser(bibrec):
	"""Customize the bibtex parser

    :param bibrec: a bibtex record
    :returns: -- customized record
    """
    record = type(record) # lower case for entry type
    record = author(record) # author to list of "Name, Surname"
    record = editor(record) # editorid, editor name
    record = journal(record)
    record = link(record)
    record = page_double_hyphen(record) # harmonize page rec
    record = doi(record) # doi
    record = homogenize_latex_encoding(record) # char encoding
    return record


def bibparser(infile):
	bib_db = None
	bparser = BibTexParser()
    bparser.customization = customize_parser
	with open(infile) as bibtex:
		bib_db = bibtexparser.load(bibtex, parser=bparser)
	return bib_db


def diff(bibdb1, bibdb2):
	"""Return the symmetric difference between bibdb1 and bibdb2

    :param bibdb1: first bib record
    :param bibdb2: second bib record
    :return: a bibliographic database containing the symmetric differences
    :rtype: BibDatabase    
    """
    pass


def compare(entry1, entry2):
    """Compare two bibtex entries
    Return 0 if the two entry are different, 
    2 if they are similar and 1 if they are truly identical

    :param entry1: first bibtex entry
    :type: dict
    :param entry2: second bibtex record
    :type: dict
    :returns: -- the comparison result
    :rtype: int    
    """    
    if entry1['ID'] == entry2['ID'] and entry1['title'] == entry2['title']:
        return 1
    else:
        s = SequenceMatcher(lambda x: x in "-;,. \t", entry1['title'], entry2['title'])
        r = s.quick_ratio()
        # if title are similar:
        if r >= 0.95:
            for 

        return 0


def substract(bibdb1, bibdb2):
	"""Return the difference between bibdb1 and bibdb2
    
    :param bibdb1: parent bib record
	:type: BibDatabase
    :param bibdb2: second bib record
	:type: BibDatabase
    :returns: -- the bibliographic database corresponding to bibdb1 - bibdb2
	:rtype: BibDatabase    
    """
    pass
    


def merge(bibdb1, bibdb2):
	"""Merge bibdb2 into bibdb1 database

    :param bibdb1: first bib record
	:type: BibDatabase
    :param bibdb2: second bib record
	:type: BibDatabase
    :return: merged database -- mapping
    :rtype: BibDatabase -- dict
    """
    for ent1 in bibdb1.entries:
        for ent2 in bibdb2.entries:
            if ent1 == ent2:
                pass

