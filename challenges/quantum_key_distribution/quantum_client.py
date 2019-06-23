import numpy
import requests
import random
import json
import subprocess

LEN = 512
URL = 'https://cryptoqkd.web.ctfcompetition.com/qkd/qubits'
FLAG = 'U2FsdGVkX19OI2T2J9zJbjMrmI0YSTS+zJ7fnxu1YcGftgkeyVMMwa+NNMG6fGgjROM/hUvvUxUGhctU8fqH4titwti7HbwNMxFxfIR+lR4='

binary = [0, 1]

data = {'basis': [], 'qubits': []}
bits = []

for x in range(LEN):
    axis = random.choice('x+')
    qubit = numpy.random.choice(numpy.arange(0, 2), p=[0.5, 0.5])
    bits.append(qubit)
    if qubit == 0:
        if axis == '+':
            qubit = {'real': 1, 'imag': 0}
        else: # axis = 'x'
            qubit = {'real': 0.707, 'imag': 0.707}
    else: # qubit = 1
        if axis == '+':
            qubit = {'real': 0, 'imag': 1}
        else: # axis = 'x'
            qubit = {'real': -0.707, 'imag': 0.707}        

    data['qubits'].append(qubit)
    data['basis'].append(axis)


r = requests.post(URL, json=data)
sat_response = r.json()

shared_hex_key = sat_response['announcement']
print('Encoded Encryption Key:', shared_hex_key)

result = []
binary_key = ""
for x in range(LEN):
    if data['basis'][x] == sat_response['basis'][x]:
        binary_key += str(bits[x])


binary_key = binary_key[:128]
print('Shared Key:', hex(int(binary_key, 2))[2:])

eek = int(shared_hex_key, 16)
sk = int(binary_key, 2)

ek = hex(eek ^ sk)
print('Encryption Key:', ek) 

derive = '(echo "%s" > /tmp/plain.key; xxd -r -p /tmp/plain.key > /tmp/enc.key)'%(ek)
subprocess.call(derive, shell=True, stdout=subprocess.PIPE)

decrypt = '(echo "%s" | openssl enc -d -aes-256-cbc -pbkdf2 -md sha1 -base64 --pass file:/tmp/enc.key > /tmp/flag.txt)'%(FLAG)
subprocess.call(decrypt, shell=True, stdout=subprocess.PIPE)

with open('/tmp/flag.txt') as flag:
    flag = flag.read()

print('\n', flag)
