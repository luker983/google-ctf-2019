with open('xor.txt') as f:
    a = []
    b = []
    for x in f:
        a.append(x.rstrip("\n").split(' ')[0])
        b.append(x.rstrip("\n").split(' ')[-1])

for x in range(0, len(a)):
#    if (int(a[x]) > 208):
#        print(chr(int(a[x]) ^ int(b[x-1])), end="")
#        continue
    print(chr(int(a[x]) ^ int(b[x])), end="")
