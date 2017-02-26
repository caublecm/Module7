from sortedcontainers import SortedDict

def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Username')
    print('5. Quit')
    print()

# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

#display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    # use try/except to insure a integer number is entered
    try:
        menu_choice = int(input("Type in a number (1-5): "))
    except ValueError:
        print("That is not a number!\n".format(menu_choice))
    
    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x,y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x,y))
            
    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = username
      
        usernames[name] = username
        
    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name: ")
        if name in usernames:
            #if key exists in dictionary delete the key and value for that entry
            del usernames[name]
            #inform user the entry has been deleted
            print("Name: {} deleted\n".format(name))
        else:
            # if key does not exist state "not found"
            print("Name: {} not found\n".format(name))

    # view user name      
    elif menu_choice == 4:
        print("Lookup Username")
        name = input("Name: ")
        if name in usernames:
            #if key exists in dictionary delete the key and value for that entry
            username = usernames[name]
            #inform user the entry has been deleted
            print("Name: {}\tUserName: {} \n".format(name, username))
        else:
            # if key does not exist state "not found"
            print("Name: {} not found\n".format(name))
    
    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()
