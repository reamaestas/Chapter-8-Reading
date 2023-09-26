#triple quotes allows us to creat strings that cover multiple lines

sentence = '''This string covers
multiple lines.
Cool!'''
print(sentence)
print("---------------")
#bracket notation
print(sentence[2])
print('sentence'[2])
print(len(sentence))
# this thows an error: print(sentence[len(sentence)])
# do this instead:
print(sentence[len(sentence)-1])
print("------USING NEGATIVE INDEX INTEGERS---------")
#left to right is zero basing indexes
#right to left the index value starts at -1
print(sentence[-2])
print('sentence'[-2])

print("---------------")

# ---- Try It! ----
this_string = 'Zero-based indexing!'

print(this_string[5])
 #note how there seems to be nothing printed bc it returns a space 
print('Alphabet soup'[-5])
print("-----slicing/substring----------")
alphabet = "abcdefghijklmnopqrstuvwxyz"
substring = alphabet[2:5]
print(substring)
#remember that the end index is NOT included in the substring

#working with empty start/stop index
fruit = "cucumber"
#beginningn to index 3 (not including 3)
print(fruit[:3])
#index 3 to last index
print(fruit[3:])
print("------saving substrings---------")
vegetable = "carrot"
print(len(vegetable))
top_half = vegetable[:3]
bottom_half = vegetable[3:]
end_piece = vegetable[-1]
print(top_half, bottom_half, end_piece)
print("----STRING IMMUTABLITY-----------")
title = 'the princess bride'
print(title)
title = 'The Princess Bride'
print(title)
#we aren't CHANGING the string, we are REPLACING the string
pet = 'dog'
print(pet +'s')
print(pet)
pet = 'cat'
print(pet)
pet +='s'
print(pet)
print("----str methods-----------")
print(vegetable.count('r'))
print(vegetable.find('a'))
print(vegetable.find('r')) #returns first occurance
print(vegetable.find('q')) #returns -1 if not found
print(vegetable.index('a'))
print(vegetable.index('r')) #returns first occurance
#if not found, throws an error 
# ie print(vegetable.index('q'))
print(vegetable.upper())
print(vegetable.lower())
print(vegetable.replace('r','f'))
print(vegetable.replace('q','f'))
#it wont replace what isnt there
print(vegetable.split('r'))
print(vegetable.split('a'))
print(vegetable.strip('c'))
#useful to strip spaces
print("---------------")
nonprofit = 'LaunchCode'
lowercase = nonprofit.lower()
meal_plan = nonprofit.replace("a", '')
print(nonprofit, lowercase, meal_plan)
print("---------SPECIAL CHARACTERS------")
print('A message,\nbroken across lines,\n\tand indented')
print("---------------")
print('Use newline\n\tand tab\n\t\tcharacters to\n\t\t\t create this\n\t\t output with\n\t a single\n print statement.')
print("-------other characters--------")
print('\u25E8	\u26bd')
#dont have to be capital or lowercase
print("-----template literals----------")
#this is concatenation
name = 'Jack'
current_age = 9
print("Next year, " + name + " will be " + str(current_age +1) + '.')
#this cleaner using .format
jacks_age = "Next year, {} will be {}."
print(jacks_age)
print(jacks_age.format(name, current_age + 1))
print("---------------")
my_string = 'Hello'
my_number = 3
my_expression = my_string * my_number

output = '''This is my string: "{}".
This is my_number: {}.
This is the length of my_string * my_number: {}'''

print(output.format(my_string, my_number, len(my_expression)))
print("-------index values of format()--------")
my_num = 10
num_output = '{} + {} + {} + {}'
print(num_output.format(my_num, my_num, my_num, 3*my_num))
#cleaner to use indeces
num_output = '{0} + {0} + {0} + {1}'
print(num_output.format(my_num, 3*my_num))
print("----can be called in any order-----------")
hello = "Hello, {1}. You turn {0} today. Happy birthday, {1}!"
print(hello.format(5, 'Anna'))
print("------- f-strings --------")
her_name = 'Caroline'
her_age = 9
hello_to_her = f"Hello, {her_name}! Can't wait until you turn {her_age +1}."
print(hello_to_her)
print("-----interate by index or characters-----")
for index in range(0, len(her_name), 2):
	print(her_name[index])
print("---------------")
	
for index in range(-1, -len(her_name), -2):
	print(her_name[index])
print("-------interation by item--------")
fruit = 'bananas'
fruit_copy = ''

for char in fruit:
	fruit_copy += char
	print(char, fruit_copy)
print("---------------")
for char in fruit:
	fruit_copy += char.upper() + fruit_copy
	print(char, fruit.count(char))

print("-------checking type--------")
my_var = True

if type(my_var) == str:
	print("The value '{0}' is a string.".format(my_var))
elif type(my_var) == float:
	print('The value of {0} is a float.'.format(my_var))
elif type(my_var) == bool:
	print('The value of {0} is a boolean.'.format(my_var))
else: 
	print('The value {} is NOT a string.'.format(my_var))
print("---------------")
#keep it DRY with:
print("The value {0} is a {1} data type.".format(my_var, type(my_var)))
print("----WE CAN USE COMPARISON OPERATORS ON STRINGS-----")
pet1 = 'dog'
pet2 = 'cat'
pet3= 'Crow'

print(pet1 == pet2)
print(pet2[0] == pet3[0])
#case matters
print(pet2[0].lower() == pet3[0].lower())

print(pet1 < pet2)
#i dont understand the last one bc its related to the unicode number value of the characters
print("---checking with in and not in ----")
movie = 'The Hunger Games'
search_char = 'e'

for char in movie:
	if char == search_char:
		print("'{0}' is in '{1}'".format(search_char, movie))

print("-------------")
#better approach
if search_char in movie:
	print("'{0}' is in '{1}'.".format(search_char, movie))
print("---------------")
#make the check for vowels case sensitive
text = "Armadillos or anteaters"
vowels = "aeiou"
vowel_count = 0
consonate_count = 0

for char in text:
	if char in vowels or char in vowels.upper():
		vowel_count += 1

print(f"'{text}' contains {vowel_count} vowels.")
print("---------------")
for char in text:
	if char not in vowels or char not in vowels.upper():
		consonate_count += 1

print(f"'{text}' contains {consonate_count} consonates.")
print("------ checking case ------")
character = 'a'
word = 'yep!'
non_letters = '$10.75'

print(character.isupper())
print(word.islower())
print(non_letters.isupper())
print(non_letters.islower())

print("------STRING MODULE---------")
import string

print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.punctuation)
print("-------------")
this_char = ''
if this_char == '':
	print(" '' is a space.")
elif this_char in string.ascii_lowercase:
	print("'{0} is a lowercase letter.'".format(this_char))
elif this_char in string.ascii_uppercase:
	print("'{0} is an uppercase letter.'".format(this_char))
elif this_char in string.digits:
	print("'{0} is a digit.'".format(this_char))
elif this_char in string.punctuation:
	print("'{0} is punctuation.'".format(this_char))
else:
	print("I don't know what the hell that is!")
print("-------------")

print("-------------")
print("-------------")
print("-------------")




