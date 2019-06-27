# generates string that shows how rule 126 reduces the keyspace
STATE = '66de3c1bf87fdfcf' # goal state in hex 
SIZE = 64 # bit size of step

s = int(STATE, 16)
s = format(s, '064b')

print('GOAL:', s)

goal = s

# generate empty mask
mask = ['0'] * SIZE
x = '1'

for i in range(SIZE):
    # when a bit is 0, it's reverse must be 111 or 000
    if goal[i] == '0':
        mask[(i - 1) % SIZE] = x
        mask[i] = x
        mask[(i + 1) % SIZE] = x
        if goal[(i + 1) % SIZE] == '1':
            x = str(hex(int(x, 16) + 1))[2:]
        
print('MASK:', end=" ")  
for c in mask:
    print(c, end="")
print()
