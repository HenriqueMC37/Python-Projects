import sys

#set counter variable for while loop
operation_sign = False
#start while loop for mathematical operation which will be dependent on what mathematical sign the user inputs
while operation_sign == False:
    #use a try-except block to make sure the user inputs a valid number for the first and second number
    try_number_one = False
    while try_number_one == False:
        try:
            first_number = int(input("Please enter a number: "))
            try_number_one = True
            break
        except ValueError:
            print("That was not a valid number, please input one again.")
            try_number_one = False

    try_number_two = False
    while try_number_two == False:
        try:
            second_number = int(input("Please enter a number: "))
            try_number_two = True
            break
        except ValueError:
            print("That was not a valid number, please try again")
            try_number_two == False

    #ask for the user's input for what mathematical operation he would like to perform
    operation_sign = input("Please enter the operation sign: ")
    
    '''Make if-elif-else block to select what kind of operation to do based on the user's input for operation_sign
    After every calculation, the program will append the result to a text file called 'output.txt'. Because the opening mode
    for the file is 'a', it will create a file called 'output.txt' if it doesn't exist. '''
    if operation_sign == "+":
        addition = first_number + second_number
        print(f"Addition = {str(first_number)} + {str(second_number)}")
        print(addition)
        with open('output.txt', 'a') as f:
            f.write(f'''\nAddition = {str(first_number)} + {str(second_number)}\nAddition = {str(addition)}\n''')
        
    
    elif operation_sign == "-":
        subtraction = first_number - second_number
        print(f"Subtraction = {str(first_number)} - {str(second_number)}")
        print(subtraction)
        with open('output.txt', 'a') as f:
            f.write(f'''\nSubtraction = {str(first_number)} - {str(second_number)}\nSubtraction = {str(subtraction)}\n''')
        
               

    elif operation_sign == "*":
        multiplication = first_number * second_number
        print(f"Multipication = {str(first_number)} * {str(second_number)}")
        print(multiplication)
        with open('output.txt', 'a') as f:
            f.write(f'''\nMultiplication = {str(first_number)} * {str(second_number)}\nMultiplication = {str(multiplication)}\n''')
        
    #For mathematical operations that would include division (division, modulus, floor division) there is a try-except block to make sure a number is not divided by zero
    
    elif operation_sign == "/":

        try:
            division = first_number / second_number
            print(f"Division = {str(first_number)} / {str(second_number)}")
            print(division)
            with open('output.txt', 'a') as f:
                f.write(f'''\nDivision = {str(first_number)} / {str(second_number)}\nDivision = {str(division)}\n''')
                         
        except ZeroDivisionError:
            print("We can't divide a number by zero, please start from the beginning.")
    
         
    elif operation_sign == "%":

        try:
            modulus = first_number % second_number
            print(f"Modulus = {str(first_number)} % {str(second_number)}")
            print(modulus)
            with open('output.txt', 'a') as f:
                f.write(f'''\nModulus = {str(first_number)} % {str(second_number)}\nModulus = {str(modulus)}\n''')
                
        except ZeroDivisionError:
            print("We can't divide a number by zero, please start from the beginning.")

        
    elif operation_sign == "//":

        try:
            floor_division = first_number // second_number
            print(f"Floor Division = {str(first_number)} // {str(second_number)}")
            print(floor_division)
            with open('output.txt', 'a') as f:
                f.write(f'''\nFloor Division = {str(first_number)} // {str(second_number)}\nFloor Division = {str(floor_division)}\n''')
                
        except ZeroDivisionError:
            print("We can't divide a number by zero, please start from the beginning.")

    #if the user input for operation sign is not any of the above then the program will ask the user to input a new one 

    else:
        print("That was not a valid operation sign. Please try again.")
        operation_sign = False

    #create a nested while loop for the choice the user will make for either a next operation, to read his previous operations or to exit the calculator
    choice = False
    
    while choice == False:
        choice = input("\nWould you like to do another calculation, check your previous operations or exit the program?\nReply with either: 'Calculation', 'Read' or 'Exit': ").lower()
        content = ""
        #if user chooses calculation the operation_sign value will be set to False again and the first while loop will reset
        if choice == "calculation":
            operation_sign = False

        #if user chooses to read the previous calculations he will be asked to give his file a title
        elif choice == "read":
            
            '''while loop with try-except block to make sure the user inputs a valid name for the file
            #We can check that the file has a valid name if the program is able to open the file without an error
            #occurring. In that case, we can break out of the loop and continue with the copying and reading the file'''
            file_name = False
            while file_name == False:
                file_name = input("\nWhat would you like your file to be called?\n")

                # If the file does not have '.txt' in its name, then the program will add it to the name.
                try: 
                    if ".txt" not in file_name:
                        file_name = file_name + ".txt"
                    f = open(file_name, 'w')
                    f.close()
                    break
                
                #Exception on EnvironmentError was the exception that worked the best for invalid file names
                except EnvironmentError:
                    print("\nThat's not a valid file name, please try again.\n")
                    
                
                file_name = False
                    
            
            '''The reason I put the mode 'w' for the secondfile was so that even if the user asks for the same 
            file name again, then it will just overwrite what the user already had on that file so long as 
            the user does not delete the output.txt file. '''

            # copy the contents of output.txt to the newly created file
                
            with open('output.txt', 'r') as firstfile, open(file_name, 'w') as secondfile:
                        for line in firstfile:
                            secondfile.write(line)
               
            #read the contents of that newly created file
            with open(file_name, 'r+') as f:
                    for line in f:
                        content = content + line
                    print(content)

        #give an option to exit the program without doing another calculation or read the previous calculations
        elif choice == "exit":
            sys.exit()

        else:
            print("You did not choose a valid option, try again.")
            choice = False


    

