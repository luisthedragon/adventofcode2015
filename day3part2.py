def solution(line):
    UP_CHAR = "^"
    DOWN_CHAR = "v"
    RIGHT_CHAR = ">"
    LEFT_CHAR = "<"
    santa_coords = (0,0)
    robot_coords = (0,0)
    visited = set()
    visited.add(santa_coords)
    for i, dir in enumerate(line):
        if i % 2 == 0:
            current_coords = robot_coords
        else:
            current_coords = santa_coords
        if dir == UP_CHAR:
            current_coords = (current_coords[0], current_coords[1] + 1)
        elif dir == DOWN_CHAR:
            current_coords = (current_coords[0], current_coords[1] - 1)
        elif dir == RIGHT_CHAR:
            current_coords = (current_coords[0] + 1, current_coords[1])
        elif dir == LEFT_CHAR:
            current_coords = (current_coords[0] - 1, current_coords[1])
        visited.add(current_coords)
        # update santa and robot coords
        if i % 2 == 0:
            robot_coords = current_coords
        else:
            santa_coords = current_coords
    print(visited)
    return len(visited)

f = open("day3part2_input.txt", "r")
for line in f:
    print(solution(line))
