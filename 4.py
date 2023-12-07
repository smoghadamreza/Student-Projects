num_lines = int(input())

for _ in range(num_lines):
    line = input().split()
    letter = line[0]
    repeat_count = int(line[1])

    print(letter * repeat_count)
