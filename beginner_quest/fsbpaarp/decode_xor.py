# read in primes and stack lines
with open('prime.txt') as p:
    with open('stack.txt') as s:
        plines = p.readlines()
        slines = s.readlines()

# xor each value and then print as character
for i in range(len(plines)):
    print(chr(int(plines[i].rstrip("\n")) ^ int(slines[i].rstrip("\n"))), end="")
print()
