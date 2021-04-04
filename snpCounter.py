# snpCounter.py

__author__ = "Christopher Korfmann"
__copyright__ = "Copyright (c) 2021, Christopher Korfmann"
__license__ = "BSD 3-Clause License"
__version__ = "1.2"


import re, sys
defaultOutput = 'output.csv'  # define default output file

# check for number of input arguments
if len(sys.argv) < 2:
    sys.exit(">>> Need an input file. First input argument should contain the directory to a valid .map file.\n>>> Example: snpCounter.py genome.map")
if len(sys.argv) < 3:
    confirm = input(
        ">>> Warning, will overwrite any file in the current directory called 'output.csv'. Continue? (y/n)\n>>> ")
    if confirm.lower() != 'y':
        sys.exit(">>> No output. Exited successfully...")
    sys.argv.append(defaultOutput)  # set output to default ('output.csv')


class snpList:
    total = []  # list of all unique substitutions

    def __init__(self, position, base, substitution):
        self.position = position  # integer position of SNP
        self.base = base          # expected base at the position

        # initialize counters for each type of substitution
        if base == 'A':
            self.ACcount = 0
            self.AGcount = 0
            self.ATcount = 0

        if base == 'C':
            self.CAcount = 0
            self.CGcount = 0
            self.CTcount = 0

        if base == 'G':
            self.GCcount = 0
            self.GAcount = 0
            self.GTcount = 0

        if base == 'T':
            self.TCcount = 0
            self.TGcount = 0
            self.TAcount = 0

        self.add(substitution)      # count first substitution
        snpList.total.append(self)  # add to list

    def add(self, substitution):    # counter function
        # increment substitution specific counter
        if self.base == 'A':
            if substitution == 'C':
                self.ACcount += 1
            if substitution == 'G':
                self.AGcount += 1
            if substitution == 'T':
                self.ATcount += 1

        if self.base == 'C':
            if substitution == 'G':
                self.CGcount += 1
            if substitution == 'A':
                self.CAcount += 1
            if substitution == 'T':
                self.CTcount += 1

        if self.base == 'G':
            if substitution == 'A':
                self.GAcount += 1
            if substitution == 'T':
                self.GTcount += 1
            if substitution == 'C':
                self.GCcount += 1

        if self.base == 'T':
            if substitution == 'A':
                self.TAcount += 1
            if substitution == 'G':
                self.TGcount += 1
            if substitution == 'C':
                self.TCcount += 1


# main function
lineCount = 0
with open(sys.argv[1], 'r') as f:   # open input (.map) file

    for item in f.readlines():      # begin reading each line
        # └--->split current line into space separated tokens
        line = re.split(r'\t', item)
        if len(line) == 8:
            lineCount += 1
        # └--->find the SNP string token at the end of current line (last space separated string in each line of .map file)
        snpString = re.split(r'([, \n])', line[7])

        for snpToken in snpString:   # └--->parse through current SNP string token and generate usable unique SNP token
            if snpToken == '' or snpToken == '\n':
                break
            if snpToken == ',':
                continue
            # └--->└---> generate position, base, and substitution tokens from current SNP token
            SNP = re.split('([:>])', snpToken)
            # └--->└---> capture actual position (not zero-based indexed position from .map) of SNP, ie. 62:A>G will be snpPosition = 63
            snpPosition = int(SNP[0]) + 1
            # └--->└---> capture expected base
            base = SNP[2]
            # └--->└---> capture substituted base
            substitution = SNP[4]

            index = 0
            for snpElem in snpList.total:   # └--->└---> check if current position/base pair exists in the list
                # └--->└--->└---> if exists, increment substitution specific counter
                if snpElem.position == snpPosition and snpElem.base == base:
                    snpElem.add(substitution)
                    break
                index += 1
            # └--->└---> add position/base pair to list, if it doesn't exist
            if index == len(snpList.total):
                snpList(snpPosition, base, substitution)

f.close()   # close input file

# Save a reference to the original standard output
original_stdout = sys.stdout

with open(sys.argv[2], 'w') as o:      # open output file (sys.argv[2]) as writeable
    # Change the standard output to sys.argv[2]
    sys.stdout = o
    print('Position,Base,A,C,G,T')     # Print column names
    for final in snpList.total:        # print each position/base pair and its counter
        if final.base == 'A':
            print(str(final.position) + ',' + final.base + ',' + str(lineCount - (final.ACcount + final.AGcount + final.ATcount)) + ',' +
                  str(final.ACcount) + ',' + str(final.AGcount) + ',' + str(final.ATcount))
        if final.base == 'C':
            print(str(final.position) + ',' + final.base + ',' + str(final.CAcount) + ',' +
                  str(lineCount - (final.CAcount + final.CGcount + final.CTcount)) + ',' + str(final.CGcount) + ',' + str(final.CTcount))
        if final.base == 'G':
            print(str(final.position) + ',' + final.base + ',' + str(final.GAcount) + ',' +
                  str(final.GCcount) + ',' + str(lineCount - (final.GCcount + final.GAcount + final.GTcount)) + ',' + str(final.GTcount))
        if final.base == 'T':
            print(str(final.position) + ',' + final.base + ',' + str(final.TAcount) + ',' +
                  str(final.TCcount) + ',' + str(final.TGcount) + ',' + str(lineCount - (final.TCcount + final.TGcount + final.TAcount)))

    # Reset the standard output to its original value
    sys.stdout = original_stdout

o.close()   # close output file

print('>>> Output written to "' + sys.argv[2] + '"')


# Author: Christopher Korfmann
# Copyright (c) 2021, Christopher Korfmann
# All rights reserved
