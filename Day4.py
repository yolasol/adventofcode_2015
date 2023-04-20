# part 1
# import library, get puzzle input
import hashlib
input = 'yzbqklnj'
num = 1

# get key, translate to MD5 hash
key = input + str(num)
hash = hashlib.md5(key.encode())
hex = hash.hexdigest()

# are we there yet?
while hex[0:5] != '00000':
    key = input + str(num)
    hash = hashlib.md5(key.encode())
    hex = hash.hexdigest()
    num += 1

print(hex, num-1)

# reset
# why? because I cannot brain
num = 1
key = input + str(num)
hash = hashlib.md5(key.encode())
hex = hash.hexdigest()

# are we there yet? part 2
while hex[0:6] != '000000':
    key = input + str(num)
    hash = hashlib.md5(key.encode())
    hex = hash.hexdigest()
    num += 1

print(hex, num-1)
