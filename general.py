#function to create dir check if already exist
import os


def create_dir(dirctory):
    if not os.path.exists(dirctory):
        os.makedirs(dirctory)

def write_file(path, data):
    f=open(path, 'w')
    f.write(data)
    f.close()