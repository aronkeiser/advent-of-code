import numpy as np
import pandas as pd

# Read input and strip whitespaces
with open('2015/input/input_2015-06.txt', 'r') as input:
    data = input.read().strip()

# Part 1

# Generate empty data frame
instr = pd.DataFrame(columns=('action', 'from', 'to'))

# Preprocess data to get raw values
data = data.replace('turn ', '')
data = data.replace(',', '')
instr_raw = data.split('\n')

# Iterate over each row and append to data frame
for row in instr_raw:

    # Isolate elements
    row_split  = row.split(' ')
    row_action = row_split[0]
    row_from   = row_split[1]
    row_to     = row_split[3]

    # Generate dictionary
    row_dct = {
        'action': row_action,
        'from': row_from,
        'to': row_to
        }

    # Append dictionary to data frame
    instr = instr._append(row_dct, ignore_index=True)

# Set dtypes
instr = instr.astype({
    'action': 'str',
    'from': 'int',
    'to': 'int'
    })

print(instr)