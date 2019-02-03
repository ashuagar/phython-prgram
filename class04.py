# """
# if <Condition>:
#     statement
#
# """
# number_01 =4
# number_02 =4
# number_03 =6
#
# if number_01 < number_02:
#     print('Number 02 is greater than Number01.')
#
# #if else
#
# if number_01 > number_02:
#     print("Number 01 is greater than Number02.")
# else:
#     print('Number 02 is greater than Number01.')
#
# #if elif else
#
# if number_01 > number_02:
#     print("Number 02 is greater than Number 01.")
#
# elif number_02 < number_03:
#     print('Number 03 is greater than Number02.')
#
# else:
#     print('Number 02 is greater than Number01.')
#
# # nested if else
#
# if number_01 > number_02:
#     if number_01 > number_03:
#         print("01 number 01 is max")
#     else:
#         print("02 number 03 is max")
# else:
#     if number_02> number_03:
#         print("03 number 02 is max")
#     else:
#         print("04 number 03 is max")
#
#
# if number_01 < number_02 < number_03:
#     print("05 number 03 is max")
# elif number_01 < number_02 and number_02> number_03:
#     print(" 06 number 02 is max")
#
# elif number_01 > number_02 and number_01 > number_03:
#     print("07 number 01 is max")
#
# """
# for i in range():
# print(i)
# """
# # for loop
# for i in range(0,5):
#     print(i)
# #while loop
# number = 0
# while number < 5:
#     print (number)
#     number += 1
# #  ################################################
#     # 4) Nested loop
#     ##########################
# for i in range (0,5):
#       for j in range(0,i):
#           print(j,end="")
#           print('')
#
# #do while loop(by default enter in loop)
# number =0
# while True:
#         if number > 5:
#             break
#             print (number)
#             number += 1
#
# #

for i in range(0, 5):

    for j in range(0, 5):
        print("*", end=" ")
    print('')

