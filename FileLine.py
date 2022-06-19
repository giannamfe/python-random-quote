#Starting out
enterfile = input("Enter the file name: ")
file = open(enterfile, 'r')
linecount = 0

#Line count in text file
for line in file:
    linecount = linecount + 1

print("The number of lines in this txt. file is", linecount)

#Loop for reading file
while True:
    linenum = 0

    num = int(input("Please enter a line number or press 0 to quit: "))
    if num >=1 and num <= linecount:
        file = open(enterfile, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(lines)
    else:
        if num == 0:
            print("Thanks for using the program")
            break
#End of program