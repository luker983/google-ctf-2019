# [Reverse Cellular Automata](https://cellularautomata.web.ctfcompetition.com/)

![Reversing Cellular Automata(images/rca.png "Img")

## Challenge

We have built a cellular automata with 64 bit steps and obeys Wolfram rule 126, it's boundary condition wraps around so that the last bit is a neighbor of the first bit. Below you can find a special step we chose from the automata.

The flag is encrypted with AES256-CBC, the encryption key is the previous step that generates the given step. Your task is to reverse the given step and find the encryption key.

### Example decryption with 32 bit steps:

```
echo "404c368b" > /tmp/plain.key; xxd -r -p /tmp/plain.key > /tmp/enc.key
```

```
echo "U2FsdGVkX18+Wl0awCH/gWgLGZC4NiCkrlpesuuX8E70tX8t/TAarSEHTnpY/C1D" | openssl enc -d -aes-256-cbc -pbkdf2 -md sha1 -base64 --pass file:/tmp/enc.key
```

### Flag (base64)

```
U2FsdGVkX1/andRK+WVfKqJILMVdx/69xjAzW4KUqsjr98GqzFR793lfNHrw1Blc8UZHWOBrRhtLx3SM38R1MpRegLTHgHzf0EAa3oUeWcQ=
```

### Obtained step (hex)

```
66de3c1bf87fdfcf
```

## Files

* `cellular_automata.py`: Cellular automata program that starts with the provided step and follows the rules in the challenge prompt.
* `cell_test.py`: Takes one step and runs it through one round of Wolfram rule 126 to see if it matches the desired step.
* `mask_gen.py`: Generates a mask that shows what values in a previous step must be equal in order to result in the desired step.
* `key.txt`: File to show how the mask is interpreted in order to reduce the keyspace.
* `cryptanalysis.py`: Brute force steps to get every possible reverse step.
* `reverse.txt`: List of all possible reverse steps.
* `decrypt.py`: Decrypt the flag using every possible reverse step key.
* `flag.txt`: Solution to this challenge.

## Steps

1. Go to `https://cellularautomata.web.ctfcompetition.com/`
2. Construct cellular automata
3. Keyspace is 2^64, but can be reduced to 2^29 because 0's are only produced by 111 or 000
