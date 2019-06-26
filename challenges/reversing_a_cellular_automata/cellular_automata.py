STATE = '66de3c1bf87fdfcf' # initial state in hex
# STATE = 'deadbeef' # if using this state, change SIZE to 32
SIZE = 64 # bit size of step
COUNT = 80 # number of iterations

s = int(STATE, 16)
s = format(s, '0%sb'%(str(SIZE)))

print('GOAL:', s)

s1 = s

i = 0
while i < COUNT:
    i += 1
    s2 = ""
    for j in range(SIZE):
        nbor = int(s1[(j - 1) % SIZE] + s1[j] + s1[(j + 1) % SIZE], 2)
    
        if nbor == 7 or nbor == 0:
            s2 += '0'
        else:
            s2 += '1'

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
