def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [11, 22, 33])
values_list = ['Urban', 66, False]
values_dict = {'a': 222, 'b': True, 'c': [1, 2, 3]}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [[67,True], 'Ivan']
print_params(*values_list_2, 42)