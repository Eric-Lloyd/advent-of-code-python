#!/usr/bin/env python3

def is_marker(s: str) -> bool:
    return len(set(s)) == len(s)

def find_marker(subroutine: str, marker_size: int) -> int:
    for start in range(len(subroutine)):
        end = start + marker_size
        if is_marker(subroutine[start:end]):
            return end


with open('input_data.txt', 'r') as input_data:
    subroutine = [line.strip() for line in input_data.readlines()][0]

print(find_marker(subroutine, 4)) # part 1
print(find_marker(subroutine, 14)) # part 2