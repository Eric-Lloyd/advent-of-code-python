#!/usr/bin/env python

from typing import List

def read_elves_calories() -> List[List[int]]:
  with open('input_data.txt', 'r') as input_data:
    elves_data = input_data.read().split("\n\n")

  return [[int(cal) for cal in elf_data.split()] for elf_data in elves_data]

elves_calories = read_elves_calories()

elf_calories_sums = sorted([sum(elf_calories) for elf_calories in elves_calories])

print(elf_calories_sums[-1]) # part 1
print(sum(elf_calories_sums[-3:])) # part 2
