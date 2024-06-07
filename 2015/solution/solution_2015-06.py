import pandas as pd
import time

# Function for reading in and processing instructions
def gen_instr_df():

    # Read input and strip whitespaces
    with open('2015/input/input_2015-06.txt', 'r') as input:
        data = input.read().strip()

    # Generate data frame to hold instructions
    instr = pd.DataFrame()

    # Preprocess data to get raw values
    data = data.replace('turn ', '')
    instr_raw = data.split('\n')

    # Iterate over each row and append to data frame
    for row in instr_raw:

        # Isolate elements
        row_split  = row.split(' ')

        # Isolate action
        row_action = row_split[0]

        # Isolate "from" coordinates
        row_from = row_split[1].split(',')
        row_from_x = row_from[0]; row_from_y = row_from[1]

        # Isolate "to" coordinates
        row_to = row_split[3].split(',')
        row_to_x = row_to[0]; row_to_y = row_to[1]

        # Generate dictionary
        row_dct = {'action': row_action, 'from_x': row_from_x, 'from_y': row_from_y,
                   'to_x'  : row_to_x, 'to_y'  : row_to_y}

        # Append dictionary to data frame
        instr = instr._append(row_dct, ignore_index=True)

    # Set dtypes
    instr = instr.astype({'action': 'str', 'from_x': 'int', 'from_y': 'int',
                          'to_x'  : 'int', 'to_y'  : 'int'})
    
    return instr

# Function for generating 2d matrix represented by a data frame
def gen_lights_df():

    lights = pd.DataFrame(columns = range(1000), index = range(1000))

    # Set all lights off (0) and supress FutureWarning
    with pd.option_context("future.no_silent_downcasting", True):
        lights = lights.fillna(0).infer_objects(copy=False)

    return lights

# Function that generates intermediate data frame with updated values for respective case (part 1)
def switch_lights_part1(d):

    # Index data frame according to instructions and replace values
    lights_ = lights.iloc[
        instr.iloc[row]['from_x']:instr.iloc[row]['to_x']+1,
        instr.iloc[row]['from_y']:instr.iloc[row]['to_y']+1
        ].replace(d)
    
    return lights_

# Function that generates intermediate data frame with updated values for respective case (part 2)
def switch_lights_part2(i):

    # Index data frame according to instructions and replace values
    lights_ = lights.iloc[
        instr.iloc[row]['from_x']:instr.iloc[row]['to_x']+1,
        instr.iloc[row]['from_y']:instr.iloc[row]['to_y']+1
        ]+i
    
    return lights_

# Part 1
# Get start time
start = time.time()

# Generate instructions data frame
instr = gen_instr_df()

# Generate lights data frame
lights = gen_lights_df()

# Iterate over all intructions in instructions data frame
for row in instr.index:

    # Generate intermediate dataframe with updated values for respective case
    if instr.iloc[row]['action'] == 'on':
        lights_ = switch_lights_part1({0:1})

    if instr.iloc[row]['action'] == 'off':
        lights_ = switch_lights_part1({1:0})

    if instr.iloc[row]['action'] == 'toggle':
        lights_ = switch_lights_part1({0:1, 1:0})
    
    # Update lights data frame with values from intermediate data frame
    lights.update(lights_)

# Get end time
end = time.time()

# Get elapsed time
total_time = end - start

# Get total number of turned on lights
print(f'\nPart 1',
      f'Total number of lit lights: {lights.sum().sum()}',
      f'Script execution time: {total_time:.2f} seconds', sep='\n')

# Part 2
# Get start time
start = time.time()

# Generate instructions data frame
instr = gen_instr_df()

# Generate lights data frame
lights = gen_lights_df()

# Iterate over all intructions in instructions data frame
for row in instr.index:

    # Generate intermediate dataframe with updated values for respective case
    if instr.iloc[row]['action'] == 'on':
        lights_ = switch_lights_part2(1)

    if instr.iloc[row]['action'] == 'off':
        lights_ = switch_lights_part2(-1)

        # Make sure that there are non negative values
        lights_ = lights_.mask(lights_ < 0, 0)

    if instr.iloc[row]['action'] == 'toggle':
        lights_ = switch_lights_part2(2)
    
    # Update lights data frame with values from intermediate data frame
    lights.update(lights_)

# Get end time
end = time.time()

# Get elapsed time
total_time = end - start

# Get total number of turned on lights
print(f'\nPart 2',
      f'Total brightness of all lights combined: {lights.sum().sum()}',
      f'Script execution time: {total_time:.2f} seconds', sep='\n')