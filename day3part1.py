from collections import defaultdict


def solution(line):
    UP_CHAR = "^"
    DOWN_CHAR = "v"
    RIGHT_CHAR = ">"
    LEFT_CHAR = "<"
    current_house_coords = (0,0)
    visited = set()
    visited.add(current_house_coords)
    for dir in line:
        if dir == UP_CHAR:
            current_house_coords = (current_house_coords[0], current_house_coords[1] + 1)
        elif dir == DOWN_CHAR:
            current_house_coords = (current_house_coords[0], current_house_coords[1] - 1)
        elif dir == RIGHT_CHAR:
            current_house_coords = (current_house_coords[0] + 1, current_house_coords[1])
        elif dir == LEFT_CHAR:
            current_house_coords = (current_house_coords[0] - 1, current_house_coords[1])
        visited.add(current_house_coords)
    print(visited)
    return len(visited)

f = open("day3part1_input.txt", "r")
for line in f:
    print(solution(line))
