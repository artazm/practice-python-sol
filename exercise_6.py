# String Lists

string = input('Please enter a string: ')
string_length = len(string)

reverse_string = string[string_length::-1]

print(string == reverse_string)
