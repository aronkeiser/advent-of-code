import numpy as np

# part 1

## read input and strip whitespaces
with open('2015/input/input_2015-02.txt', 'r') as input:
    data = input.read().strip()

## split data into list of presents
presents = data.split('\n')

## split presents into l, w, h
presents_dim = np.array([list(map(int, present.split('x'))) for present in presents])

presents_area = []

for present_dim in presents_dim:

    l = int(present_dim[0])
    w = int(present_dim[1])
    h = int(present_dim[2])

    ### get the two smallest dims
    smallest_dims = np.sort(present_dim)[:2]

    ### get paper needed for present
    present_area = np.sum([
        l * w * 2,
        l * h * 2,
        w * h * 2,
        smallest_dims[0] * smallest_dims[1]
        ])
    
    ### append are value to list of presents
    presents_area.append(present_area)

area = np.sum(presents_area)
print(f'they should order a total of {area} square feet of wrapping paper')

# part 2

presents_ribbon = []

for present_dim in presents_dim:

    l = int(present_dim[0])
    w = int(present_dim[1])
    h = int(present_dim[2])

    ### get the two smallest dims
    smallest_dims = np.sort(present_dim)[:2]

    ### get paper needed for present
    present_ribbon = np.sum([
        smallest_dims[0] * 2 + smallest_dims[1] * 2,
        l * w * h
        ])
    
    ### append are value to list of presents
    presents_ribbon.append(present_ribbon)

ribbon = np.sum(presents_ribbon)
print(f'they should order a total of {ribbon} feet of ribbon')