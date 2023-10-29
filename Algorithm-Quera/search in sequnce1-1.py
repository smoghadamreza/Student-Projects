n, q = map(int, input().split())
lst_q = []
lst_c = [num for num in input().split(" ", n-1)]
#for i in range(0, n):
#    ele = input()
#    lst_c.append(ele)
for i in range(0, q):
    ele = input()
    lst_q.append(ele)
for i in lst_q:
    count = 0
    for j in lst_c:
        if int(j) < int(i):
            count += 1
    print(count)
