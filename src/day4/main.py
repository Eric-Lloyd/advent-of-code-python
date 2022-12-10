#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Pair:
  left: int
  right: int

  @staticmethod
  def parse(l: List[str]) -> "Pair":
    left, right = [int(s) for s in l.split("-")]
    return Pair(left, right)

  def is_fully_contained_by(self, other: "Pair") -> bool:
    return self.left >= other.left and self.right <= other.right

  def is_overlapped_by(self, other: "Pair") -> bool:
    return (
      other.left <= self.left <= other.right or
      other.left <= self.right <= other.right
    )


@dataclass(frozen=True)
class Couple:
  left: Pair
  right: Pair

  @staticmethod
  def parse(line: str) -> "Couple":
    left_pair, right_pair = line.split(",")
    return Couple(Pair.parse(left_pair), Pair.parse(right_pair))

  def has_fully_contained_pairs(self) -> bool:
    return (
      self.left.is_fully_contained_by(self.right) or
      self.right.is_fully_contained_by(self.left)
    )

  def has_overlapping_pairs(self) -> bool:
    return (
      self.left.is_overlapped_by(self.right) or
      self.right.is_overlapped_by(self.left)
    )


with open('input_data.txt', 'r') as input_data:
    couples = [
      Couple.parse(line.strip())
      for line in input_data.readlines()
    ]

fully_contained_pairs_count = 0
overlapping_pairs_count = 0
for couple in couples:
  if couple.has_fully_contained_pairs():
    fully_contained_pairs_count += 1
  if couple.has_overlapping_pairs():
    overlapping_pairs_count += 1

print(fully_contained_pairs_count) # part 1
print(overlapping_pairs_count) # part 2

