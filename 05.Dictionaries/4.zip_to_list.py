
my_list_1 = [1,2,3,4]
my_list_2 = ['a','b','c','d']

joined = list(zip(my_list_1,my_list_2))

print(f'The result of the zip function is {joined} it is of type {type(joined)}')


i,j = zip(*joined)