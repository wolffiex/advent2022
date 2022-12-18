def part1(input_):
    zeros = [0,0,0]
    translations = []
    for pos in range(3):
        for v in [-1, 1]:
            t = zeros.copy()
            t[pos] = v
            translations.append(tuple(t))
    points = set(map(lambda line: tuple(map(int, line.split(","))), input_.rstrip().split("\n")))
    return sum(count_unoccupied(translations, points))


def count_unoccupied(translations, points):
    for p in points:
        translated = set(map(lambda t: (t[0] + p[0], t[1] + p[1], t[2] + p[2]), translations))
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

print(f"Part 1 sample: {part1(get_sample())}")
print(f"Part 1: {part1(get_input())}")
