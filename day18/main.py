zeros = [0,0,0]
translations = []
for pos in range(3):
    for v in [-1, 1]:
        t = zeros.copy()
        t[pos] = v
        translations.append(tuple(t))

def part2(input_):
    points = set(map(lambda line: tuple(map(int, line.split(","))), input_.rstrip().split("\n")))
    exterior = find_exterior(points)
    return sum(count_exterior(points, exterior))

def part1(input_):
    points = set(map(lambda line: tuple(map(int, line.split(","))), input_.rstrip().split("\n")))
    return sum(count_unoccupied(points))

def move_point(p, t):
    return (t[0] + p[0], t[1] + p[1], t[2] + p[2])

def in_bounds(p):
    for i in range(3):
        if p[i] < 0 or p[i] > 30:
            return False
    return True

def find_exterior(points):
    exterior = {(0,0,0)}
    last_size = 0
    while len(exterior) > last_size:
        last_size = len(exterior)
        translated = set().union(*map(lambda t: {*map(lambda p: move_point(t,p), exterior)}, translations))
        candidates = {*filter(in_bounds, translated)}.difference(points)
        exterior.update(candidates)
    return exterior

def count_exterior(points, exterior):
    for p in points:
        translated = set(map(lambda t: move_point(t,p), translations))
        yield len(translated.intersection(exterior))

def count_unoccupied(points):
    for p in points:
        translated = set(map(lambda t: move_point(t,p), translations))
        yield len(translated.difference(points))


def get_input():
    return open("input.txt").read()

def get_sample():
    return """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""

def get_tiny():
    return """1,1,1
1,1,2
1,1,3
"""

print(f"Part 1 sample: {part1(get_sample())}")
print(f"Part 1: {part1(get_input())}")
print(f"Part 2 sample: {part2(get_sample())}")
print(f"Part 2: {part2(get_input())}")
