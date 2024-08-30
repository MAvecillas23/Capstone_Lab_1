print('Hello capstone!') #printing 

# Variables-- varibles can be made using camelCase or snake_case
school = 'MCTC' #string
gpa = 4.0  #float
students_in_class = 22 #integers


# if/elif/else -statements--- a colon is needed to create an if statement
# the indent is the conditional code under if statements
if gpa == 4:
    print('WOW!')
elif gpa > 3:
    print('Awesome!')
else:
    print('Cool!')

# lists
schools = ['MCTC', 'DCTC', 'North Hennepin Technical College'] # create a list
if 'MCTC' in schools: # the "in" operator checks something is in a list
    print('MCTC is one of the schools in the list')

# things to do with lists
schools.sort() # sorts list in alphabetical order
print(schools)

schools.append('Century College') # adds new string to end of schools list
print(schools) 

schools.reverse() # returns list reversed
print(schools)



# strings
class_name = 'Software Development Capstone'
print(class_name.upper()) # every character in class_name is upper case
print(len(class_name)) # number of characters in class_name string
print(class_name.split()) # splits characters by whitespace and creates a list with the splitted strings
print(class_name.split('o')) # splits string by the character 'o' and creates a list of splitted strings

# string and if statement example
if 'Capstone' in class_name:
    print('This must be the capstone')

# loops - for loops over range
# for loop that prints ints 0-9 in a newline... vertically
for x in range(10):
    print(x)

# loops - for loops over sequence
for s in schools:  # for loop is used to print each element in a list in a newline 
    print(s.upper())

for letter in school: # using the school variable...
                      # this for loop prints every letter in the school variable
    print(letter)

# while loops
name = input('Enter your name')         #--- example of an input statement as well
while len(name) == 0:                   # while length of name is equal to 0
    print('Please enter at least one character') # tells user to enter at least one charcter
    name = input('Enter your name') # ask again under name variable

name = input('Name?')
print(name)

# True and False and None

start_of_semester = True
winter = False

if winter:
    print('brr!')
else:
    print('it is not winter')


# Dictionaries... Keys and Values
class_codes = {2905: 'Capstone', 2560: 'Web', 2545: 'Java'} # create a dictionary.. curly brackets
for code in class_codes:
    print(code)  # prints class codes.. keys
    print(class_codes[code])  # prints key and values
    print(class_codes[2560]) # prints the value of the key 2560

# another way to print a for loop using dictionaries
for code, name in class_codes.items():
    print('The class code is ' + str(code) + ' and the name is ' + name)

# formatting the print string above 

print(f'The class code is {code} and the name is {name}')


# slicing strings, lists
first_two = schools[0:2]  # slice and print indexes 0 through 2 minus the index 2 from the schools lists
print(first_two)

school_name = 'Minneapolis Community and Technical College'
city = school_name[:11]
print(city)

last_school = schools[-1] # slices and returns the last position of the schools list
print(last_school)

last_two_schools = schools[-2:]  # slice and return schools beginning at -2  ending at 0
print(last_two_schools)


# File IO
with open ('data.txt') as f:  # read file and print
    print(f.read())

with open('schools.txt', 'w') as f:  # writes the info from data txt file to a new file called schools.txt
    f.writelines(schools)

# Functions
def get_name():  # def is what creates the function 
    print('Hello, please enter your name!')
    name = input('Your name is: ')
    return name  # returns name to wherever it was called from  

name = get_name()