#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Set, List, Tuple

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def move(self, dx: int, dy: int) -> "Point":
        return Point(self.x + dx, self.y + dy)

    def is_touching(self, other: "Point") -> bool:
        return max(abs(self.x - other.x), abs(self.y - other.y)) <= 1


@dataclass(frozen=True)
class Instruction:
    direction: str
    distance: int

    @property
    def dx(self) -> int:
        if self.direction == "L":
            return -1
        if self.direction == "R":
            return 1
        return 0

    @property
    def dy(self) -> int:
        if self.direction == "D":
            return -1
        if self.direction == "U":
            return 1
        return 0

def parse_instruction(line: str) -> Instruction:
    l, r = line.strip().split(" ")
    return Instruction(l, int(r))

def magic(d) -> int:
    return d // abs(d)

def handle_instruction(
        instruction: Instruction,
        points: List[Point],
        visited: Set[Point],
) -> Tuple[Point]:
    for _ in range(instruction.distance):
        h, *_ = points
        h = h.move(instruction.dx, instruction.dy)
        points[0] = h
        previous = h
        for i in range(1, len(points)):
            curr = points[i]
            dx = previous.x - curr.x
            dy = previous.y - curr.y
            if previous.is_touching(curr):
                pass
            elif dx == 0: # vertical
                curr = curr.move(0, magic(dy))
            elif dy == 0: # horizontal
                curr = curr.move(magic(dx), 0)
            else: # diagonal
                curr = curr.move(magic(dx), magic(dy))
            points[i] = curr
            previous = points[i]
            if i == len(points) - 1:
                visited.add(points[i])

    return points


def tail_size(n: int, instructions: List[Instruction]) -> int:
    points = [Point(0, 0) for _ in range(n)]
    visited: Set[Point] = {points[-1]}

    for inst in instructions:
        points = handle_instruction(inst, points, visited)

    return len(visited)


### EXECUTION ###
with open('input_data.txt', 'r') as input_data:
    instructions = [
        parse_instruction(line)
        for line in input_data.readlines()
    ]

print(tail_size(2, instructions))  # part 1
print(tail_size(10, instructions)) # part 2