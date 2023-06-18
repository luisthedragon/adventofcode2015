import hashlib

def solution(line):
    # initializing string
    for i in range(99999999):
        str2hash = line+str(i)
        result = hashlib.md5(str2hash.encode())
        hexresult = result.hexdigest()
        if hexresult.startswith("000000"):
            return i

f = open("day4part2_input.txt", "r")
for line in f:
    print(solution(line))
