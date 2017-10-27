#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
import subprocess
import sys
#import errno
########
#Version 2
#Uli Zander 2017-07-27
#zander@embl.fr
#automatic MR model preparation:
#run the following way:
#MR_prepare.py NAME_OF_PDB
##
#The script will remove aniso records, alternative conformations (conformation A is kept)
#and set all Bfactors to 20.00 
#
########





def pdbFileAtomOnly(pdbfile):
###removes header, HETATM enties and 
    with open(pdbfile, 'r') as pdbfile:
        pdbfile = pdbfile.readlines()
    newPdb = []
    for line in pdbfile:
        if line.startswith('ATOM'):
           newPdb.append(line.rstrip())
    return newPdb


def pdbFileConfBfacCleanup(pdbfile):
    newpdb = []
#set occupancies to 1, Bfactors to 20
    for line in pdbfile:
        line = line[:56] + '1.00' + '  ' + '20.0' + ' ' + line[67:]
#check for alternative conformations, keep only A   
        if line[16] == ' ':
            newpdb.append(line)
        else:
            if line[16] == 'A':
                line = line[:16] + ' ' + line[17:]
                newpdb.append(line)
    return newpdb

try:
    pdbfile = sys.argv[1]
except IndexError:
    print('''
Please provide a pdb file as input:

MR_prepare.py YOUR_PDB_FILE
''')
    sys.exit(1)

pdbfile = pdbFileAtomOnly(pdbfile)
pdbfile = pdbFileConfBfacCleanup(pdbfile)

#for i in pdbfile:
#    print (i)
#newpdb = []
#for line in pdbfile:
#    line = line[:56] + '1.00' + '  ' + '20.0' + ' ' + line[67:]
#check for alternative conformations, keep only A   
#    if line[16] == ' ':
#        newpdb.append(line)
#    else:
#        if line[16] == 'A':
#            line = line[:15] + '  ' + line[17:]
#            newpdb.append(line)
#            newpdb.append(line)
        #############################
##does not work with del/pop, need to work with different list
#print (len(newpdb)) 
#print (newpdb)      
#for line in   newpdb:     
#    print (line)        
print(
'''
*************************************************************
This script can be used to prepare a MR model from a pdb file.
It will apply the following changes:

-remove aniso records
-remove alternative conformations (conformation A is kept)
-change all occupancies to 1.00
-change all B-factors to 20.00

It generates an output file called 'SEARCHMODEL.pdb'

(\/)(@@)(\/)

*************************************************************
''')
with open('SEARCHMODEL.pdb', 'w') as outputfile:
    for line in pdbfile:
        print (line, file=outputfile)
