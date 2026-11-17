#1) Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
result = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4

#2) Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string5 = 'Coding'
string6 = 'For'
string7 = 'All'
result2 = string5 + ' ' + string6 + ' ' + string7
#3) Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
#4) Print the variable company using print().
print(company)
#5) Print the length of the company string using len() method and print().
print(len(company))
#6) Change all the characters to uppercase letters using upper() method.
print(company.upper())
#7) Change all the characters to lowercase letters using lower() method.
print(company.lower())
#8) Use capitalize(), title(), swapcase() methods to format the value of the string
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9) Cut(slice) out the first word of Coding For All string.
print(company[0:6])
#10) Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))  # returns the index of the first occurrence of 'Coding'
print(company.index('Coding'))  # returns the index of the first occurrence of 'Coding'
print('Coding' in company)  # returns True if 'Coding' is found in the string
#11) Replace the word coding in the string 'Coding For All' to 'Python for Everyone'.
new_company = company.replace('Coding', 'Python for Everyone')
print(new_company)
#12) Change Python for Everyone to Python for All using the replace() method.
new_company2 = new_company.replace('Python for Everyone', 'Python for All')
print(new_company2)
#13) Split the string 'Coding For All' using space as the separator (split())
split_company = company.split(' ')
print(split_company)
#14) "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma and change it to a list.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
company_list = companies.split(', ')
print(company_list)
#15) What is the character at index 0 in the string Coding For All.
print(company[0])
#16) What is the character at index 10 in the string Coding For All.
print(company[10])
#17) What is the last index of the string Coding For All.
print(len(company) - 1)
#18) What character is at index 7 in the string Coding For All.
print(company[7])
#19) What is the character at index -1 in the string Coding For All.
print(company[-1])
#20) What is the character at index -5 in the string Coding For All.
print(company[-5])
#21) Slice the string Coding For All from index 0 to 5.
print(company[0:6]) 
#22) Slice the string Coding For All from index 7 to 11.
print(company[7:12])
#23) Slice the string Coding For All from index 12 to 15.
print(company[12:16])
#24) Check if the string Coding For All starts with a substring Coding using the method startswith().
print(company.startswith('Coding'))
#25) Check if the string Coding For All ends with a substring coding using the method endswith().
print(company.endswith('coding'))
#26) "   Coding For All      "  , remove the left and right trailing spaces in the string using the strip() method.
string_with_spaces = "   Coding For All      "
print(string_with_spaces.strip())
#27) Remove all the spaces in the string 'Coding For All' using the replace() method.
print(company.replace(' ', '')) 
#28) Change 'Coding For All' to 'Python For All' using the replace() method.
print(company.replace('Coding', 'Python'))
#29) Split the string 'Coding For All' at the space.
print(company.split(' '))
#30) "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma and change it to a list.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
company_list = companies.split(', ')
print(company_list)
#31) Create an acronym or an abbreviation for the name 'Python For Everyone'
s='Python For Everyone'
acronym = ''.join(word[0] for word in s.split())
print(acronym)
#beginner friendly
s = 'Python For Everyone'
words = s.split()
acronym = ''
for word in words:
    acronym += word[0]
print(acronym)
#Use index to determine the position of the first occurrence of C in Coding For All
print(company.index('C'))
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.find('because'))
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:47])
#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
# Does 'Coding For All' start with a substring _Coding_?
print(company.startswith('Coding'))
# Does 'Coding For All' end with a substring _coding_?
print(company.endswith('coding'))
#'&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
string_with_spaces = '   Coding For All      '
print(string_with_spaces.strip())
#Which one of the following variables return True when we use the method isidentifier():
print('30DaysOfPython'.isidentifier())  # True
print('thirty_days_of_python'.isidentifier())  # True
#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))
#Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")
#Use a tab escape sequence to write the following lines.
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))
#Use the string formatting method to display the following:
a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))