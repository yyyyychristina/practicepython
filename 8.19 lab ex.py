'''
8.19 LAB: Contact list

A contact list is a place where you can store a specific contact with other associated information such as a phone number, email address, birthday, etc.
Write a program that first takes in word pairs that consist of a name and a phone number (both strings), separated by a comma.
That list is followed by a name, and your program should output the phone number associated with that name. Assume the search name is always in the list.

Ex: If the input is:

Joe,123-5432 Linda,983-4123 Frank,867-5309
Frank

the output is:

867-5309
'''



user_input = input()         
user_name = input()
contact_list = {}             #make an empty dict

entries = user_input.split()   #split the contacts by space into the entries



for i in range(len(entries)):            #for each pair in entries
    split_pair = entries[i].split(',')  #split a pair with comma into list called split_pair
    contact_list[split_pair[0]] = split_pair[1]

print(contact_list.get(user_name, 'N/A'))


