#!/usr/bin/env python3

from dataclasses import dataclass
from queue import Queue
from typing import List, Tuple

@dataclass(frozen=True)
class Point:
  x: int
  y: int
  value: str

  def get_neighbors(self, rows: List[List[str]]) -> Tuple["Point"]:
    n = len(rows[0])
    m = len(rows)
    neighbors = []
    if self.x < n - 1:  # right
      nv = rows[self.y][self.x + 1]
      if ord(nv) - ord(self.value) <= 1:
        neighbors.append(Point(self.x + 1, self.y, nv))
    if self.x > 0:  # left
      nv = rows[self.y][self.x - 1]
      if ord(nv) - ord(self.value) <= 1:
        neighbors.append(Point(self.x - 1, self.y, nv))
    if self.y < m - 1:  # down
      nv = rows[self.y + 1][self.x]
      if ord(nv) - ord(self.value) <= 1:
        neighbors.append(Point(self.x, self.y + 1, nv))
    if self.y > 0:  # up
      nv = rows[self.y - 1][self.x]
      if ord(nv) - ord(self.value) <= 1:
        neighbors.append(Point(self.x, self.y - 1, nv))
    return tuple(neighbors)


def find_source_and_destination(rows: List[List[str]]) -> Tuple[Point]:
  s, d = None, None
  for i in range(len(rows[0])):
    for j in range(len(rows)):
      value = rows[j][i]
      if value == "S":
        s = Point(i, j, "a")  # replace source value
      if value == "E":
        d = Point(i, j, "z")  # replace destination value
  if not s or not d:
    raise Exception("Invalid input!")
  return s, d


def find_all_as(rows: List[List[str]]) -> Tuple[Point]:
  all_as = []
  for i in range(len(rows[0])):
    for j in range(len(rows)):
      value = rows[j][i]
      if value == "a":
        all_as.append(Point(i, j, "a"))
  return tuple(all_as)


def bfs(s: Point, d: Point, rows: List[List[str]]) -> int:
  q = Queue()
  q.put(s)
  prev = {}
  prev[s] = None
  visited = {s}

  while not q.empty():
    p = q.get()

    for n in p.get_neighbors(rows):
      if n not in visited:
        q.put(n)
        visited.add(n)
        prev[n] = p

  path = []
  p = d
  while p is not s:
    path.append(p)
    p = prev[p]

  return len(path)


### EXECUTION ###
with open('input_data.txt', 'r') as input_data:
  rows = [list(line.strip()) for line in input_data.readlines()]

source, destination = find_source_and_destination(rows)
rows[source.y][source.x] = "a"
rows[destination.y][destination.x] = "z"

# part 1
pl = bfs(source, destination, rows)
print(pl)

# part 2
ml = pl
for a in find_all_as(rows):
  try:
    pl = bfs(a, destination, rows)
    ml = min((pl, ml))
  except Exception:  # When there's no path, an error is thrown
    continue
print(ml)