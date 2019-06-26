STATE = '66de3c1bf87fdfcf' # goal state in hex
SIZE = 64 # bit size of step

s = int(STATE, 16)
s = format(s, '064b')

print('GOAL:', s)

goal = s
s1 = s

# takes input bit as string and flips it
def flip_bit(bit):
    if bit == '1':
        flip = '0' 
    else: 
        flip = '1'

    return flip

# carefully construct test string to reduce keyspace using mask
def form_string(base):
    s = ''
    tmp = ''

    # 1-4
    s += base[0] * 2 + flip_bit(base[0]) * 4 + base[0] * 3 + flip_bit(base[0]) * 3

    s += base[1:3]
    
    # 5
    s += base[3] * 5

    s += base[4:6]

    # 6-7
    s += base[6] * 7 + flip_bit(base[6]) * 3

    s += base[7:12]

    # 8
    s += base[12] * 6

    s += base[13:20]

    # 9
    s += base[20] * 3

    s += base[21:26] 

    # a
    s += base[26] * 4

    s += base[27:29] 

    # 1
    s += base[0]

    return s

# generate all hex strings from 0 to 2^29
def gen_all_hex():
    i = 0
    while i < 2**29:
        n = "{:029b}".format(i)
        s = form_string(n)
        yield s
        i += 1

# iterate over every possible reverse step to see if it propogates to goal state
for s in gen_all_hex():
    s2 = ""
    for i in range(SIZE):
        nbor = int(s[(i - 1) % SIZE] + s[i] + s[(i + 1) % SIZE], 2)
        
        if nbor == 7 or nbor == 0:
            s2 += '0'
        else: 
            s2 += '1'

    if (s2 == goal):
        print(s)
