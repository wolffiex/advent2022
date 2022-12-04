def split_line(line):
    a,b = line.split(",")
    return tuple(map(int, a.split("-"))), tuple(map(int, b.split("-")))

def contains(a, b):
    return  a[0] <= b[0] and a[1] >= b[1]

def is_contained(line):
    a, b = split_line(line)
    return 1 if contains(a,b) or contains(b,a) else 0

def is_between(n, rng):
    return n >= rng[0] and n <= rng[1]

def is_overlap(line):
    a, b = split_line(line)
    if is_between(a[0], b) or is_between(a[1], b) or is_between(b[0], a) or is_between(b[1], a):
        return 1 
    return 0
    
def part1():
    sample_part1=sum([is_contained(line) for line in get_sample().splitlines()])
    print(f"Part 1 sample result: {sample_part1}")
    part1_result=sum([is_contained(line) for line in get_input_lines()])
    print(f"Part 1 input result: {part1_result}")

def part2():
    sample_result =sum([is_overlap(line) for line in get_sample().splitlines()])
    print(f"Part 1 sample result: {sample_result}")
    result =sum([is_overlap(line) for line in get_input_lines()])
    print(f"Part 1 result: {result}")

def get_input_lines():
    return open("input.txt")


def get_sample():
    return """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

# part1()
part2()
