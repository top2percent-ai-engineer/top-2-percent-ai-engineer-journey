import os
import shutil

def list_files():
    files = os.listdir()
    for value in files:
        print(value)

def create_files():
    filename = input("Enter Filename: ")
    if (os.path.exists(filename) and os.path.isfile(filename)):
            print("File Already Exists!")
    else:
        with open("filename","w") as f:
            f.write("")
        print("File Created Successfully!")

def create_folder():
     foldername = input("Enter Foldername: ")
     if (os.path.exists(foldername) and os.path.isdir(foldername)):
          print("Folder Already Exists!")
     else:
         os.mkdir(foldername)
         print("Folder created Successfuly!")

def search_folder():
     foldername = input("Enter Foldername: ")
     if (os.path.exists(foldername) and os.path.isdir(foldername)):
          print("Folder Already Exists!")
     else:
         print("Folder Not Exists!")

def search_file():
     filename = input("Enter Filename: ")
     if (os.path.exists(filename) and os.path.isfile(filename)):
            print("File Already Exists!")
     else:
        print("File Not Exists!")

def remove_file():
     filename = input("Enter Filename: ")
     if (os.path.exists(filename) and os.path.isfile(filename)):
            os.remove(filename)
            print("File removed Successfully!")
     else:
        print("File Not Found!")

def remove_folder():
    foldername = input("Enter Foldername: ")
    if (os.path.exists(foldername) and os.path.isdir(foldername)):
          shutil.rmtree(foldername)
          print("Folder removed Successfully")
    else:
         print("Folder Not Exists!") 

def move_item():
     source = input("Enter the File you want to move!")
     destination = input("Where to move the file!")
     if (os.path.exists(source)):
       shutil.move(source,destination)
       print("File moved!")
     else:
       print("File not Exists!")

def rename_item():
     older_name = input("Enter the Filename / Foldername")
     new_name = input("Enter the Newname")
     files = os.listdir()
     if (os.path.exists(older_name)):
               os.rename(older_name,new_name)
     else: 
        print("File not Found")


while True:
    print("Welcome to CLI Flash")
    print("1. List Files")
    print("2. Create File")
    print("3. Create Folder")
    print("4. Search File")
    print("5. Search Folder")
    print("6. Remove File")
    print("7. Remove Fiolder")
    print("8. Move File / Folder")
    print("9. Rename File / Folder")
    print("10. Exit")
    choice = input("Enter your Choice: ")
    if not  choice.isDigit():
         print("Must Enter a Digit")
         continue
    else:
         choice = int(choice)
    if (choice == 1):
        list_files()
    elif (choice == 2):
         create_files()
    elif (choice == 3):
         create_folder()
    elif (choice == 4):
         search_file()
    elif (choice == 5):
         search_folder()
    elif (choice == 6):
         remove_file()
    elif (choice == 7):
         remove_folder()   
    elif (choice == 8):
         move_item()
    elif (choice == 9):
         rename_item()
    elif (choice == 10):
        print("Exiting ...")
        break
    else:
        print("Invalid Choice Entered!")