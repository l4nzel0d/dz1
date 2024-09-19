import zipfile
import os

# Virtual File System
class VFS:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.current_dir = '/'
        self.file_structure = {}
        self.load_zip()
    
    def load_zip(self):
        with zipfile.ZipFile(self.zip_path, 'r') as z:
            for file in z.namelist():
                print(file)

if __name__ == "__main__":
    vfs = VFS("dz1/example_root.zip")