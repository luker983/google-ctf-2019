STATE = '66de3c1bf87fdfcf' # goal state in hex
PREV = '0011110001110011111010000000111011010000001101101000110110000110' # test state in binary
SIZE = 64 # bit size of step

s = int(STATE, 16)
s = format(s, '064b')

print('GOAL:', s)

s1 = PREV
s2 = ""
for i in range(SIZE):
    nbor = int(s1[(i - 1) % SIZE] + s1[i] + s1[(i + 1) % SIZE], 2)

    if nbor == 7 or nbor == 0:
        s2 += '0'
    else:
        s2 += '1'

print('PREV:', s1)
print('NEXT:', s2)
if s2 == s:
    print('NEXT matches GOAL')
