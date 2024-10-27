import random
import math

with open('flag.txt', 'r')as f:
    flag = f.read().strip()

characters = 'abcdefghijklmnopqrstuvwxyz0123456789{}_'
flag_number = ''

for a in flag:
    flag_number += f'{characters.index(a):02d}'
flag_number = int(flag_number)
print(flag_number, flag_number.bit_length())

numbers = []
inst = random.Random()
entropy = 624
while entropy > 0:
    k = random.randint(1, 3)
    x = inst.getrandbits(k * 32)
    numbers.append(x)
    entropy -= k

bits = math.ceil(flag_number.bit_length()/32) * 32
key = inst.getrandbits(bits)
print(key)

encrypted = flag_number ^ key
print(encrypted)

with open('encrypted_flag.txt', 'w') as f:
    f.write(str(encrypted))

with open('dump.txt', 'w') as f:
    f.write(str(numbers))