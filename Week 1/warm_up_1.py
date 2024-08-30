"""" This program asks for the users name and their birth month"""

name = input('What is your name? ')  # asks user for name
birth_month = input('What month were you born in? ')  # asks user for birth month
upper_month = birth_month.lower().capitalize()  # capitalizes the first letter in the users birth month


print(f'Hello {name}!')  # prints greeting 
print(f'{name} contains {len(name)} letters!') # prints the number of characters in users name


# if august is in the users birth month
if 'August' == upper_month:
    print('Happy Birthday month!')  # tells user its their birthday month




    