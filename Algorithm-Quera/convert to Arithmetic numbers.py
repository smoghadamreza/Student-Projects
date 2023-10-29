n, k = map(int, input().split())
a = list(map(int, input().split()))

val = 1000 * 1000 * 1000

for x in range(-100000, 100000):
    t = 0
    for i in range(n):
        t += abs((x + i * k) - a[i])
    val = min(val, t)

print(val)