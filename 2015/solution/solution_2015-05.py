import numpy as np
from collections import Counter
from itertools import compress

# read input and strip whitespaces
with open('2015/input/input_2015-05.txt', 'r') as input:
    data = input.read().strip()

# create list from data
words = data.split('\n')


# part 1

# initialize nice words counter
count_nice_words = 0

# iterate over each words
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
        # print(f'{word} is nice')
        # increment counter
        count_nice_words += 1
    else:
        # print(f'{word} is naughty')
        continue

# print total number of nice words
print('--- Part 1 ---')
print(f'{count_nice_words} nice words in total\n')


# part 2

def check_crit1(word):
    
    # Generate all pairs form test word
    pairs = [word[i:i+2] for i in range(len(word)-1)]
    pairs_ct = Counter(pairs)

    # Generate list of pairs that appear more than once
    pairs_dup = {key: value for key, value in pairs_ct.items() if value > 1}

    # Check if pairs are homogenous (contain 2 equal letters)
    pairs_dup_hom = list()
    for pair in pairs_dup.keys():
        
        pair_dup_hom = [(True if char_first == char_second else False)
                        for char_first, char_second in [pair]]
        pairs_dup_hom.extend(pair_dup_hom)

    # If all duplicate pairs are homogenous, perform overlap check
    if all(pairs_dup_hom):

        pairs_dup_hom_ovl = list()
        for pair in list(pairs_dup.keys()):

            # Determine length of word after removeing substring
            l = len(word.replace(pair, ''))
            # If letters don't overlap,
            # len will be 12 after removing substring
            if l > 12:
                pairs_dup_hom_ovl.append(True)
            else:
                pairs_dup_hom_ovl.append(False)
        
        if all(pairs_dup_hom_ovl): return False
        else: return True
    else: return True

def check_crit2(word):

    # create list and shifted list of letters for criterium no. 2
    x = list(word); x = x + ['','']
    y = list(word); y = ['',''] + y

    # compare list and shifted list
    comp = []
    for i in range(len(x)):
        comp.append(x[i] == y[i])

    if any(comp): return True
    else: return False

# reset nice words counter
count_nice_words = 0

# iterate over each words
for word in words:
    crit1 = check_crit1(word)
    crit2 = check_crit2(word)

    if all([crit1, crit2]):
        # print(f'{word} is nice')
        count_nice_words += 1
    else:
        # print(f'{word} is naughty')
        continue

# print total number of nice words
print('--- Part 2 ---')
print(f'{count_nice_words} nice words in total')