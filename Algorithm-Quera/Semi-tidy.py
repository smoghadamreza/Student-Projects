count = 0
n = int(input())
lst_a = [num for num in input().split(" ", n - 1)]
for i in range(0, n):
    if int(lst_a[i]) != int(i+1):
        count += 1
if count == 2:
    print("YES")
else:
    print("NO")
