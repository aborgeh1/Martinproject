import math as m
def Triangle_area_calculation(List_of_sides):
    for element in List_of_sides:        #looping Through the List_of_sides
        if len(element)==2:          #checking whether it is a base and height method
            area=0.5*element[0]*element[1]       #calculating area
            print(f' area by base and height is {area} ')    #printing to the user
        else:                             #if its area by semi perimeter method
            avg=sum(element)/len(element)     #calculating the average
            area1=m.sqrt(avg*(avg-element[0])*(avg-element[1])*(avg-element[2]))    #calculating the area
            print(f' area by semi-perimeter method is {area1}')    #printing to the user

Triangle_area_calculation([(1,3),(6,5,2),(3,4),(5,4),(6,5,3)])     # calling of invoking the function
