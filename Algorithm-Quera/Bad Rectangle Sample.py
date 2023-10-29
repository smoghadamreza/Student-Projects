answer = 0
n = int(input())
for a in range(1, n):
    for b in range(a, n - a):
        c = n - a - b
        if a + b > c >= b:
            answer += 1
print(answer)

# answer = 0
# n = int(input())
# for a in range(1, n):
#    for b in range(a, n):
#        for c in range(b, n):
#            if a + b + c == n and a + b > c:
#                answer += 1
# print(answer)
