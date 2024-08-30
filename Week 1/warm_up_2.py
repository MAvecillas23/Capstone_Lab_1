"""This program asks the user how many classes they are being taken this semester and to enter their
classes and the program displays them"""

num_of_classes = int(input('How many classes are you taking this semester?')) # asks user how many classes they are taking
class_counter = 0 # class counter for while loop
classes = [] # empty list of classes for now

while class_counter < 4: # while the class_counter is less than the number of classes... keep looping
    class_name = input('Enter the name of the class: ')  # enter class name
    classes.append(class_name) # add entered class to the classes list
    class_counter = class_counter + 1 # class counter goes up by 1 every iteration

# display the classes to the user
print('The classes you are taking are:')
for c in classes:  # for loop that displays each class in a newline
    print(c)



