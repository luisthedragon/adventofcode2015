import re

TURN_ON = 0
TURN_OFF = 1
TOGGLE = 2

def instruction_parser(instruction):
    if instruction.startswith("turn on"):
        instruction_code = TURN_ON
    elif instruction.startswith("turn off"):
        instruction_code = TURN_OFF
    elif instruction.startswith("toggle"):
        instruction_code = TOGGLE
    m = re.findall('\d*,\d*', instruction)
    x1, y1 = map(int, m[0].split(","))
    x2, y2 = map(int, m[1].split(","))
    return instruction_code, x1, y1, x2, y2

def solution(instruction, grid):
    instruction_code, x1, y1, x2, y2 = instruction_parser(instruction)
    x_dist = x2 - x1
    y_dist = y2 - y1
    for i in range(x_dist + 1): # 0 1
        for j in range(y_dist + 1): # 0 1
            if instruction_code == TURN_ON:
                grid[x1+i][y1+j] += 1
            elif instruction_code == TURN_OFF:
                if grid[x1+i][y1+j] > 0:
                    grid[x1+i][y1+j] -= 1
            elif instruction_code == TOGGLE:
                grid[x1+i][y1+j] += 2

f = open("day6part1_input.txt", "r")
grid = [[0] * 1000 for i in range(1000)]
for line in f:
    solution(line, grid)

total = 0
for row in grid:
    for cell in row:
        total += cell

print(total)
