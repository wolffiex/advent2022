def part1(inp):
    grid = list(map(lambda line: list(map(int, line)), inp.splitlines()))
    # print(grid)
    count = 0
    grid_width = len(grid[0])
    grid_height = len(grid)
    for y in range(0, grid_height):
        for x in range(0, grid_width):
            # print(f"check {x},{y} {grid[y][x]}")
            if is_visible(grid, x, y):
                count += 1
    print(f"Trees visible: {count}")

def is_visible(grid, x, y):
    tree_height = grid[y][x]
    def is_below(l):
        if not len(l):
            return True

        # print(f"   {tree_height} {l}")
        return max(l) < tree_height 

    row = grid[y]
    col = [r[x] for r in grid]
    # print(f" {row} {col}")
    return is_below(row[:x]) or is_below(row[x+1:]) or is_below(col[:y]) or is_below(col[y+1:])


def get_sample():
    return """30373
25512
65332
33549
35390
"""

# part1(get_sample())
part1(open("input.txt").read())
