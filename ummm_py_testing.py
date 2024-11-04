from time import sleep
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

lst = ['hao hao', 'kokomi', 'gau do', 'indomie']
gen = enumerate(lst)
#after enumerate lst, the result should be like this:
#[(0, 'hao hao'), (1, 'kokomi'), (2, 'gau do'), (3, 'indomie')]
#those are index before content of lst
print(list(gen))
print(list(lst))
for index, student in enumerate(lst,1):
    #index for the index number that enumerate add into
    #student for the content of lst that declared
    #enumerate works like a method that ADD THE INDEX TO THE LIST(...)
    #lst is added index number by enumerate method
    #1 is the first index number that the method add into
    print(index, '=>', student)
else:
    print('done!!')


#COMPREHENSION!!!
#COMPREHENSION!!!
#COMPREHENSION!!!