def calculate_power_of_two(number):
    result = number ** 2
    return result


input_number = int(input("لطفاً یک عدد صحیح وارد کنید: "))

result = calculate_power_of_two(input_number)
print(f"توان دو عدد {input_number} برابر است با: {result}")
