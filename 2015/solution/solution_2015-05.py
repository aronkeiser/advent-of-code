import numpy as np
from collections import Counter

## read input and strip whitespaces
with open('2015/input/input_2015-05.txt', 'r') as input:
    data = input.read().strip()

# create list from data
words = data.split('\n')

# part 1

## initialize nice words counter
count_nice_words = 0

## iterate over each words
for word in words:

    # create list and shifted list of letters for criterium no. 2
    x = list(word); x.append('')
    y = list(word); y.insert(0, '')
    # compare list and shifted list
    comp = []
    for i in range(len(x)):
        comp.append(x[i] == y[i])
    
    # perform checks for the 3 criteria
    if (
        # criterium no. 1
        np.sum([1 for letter in word if letter in "aeiou"]) >= 3) and (
            # criterium no. 2
            any(comp)) and (
                # criterium no. 3
                not 'ab' in word) and (
                     not 'cd' in word) and (
                           not 'pq' in word) and (
                                  not 'xy' in word):
        # provide feedback nice
        # print(f'{word} is a nice word')
        # increment counter
        count_nice_words += 1
    else:
        # provide feedback nice
        # print(f'{word} is a naughty word')
        continue

## print total number of nice words
# print(f'{count_nice_words} nice words in total')

# part 2

## reset nice words counter
count_nice_words = 0

# iterate over each words
for word in words:

    # initialize counter for duplicate characters
    ct = 1
    ct_list = list()

    # check if there are overlaps for rule 1
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            ct += 1
            ct_list.append(ct)
            if ct == 3:
                break
        else:
            ct = 1
            ct_list.append(ct)
    
    ct_max = max(ct_list)

    # generate pairs of characters
    pairs = [word[_:_+2] for _ in range(len(word)-1)]

    if ( # rule 1: repeating pairs and no overlaps
        (max(Counter(pairs).values()) > 1) and (ct_max != 3)):# and (

        #):
        print(f'{word} {ct} is a nice word')
    else:
        print(f'{word} {ct} is a naughty word')

# test = Counter(pairs).values()
test = list(range(10))
print(test==1)
