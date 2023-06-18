def solution(line):
    duals = dict()
    has_duplicate_dual = False
    has_double = False
    for i in range(len(line)-1):
        dual = line[i:i+2]
        # print(i)
        # print(dual)
        # print(duals.get(dual))
        if duals.get(dual) != None and duals.get(dual) != i - 1:
            has_duplicate_dual = True
        duals[dual] = i
        if i <= len(line)-3 and line[i] == line[i+2]:
            has_double = True
    return has_duplicate_dual and has_double

f = open("day5part2_input.txt", "r")
count = 0
for line in f:
    is_nice = solution(line)
    print(is_nice)
    if is_nice:
        count += 1

print(count)
