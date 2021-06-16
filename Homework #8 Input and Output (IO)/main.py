# On start up, it prompt's user for a filename.

# If the entered file name that doesn't exist, it prompt's them to enter the text they want to write to the file. After they enter the text, it saves the file and exit.

# If entered file name already exists, it ask the user if they want to:

# A) Read the file
# B) Delete the file and start over
# C) Append the file
# D) Replace a single line

# If the user wants to read the file it simply show the contents of the file on the screen. 
# If the user wants to start over then the file will be deleted and another empty one made in its place. 
# If a user elects to append the file, then they are able to enter more text, and that text is added to the existing text in the file. 
# If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:

# 1) The line number they want to update.
# 2) The text that should replace that line.

# import os.path
from os import path

filename = input("Please Enter the Filename\n")

if path.exists(filename):
    while True:
        print("A) Read the file\nB) Delete the file and start over\nC) Append the file\nD) Replace a single line\nE) Exit\n")
        option = input("Enter the option\n")
        if option =='A' or option =='a':
            with open(filename) as notes:
                for note in notes:
                    print(note,end="")
                notes.close()
        elif option == 'B' or option == 'b':
            with open(filename,"w") as notes:
                line = input("Please enter the data you want write to a file.\nPress enter to change line.\nType 'end' to close file.\n")
                while not line.lower() == "end":
                    notes.write(line+"\n")
                    line = input()
                notes.close()
        elif option == 'C' or option == 'c':
            with open(filename,"a") as notes:
                line = input("Please enter the data you want write to a file.\nPress enter to change line.\nType 'end' to close file.\n")
                while not line.lower() == "end":
                    notes.write(line+"\n")
                    line = input()
                notes.close()
        elif option == 'D' or option == 'd':
            with open(filename,"r") as notes:
                tempdata = []
                for note in notes:
                    tempdata.append(note)
                    print(note,end="")
                print()
                notes.close()
            with open(filename,"w") as notes:
                lineNumber = int(input("Enter the line number you want to replace\n"))
                newline = input("Enter the text you want to replace it with\n")
                tempdata[lineNumber-1] = newline+"\n"
                for line in tempdata:
                    notes.write(line)
                print("The file has been updated")
                notes.close()
        elif option =='E' or option =='e':
            break
        else:
            print("Please choose the correct option.")
else:
    with open(filename,"w") as notes:
        print("The entered file name does not exist")
        line = input("Please enter the data you want write to a file.\nPress enter to change line.\nType 'end' to close file.\n")
        while not line.lower() == "end":
            notes.write(line+"\n")
            line = input()
        notes.close()