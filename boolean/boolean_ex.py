# function can return boolean
def myfunction():
    return True

print(myfunction())

if myfunction():
    print('learning python selenium')
else:
    print('learning aws and jenkins')

print(bool('')) # False
print(bool(0)) # False
print(bool([])) # False
print(bool({})) # False
print(bool(None)) # False

# isinstance method
x = 'hello'
print(isinstance(x, str))