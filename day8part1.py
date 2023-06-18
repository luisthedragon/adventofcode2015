f = open("day8part1_input.txt", "r")

total = 0
for i, line in enumerate(f):
    line = line.strip()
    code_line_len = len(line)
    memory_line = bytes(line, "utf-8").decode("unicode_escape")
    memory_line_len = len(memory_line) - 2
    line_len_diff = code_line_len - memory_line_len
    total += line_len_diff

print(total)