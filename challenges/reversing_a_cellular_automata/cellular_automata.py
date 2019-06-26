STATE = '66de3c1bf87fdfcf'
# STATE = 'deadbeef' # if using this state, change SIZE to 32
FLAG = 'U2FsdGVkX1/andRK+WVfKqJILMVdx/69xjAzW4KUqsjr98GqzFR793lfNHrw1Blc8UZHWOBrRhtLx3SM38R1MpRegLTHgHzf0EAa3oUeWcQ='
SIZE = 64
COUNT = 80

s = int(STATE, 16)
s = format(s, '0%sb'%(str(SIZE)))

print('GOAL:', s)

s1 = s

i = 0
while i < COUNT:
    i += 1
    s2 = ""
    for j in range(SIZE):
        l = s1[(j - 1) % SIZE]
        c = s1[j]
        r = s1[(j + 1) % SIZE]
        
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

    ########################################
    # print out steps using unicode blocks #
    for bit in s2:
        if bit == '1':
            print(u'\u2588', end="")
        if bit == '0':
            print(' ', end="")

    print()
    #######################################

    #######################################
    # print out steps with the bit string #
    # print(s2)

    s1 = s2
   
    if (s1 == s):
        print('Found reverse step!')
