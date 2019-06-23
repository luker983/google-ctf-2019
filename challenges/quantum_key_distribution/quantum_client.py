import requests
import random
import json
import subprocess

LEN = 512
URL = 'https://cryptoqkd.web.ctfcompetition.com/qkd/qubits'
FLAG = 'U2FsdGVkX19OI2T2J9zJbjMrmI0YSTS+zJ7fnxu1YcGftgkeyVMMwa+NNMG6fGgjROM/hUvvUxUGhctU8fqH4titwti7HbwNMxFxfIR+lR4='

axis = ['+', 'x']
binary = [0, 1]

data = {'basis': [], 'qubits': []}

for x in range(LEN):
    axis = random.choice(axis)
    qubit = random.choice(binary)

    if qubit == 0:
        if axis == '+':
            qubit = {'real': 1, 'imag': 0}
        else: # axis = 'x'
            qubit = {'real': 0.71, 'imag': 0.71}
    else: # qubit = 1
        if axis == '+':
            qubit = {'real': 0, 'imag': 1}
        else: # axis = 'x'
            qubit = {'real': -0.71, 'imag': 0.71}        

    data['qubits'].append(qubit)
    data['basis'].append(axis)

#print(json.dumps(data, indent=4))

r = requests.post(URL, json=data)
#print(r.text)
sat_response = r.json()

shared_hex_key = sat_response['announcement']
print('Shared Hex Key:', shared_hex_key)

derive = '(echo "%s" > /tmp/plain.key; xxd -r -p /tmp/plain.key > /tmp/enc.key)'%(shared_hex_key)
subprocess.call(derive, shell=True, stdout=subprocess.PIPE)

decrypt = '(echo "%s" | openssl enc -d -aes-256-cbc -pbkdf2 -md sha1 -base64 --pass file:/tmp/enc.key > /tmp/flag.txt)'%(FLAG)
subprocess.call(decrypt, shell=True, stdout=subprocess.PIPE)
