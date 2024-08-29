def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1.5, 'слово', False]
values_dict = {'a': 5, 'b': 'текст', 'c': True }

print_params(*values_list)
print_params(**values_dict)