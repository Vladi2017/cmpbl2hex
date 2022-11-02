#!python
import sys
import re   # there is not installed regex module under Cygwin
usage = 'Intented usage:\n $ cmp -bl file1 file2 | cmpbl2hex'
reo1 = re.compile(r'^(\d+)(\s+)(\d+)([^\d]+\d?[^\d]+)(\d+)(.*)')
if sys.argv.__len__() == 2:
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print(usage)
        exit()
    else: x = open(sys.argv[1], 'rt', encoding='ascii')
else: x = sys.stdin
while line := x.readline():  # https://docs.python.org/3.8/reference/expressions.html#assignment-expressions
    line = line.rstrip('\r\n')
    match = re.match(reo1, line)
    addr, val1, val2 = int(match.group(1)) - 1, int(match.group(3), 8), int(match.group(5), 8)
    lineHex = "{0:x}{1}{2:x}{3}{4:x}{5}".format(addr, match.group(2), val1, match.group(4), val2, match.group(6))
    print(lineHex)
