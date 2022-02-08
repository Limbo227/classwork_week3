# #1
# def new_array(list):
#     x = len(list)//2
#     a_list = list[:x]
#     b_list = list[x:]
#     a_list.reverse()
#     b_list.reverse()
#     new_list = a_list + b_list
#     return new_list    
# list = [1,2,3,4,5,6]
# print(new_array(list))

# #2
# def fibancachi():
#     a = 0
#     b = 1
#     list = [a,b]
#     for x in range(8):
#         c = a + b
#         a = b
#         b = c
#         list.append(c)
#     return list
# print(fibancachi())

# #3
# def add(a,b):
#     x = a + b
#     return x
# def minus(a,b):
#     x = a - b
#     return x
# print(add(2,3))
# print(minus(5,2))

#1
name_file = input('name of the file?: ')
def create_file(name):
    with open('name.txt', 'r') as my_file:
        w = my_file.read()
    return w
print(create_file(name_file))