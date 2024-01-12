import math

def read_parameters_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    parameters = {}
    
    for line in lines:
        key, value = line.strip().split(':')
        if key == 'DieSize':
            parameters[key] = [int(val) for val in value.split('x')]
        elif key in ['DieShiftVector', 'ReferenceDie']:
            parameters[key] = tuple(map(int, value.strip('()').split(',')))
        else:
            parameters[key] = int(value)
    
    return parameters

file_path = 'Testcase12.txt'
parameters = read_parameters_from_file(file_path)

wafer_diameter = parameters['WaferDiameter']
die_size = parameters['DieSize']
die_shift_vector = parameters['DieShiftVector']
cow_to_reference_die = parameters['ReferenceDie']

die_indices = []
llcs = []
distance_from_center=0

if die_shift_vector[0]==0:
    pass
else:
    die_shift_vector[0]=0

if die_shift_vector[1]==0:
    pass
else:
    die_shift_vector[0]=0


num_dies_x = int(wafer_diameter / die_size[0])
num_dies_y = int(wafer_diameter / die_size[1])


for x in range(0, num_dies_x):
    for y in range(0, num_dies_y):
        die_x = x * die_size[0] + die_shift_vector[0] 
        die_y = y * die_size[1] + die_shift_vector[1] 

        distance_from_center=distance_from_center+die_size[0]
        if distance_from_center <= wafer_diameter / 2:

            die_index = f"({x},{y})"
            llc = f"({die_x:.4f}, {die_y:.4f})"
            die_indices.append(die_index)
            llcs.append(llc)
    distance_from_center=30

for x in range(-1, num_dies_x):
    for y in range(-1, num_dies_y):
        die_x = x * die_size[0] + die_shift_vector[0] 
        die_y = y * die_size[1] + die_shift_vector[1] 

        distance_from_center=distance_from_center+die_size[0]
        if distance_from_center <= wafer_diameter / 2:

            die_index = f"({x},{y})"
            llc = f"({die_x:.4f}, {die_y:.4f})"
            die_indices.append(die_index)
            llcs.append(llc)
    distance_from_center=30
for i in range(len(die_indices)):
    print(f"{die_indices[i]}:{llcs[i]}")

    

