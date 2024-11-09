#from time import sleep
#print("hello! I'm new to pycharm right now!")

#dictionary baby
#d_stand_for_dict = {'name': 'faker', 'world winner': '5 times'}
#print(d_stand_for_dict)
#name_value = d_stand_for_dict.get('name')
#win_value = d_stand_for_dict.get('world winner')
#print("name: ", name_value)
#print("world winner: ", win_value)

#file
#print('dang this is file testing')
#file_object = open('hiText.txt', mode= 'r+')
#file_write = file_object.write('\ngg mr beast lmao')
#file_object.seek(0)
#read_file = file_object.read()
#file_object.close()
#print(read_file)

#iterator object
#itera = (x for x in range(5)) #this is iterator object
#sum_itera = sum(itera, start = 0)
#max_itera = max(itera, default = 'default value')
#min_itera = min(itera, default = 'default value')
#sorted_itera = sorted(itera, reverse = True)
#print(sorted_itera)

#print(everything in there)
#print('hehe\n', 'zmjjkk', end = '')
#sleep(3)
#print('end right there')

#with open('hiText.txt', mode='w') as file_object:
#    print('umg that shit was so good fren', file = file_object)

#name = 'The Minh'
##first_talk = 'Hello, my name is '
#love = ' and I love you'
#for c in first_talk + name + love :
#    print(c, end='', flush=True)
#    sleep(0.2)

#input
#value = input('cho bo xin cai dia chi ')
#print('vai lon luon', value)

#'shiba' == 'shiba'
#value = bool('shiba' == 'shiba')
#print(value)

#a = 'oh shit bro'
#b = '69'
#if a == b:
#    print('vaice car lone')
#elif a == b*2:
#    print('the fak bro')
#else:
#    print('hehe')

#t = 'd'
#match t:
#    case 'a':
#        print('ngumaduong')
#    case 'b':
#        print('kekeke')
#    case 'c':
#        print('de ut')
#    case 'd':
#        print('feka')

#five_even_numbers = []
#num = 1
#while True:
#    if num % 2 == 0:
#        five_even_numbers.append(num)
#    if len(five_even_numbers) == 5:
#        break
#    num+=1
#print(five_even_numbers)

#NOTE!!! python doesn't need for-each to use in dict!!!
#FOR

#l = ['a', 'b', 'c', 'd']
#for i in l:
#    print(i)
#else:
#    print('done!')

#i = list(range(0,51,10))
#print(i)
#gg = 'aizz shiba'
#lst = [gg, (1, 2, 3), {'tia li lu mu', ' china go back home'}]

#for a in range(len(lst)):
#    print(lst[a])

#print('TIME TO CHANGE!!!')
#for value in range(len(lst)):
#    lst[value] = value + 1
#    print('count: ', lst[value])

#ENUMERATE

#lst = ['hao', 'kokomi', 'gau do', 'indomie']
#gen = enumerate(lst)
#after enumerate lst, the result should be like this:
#[(0, 'hao hao'), (1, 'kokomi'), (2, 'gau do'), (3, 'indomie')]
#those are index before content of lst
#print(list(gen))
#print(list(lst))
#for index, student in enumerate(lst,1):
    #index for the index number that enumerate add into
    #student for the content of lst that declared
    #enumerate works like a method that ADD THE INDEX TO THE LIST(...)
    #lst is added index number by enumerate method
    #1 is the first index number that the method add into
#    print(index, '=>', student)
#else:
#    print('done!!')

import calendar

yy = 2024
mm = 11

print(calendar.month(yy,mm))

#COMPREHENSION!!!
#COMPREHENSION!!!
#COMPREHENSION!!!



#FUNCTION!!!
#def faker(something: str) -> int:
    #print('Lee Sang-Hyuok')
    #print('faker')
    #print(something)
#    return faker(something)
#for i in range(0,4):
#    faker('world champion')

#def compare(something: str) -> int: #declare COMPARE function
#    return len(something) #return length of the parameter
#f = ['zmjjkk', 'tyson', 'kyedae', 'aspas', 't3xture']
#f.sort(key=compare) #using the COMPARE function with the SORT function
#key = compare => USING A FUNCTION AS A KEY!!!
#print(f)

#def tyson(a,b,c,d):
#    total = a+b+c+d
#    print('total: ', total)

#tyson(1,2,3,4) #positional argument
#tyson(1,2,3,d=6) #key word agrument

#def aka(a,*,key_1,key_2):
    #this function takes 1 positional agrument or keyword agrument
    #BUT IT HAVE TO TAKES 2 KEYWORD AGRUMENTS!!!
#    pass


#PACKING and UNPACKING!!!
#PACKING and UNPACKING!!!
#PACKING and UNPACKING!!!
#lst = [1,2,3,4,5,6,7,8,9,10]
#def vcl(*lst): #PACKING PARAMETER using * for take everything in list, tuple, dict,...
#    for i in range(len(lst)-1):
#        print(lst[i])
#vcl(*lst)

#arr = ['v', 'a', 'i']
#d = input()
#def f(*arr,d):
#    for i in range(len(arr)):
#        print(arr[i])
#    print(d)
#f(*arr,d = d) #after PACKING PARAMETER, there must be KEYWORD AGRUMENT

#dic = {'nameeee': 'tenz', 'ageeee': '24'}
#def dun(name,age):
#    print('name:', name)
#    print('age:', age)
#dun(*dic) #UNPACKING dict with * can take the keyword, not the value

#dic = {'name': 'tenz', 'age': '24'}
#def dun(name,age):
#    print('name:', name)
#    print('age:', age)
#dun(**dic) #UNPACKING dict with ** can take the value, not the keyword

#a_dic = {'name:': 'faker', 'age': '24', 'world': '5'}
#def ducon(**kwargs):
#    print(kwargs)
#    print(type(kwargs))
#ducon(**a_dic) #PACKING dict with **

#def zmjjkk(**kwargs):
#    for key, value in kwargs.items():
#        print(key, ':', value)

#zmjjkk(**a_dic)

#you dont allowed to put the POSITIONAL PARAMETER after PACKING PARAMETER ** or *



#in Python, YOU CAN'T PASS BY PREFERENCE.
#just PASS BY VALUE!!!

#def cal_something(a,b):
#    c = a*b
#    d = a+b
#    return c,d
#a = 1
#b = 2
#result_a, result_b = cal_something(a,b)
#print('c:', result_a,'d:',result_b)

#yield
#def diu():
#    yield 'vcl'
#    print('kaka')
#    yield 'kii'
#    print('fak')
#for value in diu():
#    print(value) #what the fuck is this







#LEETCODE






# def find_running_sum(nums: list) -> list:
#     running_sum = []
#     summ = 0
#     for i in range(len(nums)):
#         summ = sum(nums[:i+1])
#         running_sum.append(summ)
#
#     return running_sum
# print('Running sum:', find_running_sum([3,1,2,10,1]))


#2D array
#np.array is more flexible and can handle higher-dimensional arrays.
#for most matrix operations, using np.array is often preferred.
# def numpy_test(matrix = list):
# import numpy as np
# matrix = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
# arr = np.array([[3,2,1],
#                [6,5,4],
#                [9,8,7]])
# # print(matrix)
# # for row in matrix:
# #     for element in row:
# #         print(element, end='')
# print(arr + 2)



#who is the richest
#def find_the_richest(accounts: list) -> int:
#     max_wealth = []
#     for account in range(len(accounts)-1):
#         if accounts[account + 1] < accounts[account]:
#             max_wealth = accounts[account]
#
#     return sum(max_wealth)
#
# print('The richest:', find_the_richest([[7,1,3],
#                                        [2,8,7],
#                                        [1,9,5]]))




#FIZZ BUZZ
# answer = []
# def fizz_buzz(num: int) -> list:
#     for i in range(num):
#         if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
#             answer.append('FizzBuzz')
#         elif (i + 1) % 3 == 0:
#             answer.append('Fizz')
#         elif (i + 1) % 5 == 0:
#             answer.append('Buzz')
#         else:
#             answer.append(i+1)
#     return answer
#
# number = input('Enter a number: ')
# number = int(number)
# print('Result:', fizz_buzz(number))



# def step_count_to_zero(num: int) -> int:
#     step_count = 0
#     while num != 0:
#         if num % 2 == 0:
#             num = num / 2
#             step_count += 1
#         else:
#             num = num - 1
#             step_count += 1
#     return step_count
# number = input('Enter the number: ')
# number = int(number)
# print('Step count:', step_count_to_zero(number))



# def find_middle_node(lst: list) -> list:
#     final_lst = []
#     count = 0
#
#     middle_index = int(len(lst) / 2)
#     condition = middle_index
#     while count < (len(lst) - condition):
#         final_lst.append(lst[middle_index])
#         middle_index += 1
#         count += 1
#
#     return final_lst
#
# print('Middle node: ', find_middle_node([1,2,3,4,5,6,7,8]))



def can_construct(ransom_note: str, magazine: str) -> bool:
    counter = {}
    for c in magazine:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    for c in ransom_note:
        if c not in counter:
            return False
        elif counter[c] == 1:
            del counter[c]
        else:
            counter[c] -= 1

    return True

#print(can_construct('happy','happy halloween'))