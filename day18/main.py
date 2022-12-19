zeros = [0,0,0]
translations = []
for pos in range(3):
    for v in [-1, 1]:
        t = zeros.copy()
        t[pos] = v
        translations.append(tuple(t))

def part2(input_):
    points = set(map(lambda line: tuple(map(int, line.split(","))), input_.rstrip().split("\n")))
    return sum(count_exterior(translations, points))

def part1(input_):
    points = set(map(lambda line: tuple(map(int, line.split(","))), input_.rstrip().split("\n")))
    return sum(count_unoccupied(translations, points))

def move_point(p, t):
    return (t[0] + p[0], t[1] + p[1], t[2] + p[2])

def can_escape(from_point, points):
    for t in translations:
        p = from_point
        while p not in points:
            p = move_point(p, t)
            for i in range(3):
                if p[i] < 0 or p[i] > 30:
                    return True
    return False

def count_exterior(translations, points):
    for p in points:
        for t in translations:
            adjacent = move_point(p, t)
            if adjacent not in points:
                yield 1 if can_escape(adjacent, points) else 0

def count_unoccupied(translations, points):
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
