STATE = '66de3c1bf87fdfcf'
FLAG = 'U2FsdGVkX1/andRK+WVfKqJILMVdx/69xjAzW4KUqsjr98GqzFR793lfNHrw1Blc8UZHWOBrRhtLx3SM38R1MpRegLTHgHzf0EAa3oUeWcQ='
SIZE = 64

s = int(STATE, 16)
s = format(s, '064b')


print('GOAL:', s)


s1 = '0011110001110011111010000000111011010000001101101000110110000110'
s2 = ""
for i in range(SIZE):
    l = s1[(i - 1) % SIZE]
    c = s1[i]
    r = s1[(i + 1) % SIZE]
    
    if l == '1' and c == '1' and r == '1':
        s2 += '0'
    elif l == '1' and c == '1' and r == '0':
        s2 += '1'
    elif l == '1' and c == '0' and r == '1':
        s2 += '1'
    elif l == '1' and c == '0' and r == '0':
        s2 += '1'
    elif l == '0' and c == '1' and r == '1':
        s2 += '1'
    elif l == '0' and c == '1' and r == '0':
        s2 += '1'
    elif l == '0' and c == '0' and r == '1':
        s2 += '1'
    else: 
        s2 += '0'

print('ATTM:', s2)
