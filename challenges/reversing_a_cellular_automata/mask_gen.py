STATE = '66de3c1bf87fdfcf'
FLAG = 'U2FsdGVkX1/andRK+WVfKqJILMVdx/69xjAzW4KUqsjr98GqzFR793lfNHrw1Blc8UZHWOBrRhtLx3SM38R1MpRegLTHgHzf0EAa3oUeWcQ='
SIZE = 64

s = int(STATE, 16)
s = format(s, '064b')


print('GOAL:', s)

goal = s

mask = ['0'] * SIZE
x = '1'

for i in range(SIZE):
  
    if goal[i] == '0':
        mask[(i - 1) % SIZE] = x
        mask[i] = x
        mask[(i + 1) % SIZE] = x
        if goal[(i + 1) % SIZE] == '1':
            x = str(hex(int(x, 16) + 1))[2:]
        
        
for c in mask:
    print(c, end="")
