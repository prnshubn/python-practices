a="this is some string"

# finds length of the string
print(f"length is {len(a)}")

# finds the index of first occurrence of a character
print(f"first occurrence index of s is {a.find("s")}")

# finds the index of last occurrence of a character
print(f"last occurrence index of s is {a.rfind("s")}")

# other important methods
# a.capitalize() -> turns all characters to uppercase
# a.lower() -> turns all characters to lowercase
# a.isdigit() -> returns true if string contains all digits
# a.isalpha() -> returns true if string contains only alphabets
# help(str) -> returns all the methods you can use with strings

# indexing = accessing elements of a sequence using [] (indexing operator)
# [start: end: step]
# [3] -> returns the character at that index
# [3:7] -> means starting and ending index (excluding ending index)
# [:5] -> means from index 0 till index 4
# [5:] -> means from index 5 till end
# [-1] -> -1 signifies the last index of a string, therefore -2 = 2nd last character of the string, so on
# [::2] -> gives every 2nd character of the string from start to end
# [-4:] -> gives the last four
# [::-1]) -> reverses a string