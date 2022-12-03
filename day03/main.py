import re
repeated_re = re.compile(r"(.).*:.*\1")
def get_value(c):
    if ord(c) < ord('a'):
        ## uppercase
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1


def part1(line):
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

sample_result = sum(map(part1, sample_input.splitlines()))
print(f"Sample input part 1: {sample_result}")

part1_result = sum(map(part1, open("input.txt")))
print(f"Full input part 1: {part1_result}")

### Part The Second
part2_re = re.compile(r"(.).*:.*\1.*:.*\1")
def part2(elf_it):
    elf_group = ":".join([next(elf_it), next(elf_it), next(elf_it)])
    result = part2_re.search(elf_group)
    assert result
    return get_value(result.group(1))

def process(f, it):
    while True:
        try:
            yield f(it)
        except StopIteration:
            return 

sample_result2 = sum(process(part2, iter(sample_input.splitlines())))
print(f"Sample input part 2: {sample_result2}")

part2_result = sum(process(part2, map(lambda l:l.rstrip(), open("input.txt"))))
print(f"Result for part 2: {part2_result}")
