import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *

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
	pass
