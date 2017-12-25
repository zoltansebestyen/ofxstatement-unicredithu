#!/usr/bin/env python3
"""Command line tool flatten XML file to better understand
what keys it contains
"""
# import xml.etree.ElementTree as ET
import sys
from lxml import etree
import re

def print_tag(path, elem):
    for child in elem.iterchildren("*"):
        child_tag = child.tag
        p = re.match('\{[^}]+\}(.*)$', child_tag)
        if p is not None:
            child_tag = p.group(1)

        child_path = '/'.join((path, child_tag))
        if child.text is not None and child.text.strip() != '':
            print("%s: %s" % (child_path, str(child.text)))
        print_tag(child_path, child)

filename = sys.argv[1]
tree = etree.parse(filename)
print_tag('', tree.getroot())
