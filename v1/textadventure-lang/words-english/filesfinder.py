import os
import json
def get_filenames_list(path):
    """
    Returns a list of filenames in the given directory path.
    """
    try:
        filenames = os.listdir(path)
        return filenames
    except FileNotFoundError:
         return f"Error: Directory not found: {path}"
    except NotADirectoryError:
        return f"Error: Not a directory: {path}"
    
# Example usage:
path = "D:/words-english/files/" # Replace with the actual path
filenames_list = get_filenames_list(path)

for cfile in filenames_list:
    if cfile.startswith("tempa"):
        with open(f"{cfile}") as cfile2:
            
            loaded_json = json.load(cfile2)
        word = list(dict(loaded_json).values())[2]
        if os.path.isfile(f"{word}.json"):
            #with open(f"{cfile}") as cfile4:
            #    load_new = json.load(cfile4)
            #desc_new = list(dict(load_new).values())[5]
            #with open(rf"{word}.json", "rt+") as cfile3:
            #    print(word)
            #    load_old = json.load(cfile3)
            #    data = cfile3.read()
            #    desc_old = list(dict(load_old).values())[5]
            #    dict1 = dict(load_old)
            #    dict1['desc2'] = desc_new
            #    newdata = ", 'desc2': ['%s']}" % (desc_new)
            #    data = data.replace("}", newdata)
            #    with open(rf"{word}.json", "w") as writefile:
            #
            #        writefile.write(data)
            #        writefile.close()
            #    cfile3.close()
            #   exit()
            for i in range(100):
                if os.path.isfile(f"{word}_{i+2}.json"):
                    continue
                else:
                    os.system(f"ren {cfile} {word}_{i}.json")
            
            

        else:
            os.system(f"ren {cfile} {word}.json")
    else:
        continue
    
