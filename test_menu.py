
menu_options = {
    1: 'Option 1',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

while(True):
    print_menu()
    option = int(input('Enter your choice: '))
    if option == 1:
        print('Handle option \'Option 1\'')
    elif option == 2:
        print('Handle option \'Option 2\'')
    elif option == 3:
        print('Handle option \'Option 3\'')
    elif option == 4:
        print('Thanks message before exiting')
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 4.')