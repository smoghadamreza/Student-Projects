number = int(input())

count = 0
for i in range(number):
    if i % 2 == 0:
        count += i
print(count)