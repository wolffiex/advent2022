elves = [0]
with open("input.txt") as f:
    for line_r in f:
        line = line_r.rstrip()
        if line:
            elves[-1] += int(line)
        else:
            elves.append(0)

elves.sort()
elves.reverse()
print(f"Max calories: {elves[0]}")
print(f"Top three: {sum(elves[0:3])}")


