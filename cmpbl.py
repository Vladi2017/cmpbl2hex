#!python
import sys
if sys.argv.__len__() == 2: inFile = sys.argv[1]
else: inFile = sys.stdin
with open(inFile, 'rt', encoding='ascii') as x:
    while line := x.readline():  # https://docs.python.org/3.8/reference/expressions.html#assignment-expressions
        line = line.rstrip('\r\n')
        print(line, '+Vld.')
