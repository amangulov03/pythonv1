# import random
# count = 0
# num = random.randint(1, 100)
# while True:
#     user = input("Ведите число от 1 до 100: ")
#     if user.isdigit():
#         if int(user) == num:
#             print(f"Угадал! Число: {num}, попыток: {count}")
#             break
#         elif int(user) >= num:
#             print("Это число больше")
#             count += 1
#         else:
#             print("Это число меньше")
#             count += 1
#     elif user.isalpha():
#         print("Это слово, введите число")
#     else:
#         print("Число содержит слово или некорректные символы, введите только число")


# for i in range(8):
#     print(' ' * (8 - 1 * i) + '*' * (1 + i * 2))

# n = int(input())
# for i in range(2, (n**0.5) + 1):
#     if i % 1 == 0:
#         print(i)

# str1 = "как сделать домашку быстро и легко".split()
# count = 0
# for i in str1:
#     count += 1
# print(count)

# n = input()
# if n == n[::-1]:
#     print(True)
# else:
#     print(False)

