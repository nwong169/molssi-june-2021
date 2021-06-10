import os
import argparse

parser = argparse.ArgumentParser("This script parses mdout files to extract the total energy")
parser.add_argument("filepath", help = "The filepath to the file to be analyzed")

args = parser.parse_args()


filename = args.filepath
f = open(filename, 'r')
data = f.readlines()
f.close()

print(f"Analayzing {filename}")

output_filename = os.path.basename(filename)
output_filename = output_filename.split('.')[0]
output_filename = F"{output_filename}_Etot.txt"

f_write = open(output_filename, 'w+')
energies = []

for line in data:
    if 'Etot' in line:
        split_line = line.split()
        energies.append(float(split_line[2]))
        f_write.write(F' \t {energies} \n')
f_write.close()

print(f"Done analyzing {filename}")

