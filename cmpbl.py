#!python
import sys
inFile = sys.argv[1]
with open(inFile, 'rt', encoding='ascii') as x:
    while line := x.readline():  # https://docs.python.org/3.8/reference/expressions.html#assignment-expressions
        line = line.rstrip('\r\n')
        print(line, '+Vld.')
