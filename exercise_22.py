# Read from a File

count_dict = {}

with open('Training_01.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.strip()
        line = line.split('/')
        if line[2] in count_dict:
            count_dict[line[2]] += 1
        else:
            count_dict[line[2]] = 1
        line = open_file.readline()

print(count_dict)
