# -*- coding: utf-8 -*-
"""
   Usage: setprojid.py <product> <projectid>
"""

from __future__ import print_function
from utils import getPoFiles, getLongProductName
import os, sys

from i18ndude import catalog


def main():
    if len(sys.argv) < 3:
        print('You have to specify the product and the new text for projectid.')
        sys.exit(1)

    product = getLongProductName(sys.argv[1])
    projectid = sys.argv[2]

    os.chdir('..')
    os.chdir('i18n')

    poFiles = getPoFiles(product, all=True)
    if poFiles == []:
        print('No po-files were found for the given product.')
        sys.exit(2)

    for poFile in poFiles:
        try:
            po_ctl = catalog.MessageCatalog(filename=poFile)
        except IOError as e:
            print('I/O Error: %s' % e, file=sys.stderr)
        po_ctl.mime_header['Project-Id-Version'] = projectid
        file = open(poFile, 'w')
        writer = catalog.POWriter(file, po_ctl)
        writer.write(sort=False)

if __name__ == '__main__':
    main()
