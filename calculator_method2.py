def Calculator():
    total=0
    while True:
        User_input=input('Enter Value or Arithmetic sign :')
        if User_input=='+' or User_input=='x' or User_input=='/' or User_input=='-' or User_input=='=' or User_input=='c':  #checking operators
            if User_input=='+':      #checking whether it is addition operation
                next_value=int(input('Enter Next Value: ')) #enter next value
                total=total+ next_value       # perform addition operation and reassign to total
                print(total)                 # printing current total results
            elif User_input=='x':             #checking whether it is multiplication operation
                next_value=int(input('Enter Next Value: '))     #enter next value
                total=total* next_value           # perform multiplication operation and reassign to total
                print(total)                        # printing current total results
            elif User_input=='/':                      #checking whether it is division operation
                next_value=int(input('Enter Next Value: '))      #enter next value
                total=total / next_value          # perform division operation and reassign to total
                print(total)                             # printing current total results
            elif User_input=='-':                         #checking whether it is subtraction operation
                next_value=int(input('Enter Next Value: '))    #enter next value
                total=total - next_value               # perform subtraction operation and reassign to total
                print(total)                                # printing current total results
            elif User_input=='=':                   #checking whether equal sign is pressed
                print(total)                     # printing current total results
            elif User_input=='c':                    #checking whether c is pressed to clear current results
                total=0                         #resets total to zero
                print(0)

        elif User_input.isdigit():                  #check if User_input string is likely to be a number
            total=int(User_input)          #convert to integer and reassign to total
        elif User_input.isalpha():                 # check if any alphabet is pressed
            print('Enter Number first')               #tell the user not to enter alphabet


Calculator()                   # invoking the function