import hashlib
import os 

def hash_file(filepath):
    os.chdir(filepath)
    files = os.listdir(filepath)
    
    hash_dir = {}
    
    for filename in files:
        h = hashlib.sha1()
        hash_list = []
        with open(filename,'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)
            hash_list.append(h.hexdigest())
            if h.hexdigest() in hash_dir:
                hash_dir[h.hexdigest()].append(filename)
            else:
                hash_dir[h.hexdigest()] = [filename]
    return hash_dir

filepath = input("Enter the file path: ")
msg = hash_file(filepath)
for key, value in msg.items():
    if len(value) > 1:
        print("Duplicate files found:", value)