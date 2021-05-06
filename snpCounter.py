# snpCounter.py

#!/usr/bin/python3

__author__ = "Christopher Korfmann"
__copyright__ = "Copyright (c) 2021, Christopher Korfmann"
__license__ = "GPL-3.0-only"
__version__ = "1.3"

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import re
import sys

defaultOutput = 'output.csv'  # define default output file


if len(sys.argv) < 2:
    sys.exit(">>> Error - Need an input file. First input argument should contain the directory to a valid .map file.\n>>> Example: snpCounter.py genome.map\n>>> Enter 'snpCounter.py help' for more information")
if len(sys.argv) == 3:
    confirm = input(
        ">>> Warning, will overwrite any file in the current directory called \n    '" + sys.argv[2] + "'\n>>> Continue? (y/n)\n>>> ")
    if confirm.lower() != 'y':
        sys.exit(">>> No output written. Exited successfully...")
if len(sys.argv) < 3:
    if (sys.argv[1].lower() == "help"):
        sys.exit("\n############\nUsage: snpCounter.py <input file> <output file>\n############\nInput File: valid .map file\nOutput File: (OPTIONAL) Comma separated text list with headers, containing count of unique SNP's\n  at specific nucleotide positions from .map file.\n\nExample output file format:\nPosition,Base,A,C,G,T\n55,A,957,2,28,1\n\nSpecified output file will be overwritten, if one with an identical name exists \n    (or 'output.csv' in the current directory, in the case where no output is specified)")
    confirm = input(
        ">>> Warning, will overwrite any file in the current directory called 'output.csv'\n>>> Continue? (y/n)\n>>> ")
    if confirm.lower() != 'y':
        sys.exit(">>> No output written. Exited successfully...")
    sys.argv.append(defaultOutput)  # set output to default ('output.csv')


def main():
    # unique SNP objects and SNP list
    class snpList:
        total = []  # static list of all unique substitutions

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

            self.add(substitution)
            snpList.total.append(self)

        # substitution specific incrementer
        def add(self, substitution):
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

    lineCount = 0
    try:
        with open(sys.argv[1], 'r') as f:

            for item in f.readlines():
                # split current line into space separated tokens
                # current line length may be variable across runtimes, thus it's safest to tokenize
                line = re.split(r'\t', item)
                if len(line) > 2:
                    lineCount += 1
                # tokenize the SNP string (last space separated string in each line of .map file)
                snpString = re.split(r'[, \n]', line[7])
                # parse through current SNP string token and generate usable unique SNP token
                for snpToken in snpString:
                    if snpToken:
                        # split current SNP token into position, expected base, and substitution
                        SNP = re.split(r'[:>]', snpToken)
                        # capture actual position (not zero-based index position) of SNP
                        snpPosition = int(SNP[0]) + 1
                        # capture expected base
                        base = SNP[1]
                        # capture substituted base
                        substitution = SNP[2]

                        index = 0
                        for snpElem in snpList.total:     # check if current position/base pair exists in the list
                            if snpElem.position == snpPosition and snpElem.base == base:
                                # if exists, increment substitution specific counter
                                snpElem.add(substitution)
                                break
                            index += 1

                        # if doesn't exist, add position/base pair to list
                        if index == len(snpList.total):
                            snpList(snpPosition, base, substitution)
    except:
        sys.exit(">>> Error reading input.\n>>> Verify that the input is a valid .map file, the input directory is a valid directory, and\n that you have privileges to access the input directory.\n>>> No output written. Terminated...")

    try:
        with open(sys.argv[2], 'w') as o:
            print('Position,Base,A,C,G,T', file=o)
            for final in snpList.total:     # print each position/base pair and its substitution counters
                if final.base == 'A':
                    print(str(final.position) + ',' + final.base + ',' + str(lineCount - (final.ACcount + final.AGcount +
                          final.ATcount)) + ',' + str(final.ACcount) + ',' + str(final.AGcount) + ',' + str(final.ATcount), file=o)
                if final.base == 'C':
                    print(str(final.position) + ',' + final.base + ',' + str(final.CAcount) + ',' + str(lineCount - (
                        final.CAcount + final.CGcount + final.CTcount)) + ',' + str(final.CGcount) + ',' + str(final.CTcount), file=o)
                if final.base == 'G':
                    print(str(final.position) + ',' + final.base + ',' + str(final.GAcount) + ',' + str(final.GCcount) + ',' +
                          str(lineCount - (final.GCcount + final.GAcount + final.GTcount)) + ',' + str(final.GTcount), file=o)
                if final.base == 'T':
                    print(str(final.position) + ',' + final.base + ',' + str(final.TAcount) + ',' + str(final.TCcount) + ',' +
                          str(final.TGcount) + ',' + str(lineCount - (final.TCcount + final.TGcount + final.TAcount)), file=o)

        print('>>> Output written to \n "' + sys.argv[2] + '"')
    except:
        sys.exit(">>> Error writing output.\n>>> Verify that you have privileges to write to the output directory, or if the output file is open in another program.\n  Else, try a different directory or file.\n>>> No output written. Terminated...")


if __name__ == "__main__":
    main()

# Author: Christopher Korfmann
# Copyright (c) 2021, Christopher Korfmann
