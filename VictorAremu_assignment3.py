# importing from os
import os

# Creating a variable of my location to read from
BASE_DIRECTORY = os.getcwd()
DATA_FOLDER = 'data'
IRIS_FILE = 'iris.csv'
REDUCED = 'reduced.csv'
read_location = os.path.join(BASE_DIRECTORY, DATA_FOLDER, IRIS_FILE)
write_location = os.path.join(BASE_DIRECTORY, DATA_FOLDER, REDUCED)

def read_data(location):
    with open(location, 'r') as file_object:
        return file_object.readlines()


data = read_data(read_location)

for row in data:
    print(row)


def write_data(write_location, file):
    with open(write_location, 'w') as f:
        return f.writelines()

write_data(write_location, data)


