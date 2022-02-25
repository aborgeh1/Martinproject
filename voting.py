import pandas
def Shop_app(pin,Account_users,product_quantity,productname,productprice,productdate):
    User_name=input('Enter your username>>')
    Enter_pin=int(input('Enter Your pin>>>'))
    if Enter_pin==pin:
        print(f'{User_name} you have successfully logged in into the system')
        print(f'{User_name} what do you want to do')
        while True:
            Enter_Choice=int(input('Enter 1 for product entry,2 for checking one product quantity,3 for total products,4 For item bought>> or 5 to view all items in stock'))
            if Enter_Choice==1:
                Account_users[User_name] = pin
                Product_name = input('Enter Product name>>')
                product_price = float(input('Enter product price>>'))
                Product_Quantity_supplied = int(input('Enter Quantity supplied>>'))
                Date_Received = input('Enter Date Date_Received in the format')
                product_quantity.append(Product_Quantity_supplied)
                productname.append(Product_name)
                productprice.append(product_price)
                productdate.append(Date_Received)
            elif Enter_Choice==2:
                print(productname)
                zipped=zip(productname,product_quantity)
                Enter_product_name=input('Enter product>>')
                h=0
                for item in zipped:
                    if item[0]==Enter_product_name:h=item[1]
                print(f'The total number of {Enter_product_name} is {h}')
            elif Enter_Choice==3:print(f'The total Products in stock is {sum([quantity[1] for quantity in zip(productname,product_quantity)])}')
            elif Enter_Choice==4:
                Name_of_product=input('Enter name of Product sold')
                Enter_Quantity_Sold=int(input('Enter Quantity Sold>>'))
                zipped=zip(productname,product_quantity)
                for entered_name in zipped:
                    if entered_name[0]==Name_of_product:
                        zipped[entered_name[1]]=zipped[entered_name[1]]-Enter_Quantity_Sold
                print(f'Total quantity left in stock is {sum([quantity[1] for quantity in zip(productname,product_quantity)])}')
            elif Enter_Choice==5:print(pandas.DataFrame({'Product_Names':productname,'Product_quantity':product_quantity,'Product_Price': productprice,'ProductDate':productdate}))
    else:print(f'{User_name} you have wrongfully entered your name')
Shop_app(1242,{},[],[],[],[])


