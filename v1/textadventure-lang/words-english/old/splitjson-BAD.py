import os
import json
from itertools import islice

def split_json(
    data_path,
    file_name,
    size_split=1000,
):
    """Split a big JSON file into chunks.
    data_path : str, "data_folder"
    file_name : str, "data_file" (exclude ".json")
    """
    with open(os.path.join(data_path, file_name + ".json"), "r") as f:
        whole_file = json.load(f)

    split = len(whole_file) # size_split

    for i in range(split + 1):
        with open(os.path.join(data_path, file_name + "_"+ str(split+1) + "_" + str(i+1) + ".json"), 'w') as f:
            json.dump(dict(islice(whole_file.items(), i*size_split, (i+1)*size_split)), f)
    return
split_json(".", "english", 1000)