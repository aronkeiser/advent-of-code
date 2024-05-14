import numpy as np
import hashlib

## read input and strip whitespaces
with open('2015/input/input_2015-04.txt', 'r') as input:
    data = input.read().strip()

# part 1 + 2

num = 1 # part 1 
# num = 346386 # part 2, starting at the number part one finished with
numstr = str(num)
result = str()

while not result.startswith('00000'): # part 1
# while not result.startswith('000000'): # part 2

    print(f'checking number {numstr}')

    code = data + numstr
    result = hashlib.md5(code.encode())

    num += 1
    numstr = str(num)
    result = result.hexdigest()

print('SUCCESS!!!\n')

print(f'code: {code}')
print(f'hash: {result}')