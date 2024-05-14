import numpy as np

## read input and strip whitespaces
with open('2015/input/input_2015-03.txt', 'r') as input:
    data = input.read().strip()

# part 1
print('\npart 1')

## convert symbols to list of moves
moves = []

for char in data:
    if char == "^":
        move = ["vertical", 1]
    elif char == "v":
        move = ["vertical", -1]
    elif char == ">":
        move = ["horizontal", 1]
    elif char == "<":
        move = ["horizontal", -1]
    else:
        print("unknown character")
        break
    
    moves.append(move)

def generate_houses_list(moves):

    ## initialize houses list
    houses = [[0,0]]

    ## set starting position (vertical left, horizontal right)
    pos = [0,0]

    for move in moves:
        if move[0] == "vertical":
            pos[0] += move[1]
        elif move[0] == "horizontal":
            pos[1] += move[1]
        else:
            print("unknown axis")
            break
        houses.append(pos.copy())
    
    return houses
    
houses = generate_houses_list(moves)

## generate set (unique home that receive presents)
houses_unique = set()
for house in houses:
    houses_unique.add(tuple(house))

print(f'total number of moves: {len(data)}')
print(f'total number of gifts: {len(houses)}')
print(f'total nubmer of gifted homes: {len(houses_unique)}')

# part 2
print('\npart 2')

## index over initial moves list and generate moves for santa and robosanta
moves_santa = moves[::2]
moves_robosanta = moves[1::2]

# generate houses list for both
houses_santa = generate_houses_list(moves_santa)
houses_robosanta = generate_houses_list(moves_robosanta)

# concatenate both lists
houses_both = houses_santa + houses_robosanta

# generate unique set from mutual list
houses_unique = set()
for house in houses_both:
    houses_unique.add(tuple(house))

print(f'total number of moves: {len(data)}')
print(f'total number of gifts: {len(houses_both)}')
print(f'total nubmer of gifted homes: {len(houses_unique)}')