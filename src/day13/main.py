#!/usr/bin/env python3

from functools import cmp_to_key
from itertools import zip_longest
from typing import List

def compare(p1: List, p2: List):
  for left, right in zip_longest(p1, p2):
    if left is None:
      return -1
    elif right is None:
      return 1
    comp = None
    if isinstance(left, int) and isinstance(right, int):
      comp = left - right
    else:
      if isinstance(left, List) and isinstance(right, List):
        comp = compare(left, right)
      else:  # type mismatch
        left = [left] if isinstance(left, int) else left
        right = [right] if isinstance(right, int) else right
        comp = compare(left, right)
    if comp and comp != 0:
      return comp // abs(comp)  # make sure it's always 1 or -1
  return 0


### Execution ###
with open('input_data.txt', 'r') as input_data:
  pairs = [
    tuple(map(eval, lines.strip().split('\n')))
    for lines in input_data.read().split("\n\n")
  ]

# part 1
index_sum = 0
for i, (left, right) in enumerate(pairs):
  if compare(left, right) == -1:
    index_sum += (i + 1)  # off by one error took me ages to figure out..
print(index_sum)

# part 2
pairs.append(([[2]], [[6]]))
packets = [packet for pair in pairs for packet in pair]  # flatten list of tuples
sorted_packets = sorted(packets, key=cmp_to_key(compare))
index_product = 1
for i, packet in enumerate(sorted_packets):
  if packet == [[2]] or packet == [[6]]:
    index_product *= (i + 1)
print(index_product)