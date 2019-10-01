dat = [70, 50, 45, 75, 90, 85, 60]
max = -1  #最大値を得るシステム

for i in range(len(dat)):
    if dat[i] > max:
        max = dat[i]

print(max)

min = 101 # 最小値を得るシステム

for j in range(len(dat)):
    if dat[j] < min:
        min = dat[j]

print(min)
 # 例題
xarray = [3,5,2,2,6,1]

total = 0

for i in range(len(xarray)):
    total += xarray[i] ** 2

print(total)