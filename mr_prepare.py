from __future__ import print_function
from __future__ import division
import subprocess
import sys


def pdbFileAtomOnly(pdbfile):
'''loads a pdb file and removes al lines that do not start with ATOM'''
    with open(pdbfilepdbFileAtomOnlyle:
        pdbfile = pdbfile.readlines()
    newPdb = []
    for line in pdbfile:
        if line.startswith('ATOM'):
            line = line[:56] + '1.00' + '  ' + '20.0' + ' ' + line[67:]
            if line[16] == 'A':
                line = line[:16] + ' ' + line[17:]
            newPdb.append(line.rstrip())
    with open('SEARCHMODEL.pdb', 'w') as outputfile:
        for line in newPdb:
            print (line, file=outputfile)
    
    
def main():
    """Main entry point for the script."""
    try:
        pdbfile = sys.argv[1]
    except IndexError:
        print('''
    Please provide a pdb file as input:

    MR_prepare.py YOUR_PDB_FILE
    ''')
        sys.exit(1)
    pdbFileAtomOnly(pdbfile)
    
if __name__ == '__main__':
    sys.exit(main())
    
