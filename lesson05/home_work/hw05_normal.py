import os
import sys 


if sys.argv[1] == "1":
    directory = input("Enter directory full path>> ")
    print (os.path.dirname(directory))
    os.chdir(os.path.dirname(directory))
    print (directory, "is current directory now")
elif sys.argv[1] == "2":
    files = os.listdir(os.curdir) 
    print (files)
elif sys.argv[1] == "3":
    directory = input("Enter directory full path>> ")
    os.rmdir(os.path.dirname(directory))
    print (directory, "deleted")
elif sys.argv[1] == "4":
    directory = input("Enter directory full path>> ")
    os.makedirs(os.path.dirname(directory))
    print (directory, "created")
