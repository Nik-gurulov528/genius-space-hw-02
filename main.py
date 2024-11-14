text = "Hello, World!"
num1 = 5
num2 = 7.5
isChecked = False
lst = [1, 5, 3, 7]
keys = {'age': '27', 'isHuman': 'True'}
tuple = (1, 2, 3, 4, 5)
nothing = None

print(num1 < num2)
print(lst == tuple)
print(text != isChecked)

# Робота з рядками

num_str = 125
num_str = str(num_str)
print(type(num_str))

message = 'Hi, my name is Python!'
message = message.replace('y', '0')
message = message.replace('i', '1')
print(message)

split_test = 'This is a split test'
split_test = split_test.split()
print(split_test)
string_join = ' '.join(split_test)
print(string_join)

print(len(string_join))

# Робота зі списками

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)

print(list_extend.index(6))

print(len(list_append))

# Робота зі словниками

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test.values())

print(dict_test.keys(), dict_test.values())

print(dict_test.items())