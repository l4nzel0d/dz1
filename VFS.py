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
                
                parts = obj_path.strip('/').split('/')
                current_level = self.file_structure

                for part in parts:
                    if part == parts[-1] and not obj_path.endswith('/'):
                        current_level[part] = "f"
                    else:
                        current_level = current_level.setdefault(part, {})

    def cd(self, path): 
        parsed_path = self.path_parser(path)
        if self.get_dictionary_from_absolute_path(parsed_path) is None:
            print(f"shell.py: cd: {path}: no such directory")
        else:
            self.current_dir = parsed_path

    def path_parser(self, path):
        if path.startswith("/"):
            abs_path = path
        else:
            abs_path = self.current_dir + path
        
        parts = abs_path.split('/')

        final_parts = []

        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == "..":
                if final_parts:
                    final_parts.pop()
            else:
                final_parts.append(part)
        
        final_path = '/' + '/'.join(final_parts) + '/'

        final_path = final_path.replace('//', '/')
        if final_path == '':
            final_path = '/'
        
        return final_path

        

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
        return self.current_dir
    
    
    def ls(self, path="."):
        parsed_path = self.path_parser(path)
        directory_dict = self.get_dictionary_from_absolute_path(parsed_path)
        return path, directory_dict


    def uptime(self):
        uptime_duration = time.time() - self.start_time
        return uptime_duration
