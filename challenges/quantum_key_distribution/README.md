# Quantum Key Distribution (Crypto)

![Quantum Key Distribution](images/qkd.png "Img")

## Challenge

We are simulating a Quantum satellite that can exchange keys using qubits implementing BB84. You must POST the qubits and basis of measurement to `/qkd/qubits` and decode our satellite response, you can then derive the shared key and decrypt the flag. Send 512 qubits and basis to generate enough key bits.

## Files



## Steps

1. Read code and format at `https://cryptoqkd.web.ctfcompetition.com/`
2. Write program to send random qubits and bases to satellite
3. Use response to compare bases and derive shared key
4. Figure out how encryption key is encoded with our shared key
5. It's xor

