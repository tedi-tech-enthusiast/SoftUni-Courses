def rounding_numbers(input_list):

    return [round(num) for num in input_list]

list_of_nums = input().split()
converted_nums = [float(num) for num in list_of_nums]

result = rounding_numbers(converted_nums)
print(result)