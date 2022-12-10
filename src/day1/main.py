#!/usr/bin/env python3

from typing import List
import heapq

# Here you should replace the content of the 'input_data.txt' file with your current day input data.
with open('input_data.txt', 'r') as input_data:
    rows = [line.strip() for line in input_data.readlines()]


def day_one_part_1(rows: List[str]) -> int:
  current_max_elf_calories = 0
  current_elf_calories = 0
  for row in rows:
    if row == "": # this signifies a new elf
      current_max_elf_calories = max([current_max_elf_calories, current_elf_calories])
      current_elf_calories = 0
    else:
      carried_calories = int(row)
      current_elf_calories += carried_calories
  return current_max_elf_calories


def day_one_part_2(rows: List[str], queue_size: int) -> int:
  # initiliaze a priority queue using a heap
  heap = []
  current_elf_calories = 0
  for row in rows:
    if row == "": # this signifies a new elf
      if len(heap) >= queue_size:
        # remove minimum element if the heap has reached max queue_size
        # push current element to the heap
        heapq.heappushpop(heap, current_elf_calories)
      else:
        # push current element to the heap
        heapq.heappush(heap, current_elf_calories)
      # make sure heap is in priority order
      heapq.heapify(heap)
      current_elf_calories = 0
    else:
      carried_calories = int(row)
      current_elf_calories += carried_calories

  calories_sum = 0
  for calories in heap:
    calories_sum += calories
  return calories_sum


print(day_one_part_1(rows))
print(day_one_part_2(rows, 3))



