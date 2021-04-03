# snpCounter.py

__author__ = "Christopher Korfmann"
__copyright__ = "Copyright (C) 2021 Christopher Korfmann"
__license__ = "Private"
__version__ = "1.1"


import re
import sys
defaultOutput = 'output.csv'   # define default output file

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

    def __init__(self, position, base, change):
        self.position = position                    # integer position of SNP
        self.base = base                            # expected base at the position

        # initialize counters for each type of substitution
        if base == 'A':
            self.AAcount = 0
            self.ACcount = 0
            self.AGcount = 0
            self.ATcount = 0

        if base == 'C':
            self.CCcount = 0
            self.CAcount = 0
            self.CGcount = 0
            self.CTcount = 0

        if base == 'G':
            self.GGcount = 0
            self.GCcount = 0
            self.GAcount = 0
            self.GTcount = 0

        if base == 'T':
            self.TTcount = 0
            self.TCcount = 0
            self.TGcount = 0
            self.TAcount = 0

        self.add(change)            # count first substitution
        snpList.total.append(self)  # add to list

    def add(self, change):   # counter function
        # increment substitution specific counter
        if self.base == 'A':
            if change == 'A':
                self.AAcount += 1
            if change == 'C':
                self.ACcount += 1
            if change == 'G':
                self.AGcount += 1
            if change == 'T':
                self.ATcount += 1

        if self.base == 'C':
            if change == 'C':
                self.CCcount += 1
            if change == 'G':
                self.CGcount += 1
            if change == 'A':
                self.CAcount += 1
            if change == 'T':
                self.CTcount += 1

        if self.base == 'G':
            if change == 'G':
                self.GGcount += 1
            if change == 'A':
                self.GAcount += 1
            if change == 'T':
                self.GTcount += 1
            if change == 'C':
                self.GCcount += 1

        if self.base == 'T':
            if change == 'T':
                self.TTcount += 1
            if change == 'A':
                self.TAcount += 1
            if change == 'G':
                self.TGcount += 1
            if change == 'C':
                self.TCcount += 1


# main function
with open(sys.argv[1], 'r') as f:                   # open input (.map) file

    for item in f.readlines():                      # begin reading each line
        # └--->splits current line into space separated tokens
        line = re.split(r'\t', item)
        # └--->finds the 'error' token at the end of current line (last string in each line from .map file)
        error = re.split(r'([, \n])', line[7])

        for snpToken in error:                      # └--->parse through current 'error' token and generate usable SNP token
            if snpToken == '' or snpToken == '\n':
                break
            if snpToken == ',':
                continue
            # └--->└---> generate tokens from current SNP token
            SNP = re.split('([:>])', snpToken)
            # └--->└---> capture actual position (not indexed position from .map) of SNP position and store in int, ie. SNP@63 will be snpPosition = 63
            snpPosition = int(SNP[0]) + 1
            # └--->└---> capture expected base
            base = SNP[2]
            # └--->└---> capture substituted base
            change = SNP[4]

            index = 0
            for snpElem in snpList.total:           # └--->└---> check if current position/base pair exists in the list
                # └--->└--->└---> if exists, increment substitution specific counter
                if snpElem.position == snpPosition and snpElem.base == base:
                    snpElem.add(change)
                    break
                index += 1
            # └--->└---> add position/base pair to list, if it doesn't exist
            if index == len(snpList.total):
                snpList(snpPosition, base, change)

f.close()   # close input file

# Save a reference to the original standard output
original_stdout = sys.stdout

with open(sys.argv[2], 'w') as o:      # open output file (sys.argv[2]) as writeable
    # Change the standard output to sys.argv[2]
    sys.stdout = o
    print('Position,Base,A,C,G,T')     # Print column names
    for result in snpList.total:       # print each position/base pair and its counter
        if result.base == 'A':
            print(str(result.position) + ',' + result.base + ',' + str(result.AAcount) + ',' +
                  str(result.ACcount) + ',' + str(result.AGcount) + ',' + str(result.ATcount))
        if result.base == 'C':
            print(str(result.position) + ',' + result.base + ',' + str(result.CAcount) + ',' +
                  str(result.CCcount) + ',' + str(result.CGcount) + ',' + str(result.CTcount))
        if result.base == 'G':
            print(str(result.position) + ',' + result.base + ',' + str(result.GAcount) + ',' +
                  str(result.GCcount) + ',' + str(result.GGcount) + ',' + str(result.GTcount))
        if result.base == 'T':
            print(str(result.position) + ',' + result.base + ',' + str(result.TAcount) + ',' +
                  str(result.TCcount) + ',' + str(result.TGcount) + ',' + str(result.TTcount))

    # Reset the standard output to its original value
    sys.stdout = original_stdout

o.close()   # close output file

print('>>> Output written to "' + sys.argv[2] + '"')


# author Christopher Korfmann
# copyright (C) Christopher Korfmann 2021
#
# beta program for evaluation and testing purposes only
