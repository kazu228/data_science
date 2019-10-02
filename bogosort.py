import random, copy, time

N=10
answer = list(range(1, N+1))

dat = copy.deepcopy(answer) ; random.shuffle(dat)

start = time.perf_counter()
while(dat != answer):
    random.shuffle(dat)
print(time.perf_counter()-start)