import re
repeated_re = re.compile(r"(.).*:.*\1")
def get_value(c):
    if ord(c) < ord('a'):
        ## uppercase
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1


def part1_line(line):
    half = len(line)//2
    first, second = line[:half], line[half:]
    joined = ":".join([first, second])
    result = repeated_re.search(joined)
    assert result
    return get_value(result.group(1))

sample_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

# sum = 0
# for line in sample_input.splitlines():
#     sum += part1_line(line)

# print(f"Sample input part 1sum: {sum}")

# sum = 0
# for line in open("input.txt"):
#     sum += part1_line(line)
# print(f"Part 1 sum: {sum}")

part2_re = re.compile(r"(.).*:.*\1.*:.*\1")
def part2_line(line_iter):
    try:
        elf_group = ":".join(map(lambda _: next(line_iter), range(3)))
    except:
        return None
    if len(elf_group) == 0:
        return None
    print(len(elf_group))
    result = part2_re.search(elf_group)
    assert result
    return get_value(result.group(1))


it = iter(sample_input.splitlines())
print(part2_line(it))
print(part2_line(it))

input_it = iter(open("input.txt").read().splitlines())
part2_sum = 0
while True:
    v = part2_line(input_it)
    if v is None:
        print(f"Sum of part2 is {part2_sum}")
        break
    else:
        part2_sum += v
