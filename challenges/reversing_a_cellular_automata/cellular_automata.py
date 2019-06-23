STATE = '66de3c1bf87fdfcf'
FLAG = 'U2FsdGVkX1/andRK+WVfKqJILMVdx/69xjAzW4KUqsjr98GqzFR793lfNHrw1Blc8UZHWOBrRhtLx3SM38R1MpRegLTHgHzf0EAa3oUeWcQ='
SIZE = 8

s = bin(int(STATE, 16))[2:]
s = '0' + s

for i in range(SIZE):
    for j in range(SIZE):
        print(s[(i * 8) + j], '\t', end="")

    print()
