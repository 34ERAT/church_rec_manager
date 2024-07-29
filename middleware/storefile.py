import shutil
import os

def StoreFile(root_path,src,dest):
    if  not os.path.exists(path=root_path):
        os.makedirs(root_path)

    if dest != src:
        shutil.copyfile(src=src,dst=dest)

