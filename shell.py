import argparse
from VFS import VFS

def help_text():
    return """
Available commands:
- **`cd <path>`**: Change the current directory to `<path>`.
- **`ls [directory]`**: List the contents of the specified directory, or the current directory if no directory is provided.
- **`pwd`**: Print the current working directory.
- **`uptime`**: Show the amount of time the shell has been running.
- **`exit`**: Terminate the shell session and return control to the terminal.
- **`help`**: Display this help text with a summary of all available commands.
"""

def shell(vfs):
    while True:
        line = input(f"{vfs.current_dir}$ ").strip()
        if not line:
            continue
        parts = line.split()
        command = parts[0]
        args = parts[1:]

        if command == "exit":
            print("Exiting shell.")
            break

        elif command == "uptime":
            uptime_duration = vfs.uptime()
            print(f"Uptime: {uptime_duration:.2f} seconds")

        elif command == "pwd":
            print(vfs.pwd())
        
        elif command == "cd":
            if len(args) == 1:
                vfs.cd(args[0])
            else:
                print("Usage: cd <path>")
        
        elif command == "ls":
            if len(args) == 1:
                path, directory_dict = vfs.ls(args[0])
            elif len(args) == 0:
                path, directory_dict = vfs.ls()
            else:
                print("Usage: ls [directory]")
                print("  Lists the contents of the current directory if no directory is specified.")
                print("  Lists the contents of the specified directory if a directory is provided.")
                print("Examples:")
                print("  ls            # List contents of the current directory")
                print("  ls folder1    # List contents of 'folder1' directory")
                continue
            

            if directory_dict is None:
                print(f"shell.py: ls: {path}: no such directory")
            else:
                print("\t\t".join(sorted([keys for keys in directory_dict])))

        elif command == "help":
            print(help_text())

        else:
            print("Unknown command")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shell emulator with virtual file system.")
    parser.add_argument("zip_path", help="Path to the zip file containing the virtual file system.")
    args = parser.parse_args()

    vfs = VFS(args.zip_path)
    shell(vfs)