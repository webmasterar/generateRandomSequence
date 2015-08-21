#! /usr/bin/python

###
## title: generateRandomSequence.py
## description: Generates random DNA/Protein sequences and outputs them to a file
## license: MIT License
## date: 21/08/2015
## author: Ahmad Retha
###

import time
import random
import getopt
import sys

###
 # Define command line options
##
info = """
Command line options:
 -h\tHelp
 -f\tFile name
 -a\tAlphabet (DNA/dna/PROT/prot)
 -n\tNumber of characters
 -s\tOptional: make file fasta format with given title
 -w\tOptional: width of fasta line (default:70)
"""
f = ""
a = ""
n = 0
s = ""
w = 70
try:
    opts, args = getopt.getopt(sys.argv[1:], "hf:a:n:s:w:")
    for opt, arg in opts:
        arg = arg.strip()
        if opt == "-h":
            print info
            sys.exit(0)
        elif opt == "-a":
            validArgs = ["DNA", "dna", "PROT", "prot"]
            if arg not in validArgs:
                raise ValueError("Invalid Alphabet. Must be one of: ", ", ".join(validArgs))
            a = arg
        elif opt == "-f":
            f = arg
        elif opt == "-n":
            try:
                n = int(float(arg))
            except Exception:
                print "Error: Invalid value for -n supplied"
                sys.exit(2)
        elif opt == "-s":
            s = arg
        elif opt == "-w":
            w = int(arg)
        else:
            raise
except ValueError as e:
    print e
    sys.exit(2)
except getopt.GetoptError:
    print "Invalid Options Supplied. Try Again:\n" + info
    sys.exit(2)

###
 # Prepare random alphabet soup
##

if a == "DNA":
    alphabet = list("ATCG")
elif a == "dna":
    alphabet = list("atcg")
elif a == "PROT":
    alphabet = list("ARNDCQEGHILKMFPSTWYV")
else:
    alphabet = list("arndcqeghilkmfpstwyv")
alphSize = len(alphabet)
bowlSize = 10000
soupBowl = []

i = 0
while i < bowlSize:
    soupBowl.append(alphabet[i % alphSize])
    i = i + 1

###
 # Pull out random letters from soup and write to file
##

start = time.clock()

fileName = f
sequenceSize = n
try:
    f = open(fileName, "w")

    if s != "":
        f.write("> " + s + "\n")

    i = 0
    while i < sequenceSize:
        f.write(soupBowl[int(bowlSize * random.random())])
        i = i + 1
        if s != "" and i % w == 0:
            f.write("\n")

    f.close()
except IOError as e:
    print "Error opening file to write to %s with message: %s" % (fileName, e.strerror)
except:
    print "An unexpected error occured: ", sys.exc_info()[0]

stop = time.clock()
time = stop - start

print "Wrote %d %s characters to %s in %1.2fs" % (sequenceSize, a, fileName, time)

