#STATE = '66de3c1bf87fdfcf'
STATE = 'deadbeef'
FLAG = 'U2FsdGVkX1/andRK+WVfKqJILMVdx/69xjAzW4KUqsjr98GqzFR793lfNHrw1Blc8UZHWOBrRhtLx3SM38R1MpRegLTHgHzf0EAa3oUeWcQ='
SIZE = 32

s = int(STATE, 16)
s = format(s, '032b')


print('GOAL:', s)


s1 = s
while True:
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

    print(s2)
    s1 = s2
   
    break 
    if (s1 == s):
        break
