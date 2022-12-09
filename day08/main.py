from functools import reduce

def part1(inp):
    print(f"Part 1: {sum(process_grid(inp, count_visible))}")

def part2(inp):
    print(f"Part 2: {max(process_grid(inp, score_scenicness))}")

def process_grid(inp, f):
    grid = list(map(lambda line: list(map(int, line)), inp.splitlines()))
    grid_width = len(grid[0])
    grid_height = len(grid)
    for y in range(0, grid_height):
        for x in range(0, grid_width):
            row = grid[y]
            col = [r[x] for r in grid]
            l, r = [*reversed(row[:x])], row[x+1:]
            t, b = [*reversed(col[:y])], col[y+1:]
            height = grid[y][x]
            result = f(height, [l, r, t, b])
            # if result > 10000:
            # if result:
            #     print(f"**{x},{y} [{height}] {result}**")
            yield result

def count_visible(height, vecs):
    for vec in vecs:
        if len(vec) == 0 or max(vec) < height:
            return 1
    return 0

def score_scenicness(height, vecs):
    def count_vec(vec):
        count = 0
        for tree in vec:
            count += 1
            if not height > tree:
                break
        return count

    counted = [*map(count_vec, vecs)]
    product = reduce((lambda x, y: x * y), counted)
    return product




def get_sample():
    return """30373
25512
65332
33549
35390
"""

part1(get_sample())
part1(open("input.txt").read())
part2(get_sample())
part2(open("input.txt").read())
