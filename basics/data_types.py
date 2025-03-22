"""
1) numeric (int, float, complex)
2) string
3) list
4) tuple
5) dictionary
"""
vote_eligibility = 18
height = 5.12
complex_type = 100j

string = 'guna'

programming_languages = ['python', 'go', 'java', '.net', 'c', 'R']
print(programming_languages)

print(programming_languages[-1]) # prints last index value

# sublist
sub_list = programming_languages[1:5]
print(sub_list)

# insert(index, value)
programming_languages.insert(1, 'javascript')
print(programming_languages)

print(programming_languages[:2])

for values in programming_languages:
    if values == 'python':
        print('{} {}'.format('learning : ', values))
    else:
        print('{} {}'.format('not learning', values))


# append(value) adds at the end of the list