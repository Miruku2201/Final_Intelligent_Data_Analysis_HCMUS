import json 
import os

def update(new, key, filename):
    with open(filename, "r+") as file:
        file_data = json.load(file)
        file_data[key].append(new)
        file.seek(0)
        json.dump(file_data, file, indent=4)
        
def create(path, key):
    is_file_existed = os.path.exists(path)
    if not is_file_existed:
        json_object = json.dumps({key: []}, indent=4)
        with open(path, "w") as fwrite:
            fwrite.write(json_object)