import subprocess

FLAG = 'U2FsdGVkX1/andRK+WVfKqJILMVdx/69xjAzW4KUqsjr98GqzFR793lfNHrw1Blc8UZHWOBrRhtLx3SM38R1MpRegLTHgHzf0EAa3oUeWcQ='


# read in all reversed steps from the brute force stage
keys = []
with open('reversed.txt', 'r') as f:
    for line in f:
        keys.append(line)

for key in keys:
    key = hex(int(key, 2))[2:]
    convert = '(echo "%s" > /tmp/plain.key; xxd -r -p /tmp/plain.key > /tmp/enc.key)'%(key)
    subprocess.call(convert, shell=True, stdout=subprocess.PIPE)

    # attempt to decrypt the flag with the current key
    decrypt = '(echo "%s" | openssl enc -d -aes-256-cbc -pbkdf2 -md sha1 -base64 --pass file:/tmp/enc.key | grep CTF > /tmp/flag.txt)'%(FLAG)
    try:
        subprocess.check_call(decrypt, shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.PIPE)
        # if the call is successful, print key and stop decrypting
        print('Key: %s'%(key))
        break
    except Exception as e:
        continue

# print out flag
with open('/tmp/flag.txt', 'r') as f:
    flag = f.read()
print('Decrypted: %s'%(flag))
