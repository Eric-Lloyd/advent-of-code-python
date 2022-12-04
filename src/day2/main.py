#!/usr/bin/env python

from typing import Tuple
from functools import reduce

SCORES = {
  "A X": (1 + 3, 3 + 0),
  "A Y": (2 + 6, 1 + 3),
  "A Z": (3 + 0, 2 + 6),
  "B X": (1 + 0, 1 + 0),
  "B Y": (2 + 3, 2 + 3),
  "B Z": (3 + 6, 3 + 6),
  "C X": (1 + 6, 2 + 0),
  "C Y": (2 + 0, 3 + 3),
  "C Z": (3 + 3, 1 + 6),
}

def map_score(encrypted_round: str) -> Tuple[int, int]:
  return SCORES[encrypted_round]

def add_score(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
  return (a[0] + b[0], a[1] + b[1])

with open('input_data.txt', 'r') as input_data:
  encrypted_rounds = [line.strip() for line in input_data.readlines()]

print(reduce(add_score, map(map_score, encrypted_rounds)))

