import re
def part1(inp):
    stacks = {}
    initial, moves = inp.split("\n\n")
    initial_arr = initial.splitlines()
    bottom = len(initial_arr) - 1
    for i in range(0, len(initial_arr[bottom])):
        c = initial_arr[bottom][i]
        if c == ' ':
            continue
        stack = []
        j = bottom -1
        while j >= 0 and initial_arr[j][i] != " ":
            stack.append(initial_arr[j][i])
            j -=1
        stacks[c] = stack
    print(stacks)
    for line in moves.splitlines():
        m = re.match(r"move (\d*) from (\d*) to (\d*)", line)
        assert m
        cnt, col_from, col_to = m.groups()
        print(cnt, col_from, col_to, line)
        for i in range(0, int(cnt)):
            stacks[col_to].append(stacks[col_from].pop())

    print(stacks)
    res = ""
    for stack in stacks.values():
        res += stack[-1]
    print(res)

def part2(inp):
    stacks = {}
    initial, moves = inp.split("\n\n")
    initial_arr = initial.splitlines()
    bottom = len(initial_arr) - 1
    for i in range(0, len(initial_arr[bottom])):
        c = initial_arr[bottom][i]
        if c == ' ':
            continue
        stack = []
        j = bottom -1
        while j >= 0 and initial_arr[j][i] != " ":
            stack.append(initial_arr[j][i])
            j -=1
        stacks[c] = stack
    for line in moves.splitlines():
        m = re.match(r"move (\d*) from (\d*) to (\d*)", line)
        assert m
        cnt, col_from, col_to = m.groups()
        index = int(cnt)
        stacks[col_to].extend(stacks[col_from][-index:])
        stacks[col_from] = stacks[col_from][:-index]

    print(stacks)
    res = ""
    for stack in stacks.values():
        res += stack[-1]
    print(res)

def get_sample_input():
    return """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

def get_input():
    return open("input.txt").read()

# part2(get_sample_input())
part2(get_input())
