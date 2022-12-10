#!/usr/bin/env python3

with open('input_data.txt', 'r') as input_data:
    rows = [
        list(map(int, line.strip()))
        for line in input_data.readlines()
    ]

n = len(rows)
columns = [list(i) for i in zip(*rows)] # transpose rows


### PART 1 ###
visible_tree_count = (n * 4) - 4 # initialise with outer trees
for i in range(1, n - 1):
    column = columns[i]
    for j in range(1, n - 1):
        curr_value = rows[j][i]
        is_visible = False
        row = rows[j]
        max_left = max(row[0:i])
        if curr_value > max_left:
            visible_tree_count += 1
            continue
        max_right = max(row[i+1:])
        if curr_value > max_right:
            visible_tree_count += 1
            continue
        max_top = max(column[0:j])
        if curr_value > max_top:
            visible_tree_count += 1
            continue
        max_bottom = max(column[j+1:])
        if curr_value > max_bottom:
            visible_tree_count += 1
            continue

print(visible_tree_count)



### PART 2 ###
max_scenic_score = 0
for i in range(1, n - 1):
    column = columns[i]
    for j in range(1, n - 1):
        curr_value = rows[j][i]
        row = rows[j]

        view_left = 1
        left_index = i-1
        left_neighbor = row[left_index]
        while left_neighbor < curr_value and left_index > 0:
            view_left += 1
            left_index -= 1
            left_neighbor = row[left_index]

        view_right = 1
        right_index = i+1
        right_neighbor = row[right_index]
        while right_neighbor < curr_value and right_index < n - 1:
            view_right += 1
            right_index += 1
            right_neighbor = row[right_index]

        view_top = 1
        top_index = j-1
        top_neighbor = column[top_index]
        while top_neighbor < curr_value and top_index > 0:
            view_top += 1
            top_index -= 1
            top_neighbor = column[top_index]

        view_bottom = 1
        bottom_index = j+1
        bottom_neighbor = column[bottom_index]
        while bottom_neighbor < curr_value and bottom_index < n - 1:
            view_bottom += 1
            bottom_index += 1
            bottom_neighbor = column[bottom_index]

        scenic_score = view_left * view_right * view_top * view_bottom
        max_scenic_score = max((scenic_score, max_scenic_score))

print(max_scenic_score)