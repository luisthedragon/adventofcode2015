def solution(line):
    vowels = ["a","e","i","o","u"]
    disallowed_substrings = ["ab", "cd", "pq", "xy"]
    nvowels = 0
    has_double = False
    for i in range(len(line)-1):
        if line[i] in vowels:
            nvowels += 1
        if line[i] == line[i+1]:
            has_double = True
        if line[i:i+2] in disallowed_substrings:
            return False
    # Check if last letter is a vowel
    if line[i+1] in vowels:
        nvowels += 1
    return nvowels >= 3 and has_double

f = open("day5part1_input.txt", "r")
count = 0
for line in f:
    is_nice = solution(line)
    print(is_nice)
    if is_nice:
        count += 1

print(count)
