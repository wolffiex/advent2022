import re


class Directory():
    def __init__(self, name, parent=None):
        self.name = name
        self.files = []
        self.sub_dirs = {}
        self.parent = parent

    def add(self, line):
        if line.startswith("dir"):
            m = re.match(r"dir (\w+)", line)
            assert m
            name, = m.groups()
            self.sub_dirs[name] = Directory(name, self)
        else:
            m = re.match(r"(\d+) (\w+)", line)
            assert m
            size, name = m.groups()
            self.files.append(File(name, size))

    def get_dir(self, dir_name):
        if dir_name == "..":
            assert self.parent
            return self.parent
        else:
            return self.sub_dirs[dir_name]

    @property
    def size(self):
        return sum(map(lambda f: f.size, self.files + list(self.sub_dirs.values())))

    def sum_recurse(self):
        total_sum = sum(map(lambda d: d.sum_recurse(), self.sub_dirs.values()))
        if self.size < 100000:
            total_sum += self.size
        return total_sum

    def find_smallest_over(self, min_size):
        candidate = None
        if self.size > min_size:
            candidate = self
        for d in map(lambda d: d.find_smallest_over(min_size), self.sub_dirs.values()):
            if d and (not candidate or d.size < candidate.size):
                candidate = d
        return candidate

class File():
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


def part1(inp):
    root = process_input(inp)
    print(f"Part 1: {root.sum_recurse()}")

def part2(inp):
    root = process_input(inp)
    needed = 30000000 - (70000000 - root.size)
    print(f"Part2 {root.find_smallest_over(needed).size}")

def process_input(inp):
    lines = inp.splitlines()
    assert lines.pop(0) == "$ cd /"
    cwd = Directory("/")
    root = cwd
    for line in lines:
        if line.startswith('$'):
            m = re.match(r"\$ cd (\S+)", line)
            if m:
                cwd = cwd.get_dir(m.group(1))
            #else command is ls; implicit
        else:
            cwd.add(line)
    return root
    

def get_sample():
    return """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

part2(get_sample())
part2(open("input.txt").read())
