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
print("---------------")

print("---------------")
print("---------------")
print("---------------")
print("---------------")


# it will throw and error if it's out of range

