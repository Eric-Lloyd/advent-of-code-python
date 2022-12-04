#!/usr/bin/env python

from functools import reduce
from typing import List, Set


def common_letter_priority(sets: List[Set[str]]) -> int:
  """Finds the priority of the common letter in a list of sets"""
  intersection = reduce(lambda s1, s2: s1.intersection(s2), sets)
  assert len(intersection) == 1
  letter = intersection.pop()
  return ord(letter) - 96 if letter.islower() else ord(letter) - 38

def map_rucksack(row: str) -> int:
  mid = len(row) // 2
  sets = [set(row[0:mid]), set(row[mid:])]
  return common_letter_priority(sets)

def map_group(group: List[str]) -> int:
  sets = [set(s) for s in group]
  return common_letter_priority(sets)


with open('input_data.txt', 'r') as input_data:
    rows = [line.strip() for line in input_data.readlines()]

total_part1 = sum([map_rucksack(row) for row in rows])
print(total_part1)

n = 3
groups = (rows[i:i + n] for i in range(0, len(rows), n))
total_part2 = sum([map_group(group) for group in groups])
print(total_part2)

