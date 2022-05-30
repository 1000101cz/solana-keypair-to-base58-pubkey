# convert hex string to base58 string

import sys

decimal = int(sys.argv[1],16)

outstring = ""

alphabet58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

while (decimal > 0):
    outstring = alphabet58[decimal%58] + outstring
    decimal = decimal // 58

print(outstring)
