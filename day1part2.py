def solution(line):
    # ( +1
    # ) -1
    UP_CHAR = "("
    DOWN_CHAR = ")"
    floor = 0
    for i, char in enumerate(line):
        if char == UP_CHAR:
            floor += 1
        elif char == DOWN_CHAR:
            floor -= 1

        if floor == -1:
            return i + 1
    
    
f = open("day1part2_input.txt", "r")
for line in f:
    print(solution(line))
