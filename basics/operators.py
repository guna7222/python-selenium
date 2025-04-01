# Arithmatic
bikes_owned = 1
cars_owned = 2

print(bikes_owned + cars_owned) # addition
print(bikes_owned - cars_owned) # subtraction
print(bikes_owned * cars_owned) # multiplication
print(bikes_owned / cars_owned) # division
print(bikes_owned ** cars_owned) # exponentation
print(bikes_owned // cars_owned)  # floor division
print(bikes_owned % cars_owned) # moduls

arithmatic_list = [
    bikes_owned + cars_owned, bikes_owned - cars_owned,
    bikes_owned * cars_owned, bikes_owned / cars_owned,
    bikes_owned ** cars_owned, bikes_owned // cars_owned,
    bikes_owned % cars_owned
                   ]

for x in arithmatic_list:
    print(x)

