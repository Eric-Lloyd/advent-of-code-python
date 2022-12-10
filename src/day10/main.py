#!/usr/bin/env python3

from typing import Dict, List

def increment_count(curr_count: int, counts: Dict[int, int]) -> int:
    curr_count += 1
    if curr_count in counts:
        counts[curr_count] = x
    return curr_count

def build_crt_row(
        curr_count: int,
        crt_row: List[str],
        crt_rows: List[List[str]],
        stripe: List[int],
) -> List[str]:
    """Function building the current CRT row for each cycle"""
    mod = cycle_count % 40
    check_count = curr_count - 1 if curr_count <= 40 else mod - 1
    curr_char = "#" if check_count in stripe else "."
    crt_row.append(curr_char)
    if mod == 0:  # new row:
        crt_rows.append(crt_row)
        return []
    return crt_row


### EXECUTION ###
with open('input_data.txt', 'r') as input_data:
    rows = [line.strip() for line in input_data.readlines()]

cycle_count = 0
x = 1
stripe = [x - 1, x, x + 1]
counts = {count:0 for count in range(20, 221, 40)}
crt_row = []  # current CRT row
crt_rows = []  # all CRT rows
for row in rows:
    if row == "noop":
        cycle_count = increment_count(cycle_count, counts)
        crt_row = build_crt_row(cycle_count, crt_row, crt_rows, stripe)
    else:  # double cycle
        cycle_count = increment_count(cycle_count, counts)
        crt_row = build_crt_row(cycle_count, crt_row, crt_rows, stripe)
        cycle_count = increment_count(cycle_count, counts)
        crt_row = build_crt_row(cycle_count, crt_row, crt_rows, stripe)
        value = int(row.split(" ")[-1])
        x += value
        stripe = [x - 1, x, x + 1]

# part 1
print(sum([k*v for k,v in counts.items()]))

# part 2
for crt_row in crt_rows:
    print(" ".join(crt_row))
