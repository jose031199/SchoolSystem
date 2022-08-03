import os


def clear():  # Function to clear screen
    os.system('cls')


def menu():  # Code which will help us to display the menu
    options = 0
    schools = {
        "students": [],
        "grades": {
            "math": []
        }
    }
    try:
        while options != 6:
            options = int(input("Welcome to UNIDEP School System \n"
                                "Please Choose at option\n"
                                "1. Create Students \n"
                                "2. Show Students \n"
                                "3. Delete Students\n"
                                "4. Upload Grades \n"
                                "5. Consult Grades \n"
                                "6. Exit \n"
                                "Please choose an option: "))
            if options == 1:
                # print("\nCreate Students Option")
                addStudents(schools)
                clear()
            elif options == 2:
                # print("\nEdit Students Option")
                showStudents(schools)
                clear()
            elif options == 3:
                # print("\nDelete Students Option")
                deleteStudents(schools)
                clear()
            elif options == 4:
                # print("\nUpload Grades Option")
                addGradesStudents(schools)
                clear()
            elif options == 5:
                # print("\nEdit Grades Options")
                consult_Grades(schools)
                clear()
            elif options == 6:
                print("\nGoodBye")
                clear()
            else:
                print("\nThere are only 5 options, try again")
                clear()
    except Exception as e:
        clear()
        print(f"{e}")
        menu()


def addStudents(list):  # Option 1
    try:
        name = input("Insert the students name:")
        list["students"].append(name)

    except Exception as e:
        print(f"Error {e}")


def showStudents(list):  # Option 2
    if len(list["students"]) > 0:
        for x in list.get("students"):
            print(f"Name: {x}")
    else:
        print('There are not students')


def deleteStudents(list):  # Option 3
    try:
        name = input("Search the student")
        if search_students(list, name):
            list["students"].remove(name)
        else:
            print(f"No student has that name {name}")
    except Exception as e:
        print(f"There are not students with that name {e}")


def addGradesStudents(list):  # Option 4 add Grades for student
    try:
        count = 0
        if len(list.get("students")) > 0:
            for name in list.get("students"):
                grade_math = int(input(f"Grade in math for {name}: "))
                list["grades"]["math"].append(grade_math)

    except Exception as e:
        print(f"Error {e}")


def consult_Grades(list):  # Option 5 to consult grades for each student
    try:
        name = input("Search the student: ")
        if search_students(list, name):
            pos = list.get("students").index(name)
            print(f"Math Grades {name} is {list['grades']['math'][pos]}")
        else:
            print(f"No student has that name {name}")
    except Exception as e:
        print(f"There are not students with that name {e}")


def search_students(list, name): # Search for students name if exists
    find = False
    if name in list.get("students"):
        find = True
    else:
        find = False
    return find


menu()
