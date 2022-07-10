import os
import sys

file_path_dir = sys.argv[1]

def file_handler(file_path):
    f = open(file_path, 'r')
    return f
    
file_name = 0
for f in os.listdir(file_path_dir):
    if not f.startswith('.'):
        file_path = file_path_dir + "/" + f
        content_list = []
    
        file = file_handler(file_path)
        for line in file:
            content_list.append(line.strip())

        print('\t'.join([str(file_name), ' '.join(content_list)]))

        file_name += 1



