# num1= int(input())
# num2= int(input())
# num3= int(input())
#
# largest_num = 0
#
# if num1 >= num2 and num1 >= num3:
#     largest_num = num1
# elif num2 >= num1 and num2 >= num3:
#     largest_num = num2
# else:
#     largest_num = num3
#
# print(largest_num)

num1, num2, num3 = int(input()), int(input()), int(input())

print(max(num1, num2, num3))