def transfrom_string(string):
    new_str = ""
    for char in string:
        new_str += transform_char(char)
    return new_str

def transform_char(char):
    if char == '"':
        return '\\"'
    elif char == '\\':
        return '\\\\'
    return char

f = open("day8part1_input.txt", "r")

total = 0
for i, original_line in enumerate(f):
    original_line = original_line.strip()
    original_line_len = len(original_line)
    encoded_line = transfrom_string(original_line)
    encoded_line_len = len(encoded_line) + 2
    line_len_diff = encoded_line_len - original_line_len
    total += line_len_diff

print(total)