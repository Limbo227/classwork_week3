# #1
# from my_module import a
# print(a)

# #2
# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# random_names = []
# for x in range(4):
#     random_names.append(names[random.randint(0,12)])
# print(random_names)

# # 3
# import sys
# print(sys.platform)

#4
#5


import os
import string
import random
# def create_dir(dir):
#   if not os.path.exists(dir):
#     os.makedirs(dir)
#     print("Created Directory : ", dir)
#   else:
#     print("Directory already existed : ", dir)
#   return dir
# create_dir(dir)

# save_path = '/home/bakai/Desktop/python_week3_day2'
# for k in range(5):
#     name_file = ''.join([random.choice(string.ascii_letters) for x in range(4)])
#     name_file += '.txt'
#     os.path.join(save_path, name_file)
# with open('python_week3_day2','r') as dir:
#     print(dir.read())


# #6
# import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# random.shuffle(names)
# team1 = []
# team2 = []
# team3 = []
# team4 = []
# for x in range(3):
#     team1.append(names[x])
# for x in range(3,6):
#     team2.append(names[x])
# for x in range(6,9):
#     team3.append(names[x])
# for x in range(9,13):
#     team4.append(names[x])

# #1
# import sys

# print('user input: {} {}'.format(sys.argv[0], sys.argv[1]))

# #2
# import sys
# a = input(': ')
# b = input(': ')
# if sys.getsizeof(a) > sys.getsizeof(b):
#     print(a, sys.getsizeof(a))
# else:
#     print(b, sys.getsizeof(b))

# #3
# import random
# import string
# n = int(input('сколько символов будет в пароле?: '))
# password = ''.join([random.choice(string.ascii_letters + string.digits ) for x in range(n)])
# print(password)

# #4
# import random
# choose = input(
#     ' h:Ножницы'
#     ' k:Камень'
#     ' b:Бумага'
# )
# comp = random.randint(1,3)
# if (choose == 'h' and comp == 3) or (choose == 'k' and comp == 1) or (choose == 'b' and comp == 2):
#     print('Win!')
# elif (choose == 'b' and comp == 1) or (choose == 'h' and comp == 2) or (choose == 'k' and comp == 3):
#     print('Lose!')
# else:
#     print('Draw!')

# #1
# import random
# num = random.randrange(6,12,2)
# num_5 = random.randrange(5,100,5)
# print(num, num_5)

#2

#3
# year = (1334//365) + 2021
# a = 1000%365
# month = (a//30) + 11
# b = a%30
# days = b + 30
# if month == 13:
#     month = 0
#     year += 1
# if days == 31:
#     days = 0
#     month += 1
# print(year,month,days)

