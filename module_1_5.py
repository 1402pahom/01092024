immutable_var=0, 'name', [0,1,2,3]
print(immutable_var)
print(type(immutable_var))
mutable_list=['молоко', 'хлеб', 'яблоки', 'сыр']
print(type(mutable_list))
print(mutable_list)
mutable_list.append('вино')
print(mutable_list)
mutable_list.extend('колбаса')
print(mutable_list)
mutable_list.extend(['яйца', 500])
print(mutable_list)
mutable_list.remove('хлеб')
print(mutable_list)
print('яблоки' in mutable_list )
print('яблоки' not in mutable_list )









