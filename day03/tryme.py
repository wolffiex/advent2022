def process_iterator(it, f):
    while True:
        try:
            yield f(it)
        except StopIteration:
            return 

# print(sum(summem(iter([1,2,3]), lambda x: x)))


x = range(10)
def chunk(it, n):
    accum = []
    while len(accum) < n:
        try:
            accum.append(next(it))
        except StopIteration:
            return 
    yield tuple(accum)

print(chunk(iter(range(10)), 3))
