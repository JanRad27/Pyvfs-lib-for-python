# Pyvfs utitlities file

import core # Import the pyvfs core
import os # Importing the OS lib

class FileType():
    # File Type class
    def __init__(self, assoc: str):
        self.assoc = assoc

class Inode():
    registred = 0
    # Base Inode class
    def __init__(self, swap_priority: int = 1):
        # Adding settings to inode object
        self.inodeid = Inode.registred
        self.swap_priority = swap_priority

        # Adding new registred inode
        Inode.registred += 1

class File(Inode):
    # Directory class
    def __init__(self, type: FileType, data: str, swap_priority: int = 1):
        super().__init__(swap_priority)
        self.type = type
        self.data = data

    def get_type(self):
        return self.type

    def run(self):
        os.system(f"{self.type.assoc} {self.data}")

    def __call__(self):
        self.run()

class VFS(): # VFS class
    def __init__(self, name, prefix: str = "/", separator: str = "/", no_separate_prefix: bool = True):
        # Adding the settings to VFS object
        self.name = name
        self.prefix = prefix
        self.no_separate_prefix = no_separate_prefix
        self.separator = separator
        self.inode_list: list = []

        # Adding VFS to Core
        core.new_vfs(self)

    def add_inode(target: Inode):
        self.inode_list.append(target)
