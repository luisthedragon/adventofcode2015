def solution(l, w, h):
    sides = [l,w,h]
    sides.sort()
    min_perimeter = 2 * (sides[0] + sides[1])
    volume = l*w*h
    return min_perimeter + volume

f = open("day2part2_input.txt", "r")
suma = 0
for line in f:
    l, w, h = map(int, line.split("x"))
    suma += solution(l, w, h)
print(suma)
