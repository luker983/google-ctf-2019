import numpy
import requests
import random
import json
import subprocess

LEN = 512 # number of qubits to send
URL = 'https://cryptoqkd.web.ctfcompetition.com/qkd/qubits'
FLAG = 'U2FsdGVkX19OI2T2J9zJbjMrmI0YSTS+zJ7fnxu1YcGftgkeyVMMwa+NNMG6fGgjROM/hUvvUxUGhctU8fqH4titwti7HbwNMxFxfIR+lR4='

data = {'basis': [], 'qubits': []}
bits = []

# generate LEN qubits using random bits and bases
for x in range(LEN):
    axis = random.choice('x+')
    qubit = numpy.random.choice(numpy.arange(0, 2), p=[0.5, 0.5])
    bits.append(qubit)
    if qubit == 0:
        # 0 and + = 0 degrees
        if axis == '+':
            qubit = {'real': 1, 'imag': 0}
        # 0 and x = 45 degrees
        else:
            qubit = {'real': 0.707, 'imag': 0.707}
    else:
        # 1 AND + = 90 degrees
        if axis == '+':
            qubit = {'real': 0, 'imag': 1}
        # 1 and x = 135 degrees
        else:
            qubit = {'real': -0.707, 'imag': 0.707}        

    data['qubits'].append(qubit)
    data['basis'].append(axis)


# send data to server and load response as JSON
r = requests.post(URL, json=data, verify=False)
sat_response = r.json()

encoded_encryption_key = sat_response['announcement']
print('Encoded Encryption Key:', encoded_encryption_key)

# derive shared key
shared_key = ""
for x in range(LEN):
    if data['basis'][x] == sat_response['basis'][x]:
        shared_key += str(bits[x])

shared_key = shared_key[:128]
print('Shared Key:', hex(int(shared_key, 2))[2:])

eek = int(encoded_encryption_key, 16)
sk = int(shared_key, 2)

# decode encrpytion key with shared key using XOR
ek = hex(eek ^ sk)[2:]
print('Encryption Key:', ek) 

# make key file
get_ek = '(echo "%s" > /tmp/plain.key; xxd -r -p /tmp/plain.key > /tmp/enc.key)'%(ek)
subprocess.call(get_ek, shell=True, stdout=subprocess.PIPE)

# decrypt the flag
decrypt = '(echo "%s" | openssl enc -d -aes-256-cbc -pbkdf2 -md sha1 -base64 --pass file:/tmp/enc.key > /tmp/flag.txt)'%(FLAG)

subprocess.call(decrypt, shell=True, stdout=subprocess.PIPE)

# print the flag
with open('/tmp/flag.txt') as flag:
    flag = flag.read()

print('\n', flag)
