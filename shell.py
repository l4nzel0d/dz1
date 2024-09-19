import argparse
from VFS import VFS

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
            vfs.uptime()

        elif command == "pwd":
            vfs.pwd()
        
        elif command == "cd":
            if len(args) == 1:
                vfs.cd(args[0])
            else:
                print("Usage: cd path")
        
        elif command == "ls":
            if len(args) == 1:
                vfs.ls(args[0])
            elif len(args) == 0:
                vfs.ls()
            else:
                print("Usage: ls [directory]")
                print("  Lists the contents of the current directory if no directory is specified.")
                print("  Lists the contents of the specified directory if a directory is provided.")
                print("Examples:")
                print("  ls            # List contents of the current directory")
                print("  ls folder1    # List contents of 'folder1' directory")

        else:
            print("Unknown command")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shell emulator with virtual file system.")
    parser.add_argument("zip_path", help="Path to the zip file containing the virtual file system.")
    args = parser.parse_args()

    vfs = VFS(args.zip_path)
    shell(vfs)