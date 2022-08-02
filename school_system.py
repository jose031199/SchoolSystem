import os

def clear(): # Function to clear screen
    os.system('cls')

def menu(): #Code which will help us to display the menu
    options = 0
    try:
        while options!=6:
            options = int(input("Welcome to UNIDEP School System \n"
                        "Please Choose at option\n"
                        "1. Create Students \n"
                        "2. Edit Students \n"
                        "3. Delete Students\n"
                        "4. Upload Grades \n"
                        "5. Edit Grades \n"
                        "6. Exit \n"
                        "Please choose an option: "))
            if options == 1:
                print("\nCreate Students Option")
                clear()
            elif options == 2:
                print("\nEdit Students Option")
                clear()
            elif options == 3:
                print("\nDelete Students Option")
                clear()
            elif options == 4:
                print("\nUpload Grades Option")
                clear()
            elif options == 5:
                print("\nEdit Grades Options")
                clear()
            elif options ==6:
                print("\nGoodBye")
                clear()
            else:
                print("\nThere are only 5 options, try again")
                clear()
    except Exception as e:
        clear()
        print(f"{e}")
        menu()

menu()