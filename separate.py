# separate keys from solana keypair file

# use keypair file path as argument

import sys
from os.path import exists

# check if argument entered
if len(sys.argv) < 2:
    print("Invalid arguments")
    quit()

# check if file exists
if not exists(sys.argv[1]):
    print("Enter valid keypair file path!")
    quit()


# base 58 symbols
alphabet58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

# read keypair file
text_file = open(sys.argv[1], "r")
lines = text_file.readlines()
lines = lines[0][1:-1]
lines=lines.split(',')
private_array=lines[:32]
public_array=lines[32:]

# check if keypair file is valid
if not (len(private_array)==32 and len(public_array) == 32):
    print("Invalid keypair file")
    quit()

# create keys in hex format
public_hex = ""
private_hex = ""
for i in range(0,32):
    public_hex = public_hex + "%02x"%(int(public_array[i]))
    private_hex = private_hex + "%02x"%(int(private_array[i]))

# trasfer hex value to base 10
public_decimal = int(public_hex,16)
private_decimal = int(private_hex,16)

base58_pubkey = ""
base58_private_key = ""

# encode hex value of public key to base 58
while (public_decimal > 0):
    base58_pubkey = alphabet58[public_decimal%58] + base58_pubkey
    public_decimal = public_decimal // 58

# encode hex value of private key to base 58
while (private_decimal > 0):
    base58_private_key = alphabet58[private_decimal%58] + base58_private_key
    private_decimal = private_decimal // 58

# print keys
print("pubkey:      " + base58_pubkey)
print("private key: " + base58_private_key)
