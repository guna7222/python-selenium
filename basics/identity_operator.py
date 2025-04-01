# objects are compared
x = ["java", "python"]
y = ["java", "python"]

print(x is y) # false

print(x is not y)

abc = ["java", "python"]
cba = abc
print(abc is cba) # true