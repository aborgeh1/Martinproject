def Calculator():
    total=[]
    while True:
        User_input=input('Enter Value or Arithmetic sign :')
        if User_input=='+' or User_input=='x' or User_input=='/' or User_input=='-' or User_input=='=' or User_input=='c':  #checking operators
            if User_input=='+':      #checking whether it is addition operation
                next_value=int(input('Enter Next Value: ')) #enter next value
                total.append(total[-1]+ next_value)       #add it to the total list datatype
                print(total[-1])                 # printing last item as a result
            elif User_input=='x':             #checking whether it is multiplication operation
                next_value=int(input('Enter Next Value: '))     #enter next value
                total.append(total[-1]* next_value)           #add it to the total list datatype
                print(total[-1])                        # printing last item as a result
            elif User_input=='/':                      #checking whether it is division operation
                next_value=int(input('Enter Next Value: '))      #enter next value
                total.append(total[-1] / next_value)          #add it to the total list datatype
                print(total[-1])                             # printing last item as a result
            elif User_input=='-':                         #checking whether it is subtraction operation
                next_value=int(input('Enter Next Value: '))    #enter next value
                total.append(total[-1] - next_value)               #add it to the total list datatype
                print(total[-1])                                # printing last item as a result
            elif User_input=='=':                   #checking whether equal sign is pressed
                print(total[-1])                     # printing last item as a result
            elif User_input=='c':                    #checking whether c is pressed to clear current results
                total.clear()                         #clear all including current results
                print(0)

        elif User_input.isdigit():                  #check if User_input string is likely to be a number
            total.append(int(User_input))           # add it to the empty list
        elif User_input.isalpha():                 # check if any alphabet is pressed
            print('Enter Number first')               #tell the user not to enter alphabet


Calculator()                   #invoking the function