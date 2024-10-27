import math
from mt19937predictor import MT19937Predictor


with open('dump.txt', 'r') as f:
    numbers = f.read().strip()[1:-1].split(',')
numbers = [int(a.strip()) for a in numbers]

with open('encrypted_flag.txt', 'r') as f:
    encrypted_flag = int(f.read().strip())


predictor = MT19937Predictor()
for number in numbers:
    predictor.setrandbits(number, math.ceil(number.bit_length()/32) * 32)

bits = math.ceil(encrypted_flag.bit_length()/32) * 32
key = predictor.getrandbits(bits)
print(key)


flag_number = encrypted_flag ^ key
flag_number = '0' + str(flag_number)
print(flag_number)

flag = ''
characters = 'abcdefghijklmnopqrstuvwxyz0123456789{}_'
for i in range(0, len(flag_number), 2):
    print(characters[int(flag_number[i:min(i+2, len(flag_number))])], end='')

print()