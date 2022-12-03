from enum import Enum

class Choice(str, Enum):
    ROCK='A',
    PAPER='B',
    SCISSOR='C',

self_map = {
    'X': Choice.ROCK,
    'Y': Choice.PAPER,
    'Z': Choice.SCISSOR,
}
beats = {
    Choice.ROCK : Choice.SCISSOR,
    Choice.PAPER : Choice.ROCK,
    Choice.SCISSOR: Choice.PAPER,
}

bonus = {
    Choice.ROCK : 1,
    Choice.PAPER : 2,
    Choice.SCISSOR: 3,
}

def score_round(oppo, self):
    score = 0
    score += bonus[self]
    if self == oppo:
        score += 3
    if beats[self] == oppo:
        score += 6
    return score

sum1 = 0
for line in open('input.txt'):
    [oppc, selc] = line.rstrip().split(' ')
    oppo, self = Choice(oppc), Choice(self_map[selc])
    sum1 += score_round(oppo, self)


print(f"Incomplete reading: {sum1}")

class Result(str, Enum):
    LOSE='X'
    DRAW='Y'
    WIN='Z'

def choose(oppo, result):
    match result:
        case Result.DRAW:
            return oppo
        case Result.LOSE:
            return beats[oppo]
        case Result.WIN:
            for a, b in beats.items():
                if b == oppo:
                    return a

sum2 = 0
for line in open('input.txt'):
    [opp, res] = line.rstrip().split(' ')
    oppo, result = Choice(opp), Result(res)
    self = choose(oppo, result)
    sum2 += score_round(oppo, self)

print(f"Correct reading: {sum2}")
