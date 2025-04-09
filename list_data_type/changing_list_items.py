my_list = ['hello', 'world', 'python', 'selenium']

my_list[1] = 'java'

print(my_list)

# changing multiple values using range
my_list[1:3] = ['go', 'Angular']
print(my_list)

my_list[1:3] = ['banana'] #[hello, banana, selenium]
print(my_list)


# insert(index, value)
my_list.insert(len(my_list) , 'end')
print(my_list)