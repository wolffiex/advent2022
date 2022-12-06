def part1(inp):
    i = 0
    while len({*inp[i:i+4]}) < 4:
        i += 1
    print(f"Found {i+4}")

def part2(inp):
    i = 0
    while len({*inp[i:i+14]}) < 14:
        i += 1
    print(f"Found {i+14}")
part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
part2("bvwbjplbgvbhsrlpgdmjqwftvncz")
part2(open("input.txt").read())

