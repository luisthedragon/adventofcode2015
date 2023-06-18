def solution(line):
    # ( +1
    # ) -1
    UP_CHAR = "("
    DOWN_CHAR = ")"
    floor = 0
    for char in line:
        if char == UP_CHAR:
            floor += 1
        elif char == DOWN_CHAR:
            floor -= 1

    return floor


f = open("day1part1_input.txt", "r")
for line in f:
    print(solution(line))
