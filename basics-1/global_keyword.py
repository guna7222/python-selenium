# global keyword
# we can make local variables as global variables

def test_name_length():
    global name
    name = 'username1'
    name_len = len(name)
    if name_len > 6:
        print('valid username')
    else:
        print('not a valid username')

test_name_length()

print(name)