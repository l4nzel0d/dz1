import time
import zipfile
import os

# Virtual File System
class VFS:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.current_dir = '/'
        self.file_structure = {}
        self.start_time = time.time()
        self.load_zip()
    
    def load_zip(self):
        with zipfile.ZipFile(self.zip_path, 'r') as z:
            for obj_path in z.namelist(): # here obj_path is a path to either a file or directory
                print(obj_path)
                
                parts = obj_path.strip('/').split('/')
                current_level = self.file_structure

                for part in parts:
                    if part == parts[-1] and not obj_path.endswith('/'):
                        current_level[part] = "f"
                    else:
                        current_level = current_level.setdefault(part, {})
        print(self.file_structure)

    def cd(self, path):
        # root
        if path == "/":
            self.current_dir = path
            return 
        
        
        # parent directory
        if path[0:2] == "..":
            if self.current_dir == '/':
                return
            
            parts = self.current_dir.strip('/').split('/')[:-1]
            directory = '/'
            for part in parts:
                directory += part + '/'
            self.current_dir = directory
            return
        
        # absolute or relative path
        if path[0] == '/': 
            abs_path = path
        else:
            abs_path = self.current_dir + path 

        # ensure directory ends with a slash
        if abs_path[-1] != '/':
            abs_path += '/'

        if self.get_dictionary_from_absolute_path(abs_path) == None:
            print(f"{abs_path}: No such directory")
        else: 
            self.current_dir = abs_path
        return
        

    def get_dictionary_from_absolute_path(self, path):
        if path == "/":
            return self.file_structure 

        parts = path.strip('/').split('/')
        current_level = self.file_structure
        for part in parts:
            if part in current_level and current_level[part] != 'f':
                current_level = current_level[part]
            else:
                return None
            
        return current_level

    def pwd(self):
        print(self.current_dir)
    


    def uptime(self):
        uptime_duration = time.time() - self.start_time
        print(f"Uptime: {uptime_duration:.2f} seconds")
