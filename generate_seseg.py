import os
from termcolor import colored

eseg_directory = "datasets/real_AICs/seg/"
seseg_directory = "datasets/real_AICs/sseg/"

eseg_files = [f for f in os.listdir(eseg_directory) if f.endswith('.eseg')]

mapping = {'1': '0.500000 0.000000', '2': '0.000000 0.500000'}

for eseg_file in eseg_files:
    print(eseg_file)
    with open(os.path.join(eseg_directory, eseg_file), 'r') as input_file:
        output_file_path = os.path.join(seseg_directory, eseg_file.replace('.eseg','.seseg'))
        with open(output_file_path,'w') as seseg_file:
            for line in input_file:
                line = line.strip()
                if line in mapping:
                    seseg_file.write(mapping[line] + '\n')

    print("Conversion complete : "+ colored(eseg_file, "red") + '   ---   ' + colored(output_file_path, "cyan"))
