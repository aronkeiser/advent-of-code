import numpy as np

# part 1

## read input and strip whitespaces
with open('2015/input/input_2015-01.txt', 'r') as input:
    data = input.read().strip()

## sum up results of list comrpehension, replacing parenthesis with 1 and -1 
data_converted = [1 if x == '(' else -1 for x in data]
print(f'final floor: {np.sum(data_converted)}')

# part 2

## set starting floor to ground level
level = 0

## iterate over enumerated list
for index, element in enumerate(data_converted, start=1):
    ## add to level
    level += element
    ## stop loop when basement is entered
    if level < 0:
        print(f'entered basement at position: {index}')
        break