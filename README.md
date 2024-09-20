# Virtual File System Shell Emulator

## Overview

This project provides a shell emulator that interacts with a virtual file system (VFS) stored in a zip archive. The shell emulator allows basic file system operations like navigating directories, listing contents, and checking the system uptime.

## Features

- **Navigate Directories**: Change directories using `cd`.
- **List Contents**: List files and folders with `ls`.
- **Print Current Directory**: Display the current working directory with `pwd`.
- **System Uptime**: Check how long the shell has been running with `uptime`.
- **Exiting**: Terminate the shell session and returns control to the terminal with `exit`.

## Files

- `shell.py`: The shell emulator script that uses the `VFS` class to interact with the virtual file system.
- `VFS.py`: Contains the `VFS` class, which handles the virtual file system operations.
- `example_root.zip`: A zip archive containing the virtual file system structure.
- `example_root/`: A folder with the same contents as `example_root.zip`, used for testing and comparison.
- `test_vfs.py`: Contains unit tests for the `VFS` class using the unittest framework.

## Installation

**Clone the Repository**:
   ```bash
   git clone https://github.com/l4nzel0d/dz1
   cd dz1
   ```

## How to use

**To launch**:
   ```bash
   python shell.py example_root.zip 
   ```
**To get help**:
   ```bash
   /$ help
   ```

**To test using unittest**:
```bash
python -m unittest test_vfs.py
```

## Author
---
Created by **l4nzel0d** aka **Boris Vasilyev**
