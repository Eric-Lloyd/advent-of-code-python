#!/usr/bin/env python3

from dataclasses import dataclass
from functools import lru_cache
from typing import List, Optional

@dataclass(frozen=True)
class File:
    name: str
    size: int

@dataclass
class Directory:
    name: str
    parent: Optional["Directory"]
    childs: List["Directory"]
    files: List[File]

    @classmethod
    def init_dir(cls, name: str, parent: Optional["Directory"] = None):
        return cls(name=name, parent=parent, childs=[], files=[])

    def add_dir(self, dir: "Directory"):
        self.childs.append(dir)

    def add_file(self, file: File):
        self.files.append(file)

    def __hash__(self):
        return hash(self.name) + hash(self.parent)

    @lru_cache(maxsize=100)
    def size(self):
        file_sizes = sum([file.size for file in self.files])
        dir_sizes = sum([dir.size() for dir in self.childs])
        return file_sizes + dir_sizes

def is_command(line: str) -> bool:
    return line.startswith("$")

def is_open_dir_command(line: str) -> bool:
    return is_command(line) and "cd" in line and ".." not in line

def is_close_dir_command(line: str) -> bool:
    return is_command(line) and "cd" in line and ".." in line

def directory_name(line: str) -> str:
    return line.split(" ")[-1]

def is_sub_dir(line: str) -> bool:
    return line.startswith("dir")

def is_file(line: str) -> bool:
    return not is_sub_dir(line) and not is_command(line)

def file(line: str) -> File:
    size, name = line.split(" ")
    return File(name, int(size))


def build_directories(lines: List[str]) -> List[Directory]:
    directories = []
    root_dir_name = directory_name(lines[0])
    root_dir = Directory.init_dir(root_dir_name)
    directories.append(root_dir)
    curr_dir = root_dir

    for line in lines[1:]:
        if is_open_dir_command(line):
            dir_name = directory_name(line)
            dir = Directory.init_dir(name=dir_name, parent=curr_dir)
            curr_dir.add_dir(dir)
            directories.append(dir)
            curr_dir = dir
        if is_file(line):
            curr_dir.add_file(file=file(line))
        if is_close_dir_command(line):
            curr_dir = curr_dir.parent

    return directories


### EXECUTION ###
with open('input_data.txt', 'r') as input_data:
    lines = [line.strip() for line in input_data.readlines()]

dirs = build_directories(lines)

# part 1
UPPER_BOUND = 100000
result = sum([dir.size() for dir in dirs if dir.size() <= UPPER_BOUND])
print(result)


# part 2
root_size = dirs[0].size()
DISK_SPACE = 70000000
SPACE_NEEDED = 30000000
unused_space = DISK_SPACE - root_size
sorted_dirs_size = sorted([dir.size() for dir in dirs if dir.size()])
for size in sorted_dirs_size:
    if size + unused_space >= SPACE_NEEDED:
        print(size)
        break
