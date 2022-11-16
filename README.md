# cmpbl2hex
cmpbl2hex - a (very) short but useful script which convert GNU cmp output report.

cmp is a CLI utility in diffutils package which (binary) compares two files byte by byte. Using with '-bl' switches cmp output the (decimal 1-based) byte numbers (byte addresses in file(s)) and (octal) values of all differing bytes. The key words are "decimal 1-based" and "octal". cmpbl2hex convert the representation for these values as "hexadecimal 0-based" and "hexadecimal". This could be useful since hex representation is common for binary editors. As a CLI cmpbl2hex is meant to work on the shell pipe after cmp.

For installing just place the script into your $PATH and make sure the eXecute bit is set.

Example without cmpbl2hex:
```
vladi@VladiLaptop1W10 /cygdrive/c/Users/mvman/Downloads/tmp1/tmp1/tmp1/tmp/png2svg$ cmp -bl fc2Id0U8.png fc2Id0U8_2.png
43493 335 M-]  163 s
44198 171 y    311 M-I
45924   0 ^@     1 ^A
47543 165 u    253 M-+
47944 344 M-d   15 ^M
48889  71 9      7 ^G
```
Example with cmpbl2hex on the pipe:
```
vladi@VladiLaptop1W10 /cygdrive/c/Users/mvman/Downloads/tmp1/tmp1/tmp1/tmp/png2svg$ cmp -bl fc2Id0U8.png fc2Id0U8_2.png|cmpbl2hex
a9e4  dd M-]    73 s
aca5  79 y      c9 M-I
b363   0 ^@      1 ^A
b9b6  75 u      ab M-+
bb47  e4 M-d     d ^M
bef8  39 9       7 ^G
```
