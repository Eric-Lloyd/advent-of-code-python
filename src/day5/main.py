#!/usr/bin/env python3

from collections import deque, namedtuple
from typing import Callable, List

# q: quantity, f: from, t: to
Instruction = namedtuple("Instruction", "q f t")

def build_instructions(rows: List[str]) -> List[Instruction]:
    instructions = []
    for row in rows:
        q, f, t = [int(s) for s in row.strip().split(" ") if s.isnumeric()]
        instructions.append(Instruction(q, f, t))
    return instructions


def build_stacks(crates: List[str]) -> List[deque]:
    stacks = []
    for j in range(len(crates[1])):
        stack = deque()
        # traverse from the back to have the right element at the top.
        for i in range(len(crates) - 1, -1, -1):
            elem = crates[i][j]
            if elem.isalpha():
                stack.append(elem)
        if stack:
            stacks.append(stack)

    return stacks


def p1_handler(stack_from, stack_to, instruction: Instruction):
    for _ in range(instruction.q):
        elem = stack_from.pop()
        stack_to.append(elem)


def p2_handler(stack_from, stack_to, instruction: Instruction):
    elems_to_move = []
    for i in range(instruction.q):
        elem = stack_from.pop()
        elems_to_move.insert(0, elem)
    for elem in elems_to_move:
        stack_to.append(elem)


def rearange(
        crates: List[str],
        instructions: List[Instruction],
        handler: Callable,
):
    stacks = build_stacks(crates)
    for instruction in instructions:
        stack_from = stacks[instruction.f - 1] # 0-based index
        stack_to = stacks[instruction.t - 1] # 0-based index
        handler(stack_from, stack_to, instruction)

    # peek the top of each stacks
    result = "".join([stack[-1] for stack in stacks])
    print(result)



with open('input_data.txt', 'r') as input_data:
    rows = [line for line in input_data.readlines()]

split = 9 # may be a different number for different input sizes
instructions = build_instructions(rows[split + 1:])
crates = rows[0:split]
rearange(crates, instructions, p1_handler)
rearange(crates, instructions, p2_handler)