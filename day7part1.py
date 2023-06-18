LSHIFT = 0
RSHIFT = 1
OR = 2
NOT = 3
AND = 4

operand_apparitions = dict()
operands_found = dict()

operator_mapping = {
    "LSHIFT" : LSHIFT,
    "RSHIFT" : RSHIFT,
    "OR" : OR,
    "NOT" : NOT,
    "AND" : AND,
}

def get_operand_value(operand):
    if operand.isnumeric():
        return int(operand)
    else:
        return operands_found.get(operand)

def solve(left_components):
    try:
        if len(left_components) == 3:
            if operator_mapping[left_components[1]] == LSHIFT:
                return get_operand_value(left_components[0]) << int(left_components[2])
            elif operator_mapping[left_components[1]] == RSHIFT:
                return get_operand_value(left_components[0]) >> int(left_components[2])
            elif operator_mapping[left_components[1]] == OR:
                return get_operand_value(left_components[0]) | get_operand_value(left_components[2])
            elif operator_mapping[left_components[1]] == AND:
                return get_operand_value(left_components[0]) & get_operand_value(left_components[2])
        elif len(left_components) == 2:
            MAX_16_BIT = 2**16-1
            return MAX_16_BIT - get_operand_value(left_components[1])
        else:
            return get_operand_value(left_components[0])
    except TypeError:
        return None

def parse_line(string):
    left_part, right_part = string.split(" -> ")
    left_components = left_part.split(" ")
    return left_components, right_part

for i in range(300):
    parsed_lines = []
    resolvable_operations = set()
    f = open("day7part1_input.txt", "r")
    for i, line in enumerate(f):
        parsed_line = parse_line(line.rstrip())
        parsed_lines.append(parsed_line)
        # print(parsed_line)
        operation_result = solve(parsed_line[0])
        operands_found[parsed_line[1]] = operation_result
        # print(operation_result)
print(operands_found)
