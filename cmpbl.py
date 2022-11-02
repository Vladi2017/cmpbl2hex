#!python
import sys
if sys.argv.__len__() == 2: x = open(sys.argv[1], 'rt', encoding='ascii')
else: x = sys.stdin
while line := x.readline():  # https://docs.python.org/3.8/reference/expressions.html#assignment-expressions
        line = line.rstrip('\r\n')
        print(line, '+Vld.')
