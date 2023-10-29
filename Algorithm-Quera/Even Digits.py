#Number = int(input())
#count = 0
#for i in str(Number):
#    if i in '02468':
#        count += int(i)

# Solve With Lists
# Number = int(input())
# Lst = []
# for i in str(Number):
#     if i in '02468':
#         Lst.append(int(i))
# print(sum(Lst))
Number = int(input())
Lst = []
Lst2 = [0, 2, 4, 6, 8]
for i in str(Number):
    for j in Lst2:
        if i in str(j):
            Lst.append(int(i))
print(sum(Lst))
