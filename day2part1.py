def solution(l, w, h):
    area1 = l*w
    area2 = l*h
    area3 = w*h
    min_area = min(area1, area2, area3)
    return 2*l*w + 2*w*h + 2*h*l + min_area

f = open("day2part1_input.txt", "r")
suma = 0
for line in f:
    l, w, h = map(int, line.split("x"))
    suma += solution(l, w, h)
print(suma)
