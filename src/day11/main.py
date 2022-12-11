#!/usr/bin/env python3

from collections import deque
from dataclasses import dataclass
from functools import reduce
from typing import Callable, Dict, List


@dataclass
class Monkey:
  id: int
  items: deque
  operation: Callable[[int], int]
  test: int
  actions: Dict[bool, int]
  inspect_count: int = 0

  @classmethod
  def parse(cls, lines: List[str]):
    id = int(lines[0][-2])
    l = lines[1].split(":")[-1].replace(" ", "").split(",")
    items = deque(map(int, l))
    operation = eval('lambda old: ' + lines[2].split("= ")[-1])
    test = int(lines[3].split(" ")[-1])
    actions = {
      True: int(lines[4].split(" ")[-1]),
      False: int(lines[5].split(" ")[-1]),
    }
    return cls(id, items, operation, test, actions)

  def pop(self) -> int:
    self.inspect_count += 1
    return self.items.popleft()

  def push(self, elem: int) -> None:
    self.items.append(elem)

  def transform(self, old: int) -> int:
    return self.operation(old)

  def throw_to(self, worry_level) -> int:
    divisible = worry_level % self.test == 0
    return self.actions[divisible]


def monkey_business(monkey_data: List[str], n_rounds: int, relief: bool) -> None:
  monkeys = [Monkey.parse(m) for m in monkey_data]
  magic_product = reduce(lambda a, b: a * b, (m.test for m in monkeys))
  for _ in range(n_rounds):
    for monkey in monkeys:
      items_count = len(monkey.items)
      for _ in range(items_count):
        worry_level = monkey.pop()
        worry_level = monkey.transform(worry_level)
        worry_level = worry_level // 3 if relief else worry_level % magic_product
        monkey_to = monkey.throw_to(worry_level)
        monkeys[monkey_to].push(worry_level)

  counts = (m.inspect_count for m in monkeys)
  first, second, *_ = sorted(counts, reverse=True)
  print(first * second)


### EXECUTION ###
with open('input_data.txt', 'r') as input_data:
  monkey_data = [
    list(map(str.strip, monkey_data.split("\n")))
    for monkey_data in input_data.read().split("\n\n")
  ]

monkey_business(monkey_data, n_rounds=20, relief=True)  # part 1
monkey_business(monkey_data, n_rounds=10000, relief=False)  # part 2
