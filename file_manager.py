import os, os.path, time


def Number_files():
    print("What is the way of the directory")
    b =str(input()) 
    if os.path.exists(b): 
        c = len([name for name in os.listdir(b) if os.path.isfile(os.path.join(b,name))]) #Длина от  пробегаем по листу директории и возвращам все файлы, если это файл директории которую мы ввели. isfile - проверка является ли он файлом.
        print(c)
    else:
        print("File do not exist, sorry")
        print("Do you want to continue?")
        p = str(input())
        if(p == "yes" or p== "Yes"):
            Start_menu()
        else:
            print("Good bye")


def Number_directory():
    print("What is the way of the directory")
    a = str(input())
    if os.path.exists(a): 
        c = len([name for name in os.listdir(a) if os.path.isdir(os.path.join(a,name))])
        print(c)
    else:
        print("Directory do not exist, sorry")
        print("Do you want to continue?")
        p = str(input())
        if (p == 'yes' or p == 'Yes'):
            Start_menu()
        else:
            print("Good buy. Have a nice day!")

        


def Change_directory(s):
    print('''What is the directory''')
    b = str(input())
    os.chdir(b) #Следуем к новой директории
    print('Directory changed')
    if s == 'f' or s == 'F':
        Work_files()
    else:
        Start_menu()



def Rename_file():
    print("Write your directory")
    directory = input()
    print("Write the file you want to rename")
    file_1 = input()
    print("Write new file name")
    file_2 = input()
    old_file = os.path.join(directory, file_1)
    new_file = os.path.join(directory, file_2)
    if os.path.exists(old_file):
        os.rename(old_file, new_file)
        print("Completed! The file was renamed!")
    else:
        print("File do not exist, sorry")
        print("Do you want to continue?")
        p = str(input())
        if(p == "yes" or p== "Yes"):
            Start_menu()
        else:
            print("Good bye")
        


def Return_patern_dir():
    print("Write your path to the file")
    yourpath = input()
    if os.path.exists(yourpath):
        print ("Parent directory is - " + os.path.abspath(os.path.join(yourpath, os.pardir)))
    else:
        print("File do not exist, sorry")
        print("Do you want to continue?")
        p = str(input())
        if(p == "yes" or p== "Yes"):
            Start_menu()
        else:
            print("Good bye")



def Add_text():
    print("What is the name of file?")
    b = input()
    if os.path.exists(b):
        print("What are you want write here?")
        c = str(input())
        f = open (b,'a')
        f.write(c)
        print("New content has been added!")
        f.close
    else:
        print("File do not exist, sorry")
        print("Do you want to continue?")
        p = str(input())
        if(p == "yes" or p== "Yes"):
            Start_menu()
        else:
            print("Good bye")


def Rewrite_content():
    print("What is the name of file?")
    b = input()
    if os.path.exists(b):
        print("What are you want write here?")
        c = str(input())
        f = open (b, 'r+')
        f.write(c)
        f.close
    else:
        print("File do not exist, sorry")
        print("Do you want to continue?")
        p = str(input())
        if(p == "yes" or p== "Yes"):
            Start_menu()
        else:
            print("Good bye.")


def Delete_file():
    print("File name is?")
    b = str(input()) 
    if os.path.exists(b): 
        os.remove(b) 
        print("File was deleted!")
    else:
        print("File do not exist, sorry")
    print("Do you want to continue?")
    p = str(input())
    if p == "yes" or p == "Yes":
        Start_menu()
    else:
        print("Good bye.")


def Add_file():
    print("Write the path of the directory")
    directory = input()
    print("Name of the new file")
    new_file = input()
    path = os.path.join(directory, new_file)
    function = open(path, 'w')
    print("You have created a new file!")
    print("Do you want to continue?")
    p = input()
    if p == "yes" or p == "Yes":
        Start_menu()
    else:
        print("Good bye.")


def Add_directory():
    print("Write the path of the directory")
    directory = input()
    print("Write new directory")
    new_directory = input()
    f = os.path.join(directory,new_directory)
    os.mkdir(f)
    print("You create new directory!")
    print("Do you want to continue?")
    p = input()
    if p == "yes" or p == "Yes":
        Start_menu()
    else:
        print("Good bye.")


def List_content_directory():
    print("Write the path of the directory")
    directory = input()
    print("Here is your directory content:")
    for file in os.listdir(directory):
        print(file)
    print("Do you want to continue?")
    p = input()
    if p == "yes" or p == "Yes":
        Start_menu()
    else:
        print("Good bye.")
    


def Rename_directory():
    print("What is the way of the directory")
    b = str(input()) 
    if os.path.exists(b): 
        print('What the new name')
        c = str(input())
        os.rename(b, c)         


def Work_directory():
    print('''
    1 - rename directory
    2 - number of files in directory
    3 - print number of directories
    4 - list content of the directory
    5 - add file to this directory
    6 - add new directory to this directory
    ''')
    command = input()
    if command == '1':
        Rename_directory()
    elif command == '2':
        Number_files()
    elif command == '3':
        Number_directory()
    elif command == '4':
        List_content_directory()
    elif command == '5':
        Add_file()
    elif command == '6':
        Add_directory()


def Work_files():
    print(''' 
    1 - delete file
    2 - rename file
    3 - add new content text in file
    4 - rewrite content of this file
    5 - return to the parent directory
    ''')
    command1 = input()
    if command1 == '1':
        Delete_file()
    elif command1 == '2':
        Rename_file()
    elif command1 == '3':
        Add_text()
    elif command1 == '4':
        Rewrite_content()
    elif command1 == '5':
        Return_patern_dir()



def Start_menu():
    print('''What do you want?
    - If work with directory press d or D
    - If work with file press f or F
    ''' )
    s =input()
    if s == 'd' or s == 'D':
        Work_directory()
    elif s == 'f' or s == 'F':
        Change_directory(s)


Start_menu()

