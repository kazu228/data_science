import numpy.random, time

N = 3000000

xarray = list(numpy.random.rand(N))

start = time.perf_counter()
total = 0

for i in range(N):
    total += xarray[i]
ave = total / N
total2 = 0

for i in range(N):
    total2 += (xarray[i] -ave) * (xarray[i] -ave)

var = total2/N
before = time.perf_counter()-start
print("改良前:" + str(time.perf_counter()-start))

start = time.perf_counter()
total = 0
total2 = 0

for i in range(N):
    total += xarray[i]
    total2 += xarray[i] * xarray[i]
ave = total/N
var = total2/N
after = time.perf_counter()-start
print("改良後：" + str(time.perf_counter()-start))
print("改良差：" + str(before-after))
