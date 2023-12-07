input_numbers = input().split(',')

numbers = [int(x) for x in input_numbers]

average = sum(numbers) / len(numbers)

print(round(average))
