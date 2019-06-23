import requests
import random
import json

LEN = 512
URL = 'https://cryptoqkd.web.ctfcompetition.com/qkd/qubits'

axis = ['+', 'x']
binary = [0, 1]

data = {'basis': [], 'qubits': []}

for x in range(LEN):
    data['basis'].append(random.choice(axis))
    qubit = random.choice(binary)
    if qubit == 1:
        qubit = {'real': 1, 'imag': 0}
    else:
        qubit = {'real': 0, 'imag': 1}

    data['qubits'].append(qubit)

#print(json.dumps(data, indent=4))

r = requests.post(URL, json=data)

print(r.text)
