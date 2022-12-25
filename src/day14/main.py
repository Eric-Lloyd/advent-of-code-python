#!/usr/bin/env python3

from dataclasses import dataclass
from math import copysign
from typing import Dict, List, Tuple

@dataclass
class Grid:
  max_x: int
  max_y: int
  marked_points: Dict[Tuple[int], str]
  with_floor: bool
  sand_count: int = 0

  def is_blocked(self, x: int, y: int) -> bool:
    if self.with_floor and y == self.max_y + 2:
      return True
    return (x, y) in self.marked_points

  def add_rock(self, x: int, y: int) -> None:
    self.marked_points[(x, y)] = "#"  # rock

  def add_sand(self, x: int, y: int) -> None:
    self.marked_points[(x, y)] = "o"  # sand
    self.sand_count += 1

  def in_bound(self, x: int, y: int) -> bool:
    if self.with_floor:
      return True
    return 0 < x < self.max_x and 0 <= y < self.max_y

  @classmethod
  def build(cls, lines: List[Tuple[int]], with_floor: bool = False):
    max_x, max_y = (0, 0)
    for line in lines:
      for x, y in line:
        max_x, max_y = (max(max_x, x), max(max_y, y))
    grid = cls(max_x, max_y, {}, with_floor)
    for line in lines:
      for i in range(len(line) - 1):
        grid.build_rocks(line[i], line[i+1])
    grid.drop_all_sand()
    return grid

  def build_rocks(self, a: Tuple[int], b: Tuple[int]) -> None:
    ax, ay = a
    bx, by = b
    dx = bx - ax
    dy = by - ay
    diff = max(abs(dx), abs(dy))
    self.add_rock(ax, ay)
    self.add_rock(bx, by)
    for i in range(1, diff + 1):
      curr_dx = int(copysign(1, dx)) if dx else 0
      curr_dy = int(copysign(1, dy)) if dy else 0
      self.add_rock(ax + i * curr_dx, ay + i * curr_dy)

  def drop_all_sand(self) -> int:
    in_play = True
    while in_play:
      in_play = self.drop_sand()

  def drop_sand(self) -> bool:
    curr_x, curr_y = (500, 0)
    while self.in_bound(curr_x, curr_y) and not self.is_blocked(curr_x, curr_y):
      if not self.is_blocked(curr_x, curr_y + 1):  # straight below
        curr_y += 1
      elif not self.is_blocked(curr_x - 1, curr_y + 1):  # below left
        curr_x -= 1
        curr_y += 1
      elif not self.is_blocked(curr_x + 1, curr_y + 1):  # below right
        curr_x += 1
        curr_y += 1
      else:
        self.add_sand(curr_x, curr_y)
        return True
    return False


### EXECUTION ###
with open('input_data.txt', 'r') as input_data:
  lines = [
    list(map(lambda p: list(map(int, p.split(","))), l.strip().split(" -> ")))
    for l in input_data.readlines()
  ]

print(Grid.build(lines).sand_count)  # part 1
print(Grid.build(lines, with_floor = True).sand_count)  # part 2

