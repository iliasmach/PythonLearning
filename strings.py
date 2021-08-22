import variables
string1 = "Hello world"
russian_string = "Привет, мир!"

# Array
print(string1[2])

# Looping through string
for x in string1:
    print(x)

length = len(string1)
russian_len = len(russian_string)

print("Length string " + str(length))
print("Russian length string " + str(russian_len))
# Checking in string
print("world" in string1)
print("asd" in string1)
print("asd" not in string1)

# Slices

print(string1[2:5])
print(russian_string[2:5])
print(russian_string[2:])
print(russian_string[-2:])

# Modify

print(russian_string.upper())
print(russian_string.replace("Привет", "Hello"))
print(russian_string.split(","))
print(russian_string.lower())
print(russian_string.lower().capitalize())
print(russian_string.center(30, 'f'))
print(russian_string.casefold())
print(russian_string.count('р'))
print(russian_string.endswith('мир!'))
print(russian_string.startswith('Привет'))
print(russian_string.encode('cp1251'))
print(russian_string.find(","))
print(' '.join(variables.arr))
print(russian_string.center(100).strip())
print(russian_string.partition(','))
print("x is {lower}, y is {higher}".format_map({'higher':6, 'lower':7}))

to_trans = "abc"
trans_dict = {'a':1, 'b':2, 'c':3}

print(to_trans.maketrans(trans_dict))

# Format

format_string = "My string is {}"
print(format_string.format(russian_string))
print("Format {1} {0}".format(string1, russian_string))
