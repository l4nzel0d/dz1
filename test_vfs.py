import unittest
import zipfile
import os
import time
from VFS import VFS

class TestVFS(unittest.TestCase):
    expected_structure =  {
        "folder1": 
        {
            "folder1.1": {},
            "folder1.2": {},
            "file1.txt" : "f"
        },
        "folder2": 
        {
            "file2.txt" : "f"
        },
        "file3.txt": "f"
    }
            
    def setUp(self):
        self.zip_filename = "test_vfs.zip"
        with zipfile.ZipFile(self.zip_filename, 'w') as zf:
            zf.writestr("folder1/", "")
            zf.writestr("folder1/folder1.1/", "")
            zf.writestr("folder1/folder1.2/", "")
            zf.writestr("folder1/file1.txt", "This is file1.")
            zf.writestr("folder2/file2.txt", "This is file2.")
            zf.writestr("file3.txt", "This is file3.")
        
        self.vfs = VFS(self.zip_filename)

    def tearDown(self):
        if os.path.exists(self.zip_filename):
            os.remove(self.zip_filename)
    
    def test_load_zip(self):
        self.assertEqual(self.vfs.file_structure, self.expected_structure)
    
    def test_cd(self):
        self.vfs.cd("folder1")
        self.assertEqual(self.vfs.current_dir, "/folder1/")

        self.vfs.cd("nonexistent")
        self.assertEqual(self.vfs.current_dir, "/folder1/")

        self.vfs.cd(".././folder1/../../folder1/folder1.2/")
        self.assertEqual(self.vfs.current_dir, "/folder1/folder1.2/")
    

    def test_pwd(self):
        self.assertEqual(self.vfs.pwd(), "/")

        self.vfs.cd("folder1")
        self.assertEqual(self.vfs.pwd(), "/folder1/")

    def test_ls(self):
        first_list = ["file3.txt", "folder1", "folder2"]
        self.assertEqual(sorted((self.vfs.ls()[1]).keys()), first_list)

        second_list = ["file1.txt", "folder1.1", "folder1.2"]
        self.assertEqual(sorted((self.vfs.ls("folder1")[1]).keys()), second_list)

    def test_path_parser(self):
        self.assertEqual(self.vfs.path_parser("."), "/")
        self.assertEqual(self.vfs.path_parser("folder1/./..//folder2//.//"), "/folder2/")

    def test_get_dictionary_from_absolute_path(self):
        self.assertEqual(self.vfs.get_dictionary_from_absolute_path("/"), self.vfs.file_structure)
        self.assertEqual(self.vfs.get_dictionary_from_absolute_path("folder1"), self.vfs.file_structure["folder1"])

    def test_uptime(self):
        time.sleep(1)
        self.assertGreater(self.vfs.uptime(), 1)
        self.assertLess(self.vfs.uptime(), 4)

        time.sleep(1)
        self.assertGreater(self.vfs.uptime(), 2)
        self.assertLess(self.vfs.uptime(), 5)


if __name__ == "__main__":
    unittest.main()