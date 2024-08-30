# This program turns a sentence into camelCase

sentence = input('Enter a sentence you would like turned into camelCase: ') # asks user to enter a sentence

sentence_list = sentence.split()  # splits sentence by the whitespace... and turns it into a list
camel_list = [] # this will be the camelCased list
camel_list.append(sentence_list[0].lower())  # append the first item in the sentence_list to the camel_list and lowercase it


# for loop that loops the items in index 1 and beyond and capitalizes the first letter in each string
for sentence in sentence_list[1:]:
    cap_sentence = sentence.capitalize()
    camel_list.append(cap_sentence)   # appends newly capitalized string to the camel_list list


# seperator needed to join the camel_list list together
sep = ''
camel_case = sep.join(camel_list) # joins the list and turns into a string

# display to user
print('Your sentence turned into camelCase is: ')
print(camel_case)


    



