import subprocess

FLAG = 'U2FsdGVkX1/andRK+WVfKqJILMVdx/69xjAzW4KUqsjr98GqzFR793lfNHrw1Blc8UZHWOBrRhtLx3SM38R1MpRegLTHgHzf0EAa3oUeWcQ='


keys = []
with open('reversed.txt', 'r') as f:
    for line in f:
        keys.append(line)

for key in keys:
    key = hex(int(key, 2))[2:]
    #print(key)
    derive = '(echo "%s" > /tmp/plain.key; xxd -r -p /tmp/plain.key > /tmp/enc.key)'%(key)
    subprocess.call(derive, shell=True, stdout=subprocess.PIPE)

    decrypt = '(echo "%s" | openssl enc -d -aes-256-cbc -pbkdf2 -md sha1 -base64 --pass file:/tmp/enc.key >> /tmp/flag.txt)'%(FLAG)
    subprocess.call(decrypt, shell=True, stdout=subprocess.PIPE)

