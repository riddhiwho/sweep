import hashlib
import os 

def list_files(startpath):
    hash_dir = {}
    for root, dirs, files in os.walk(startpath):
        for file in files:
            filename = (os.path.join(root, file))
            # print(filename)
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

if __name__ == "__main__":
    filepath = input("Enter the file path: ")
    msg = list_files(filepath)
    for key, value in msg.items():
        if len(value) > 1:
            print("Duplicate files found:", value)