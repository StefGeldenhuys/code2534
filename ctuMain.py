from ctuClass import ctuStock                #Imported class from ctuClass
#Declare Variables for 4 difffrent shops
stock1 = ctuStock("default", "default", 0, 0, 0)
stock2 = ctuStock("default", "default", 0, 0, 0)
stock3 = ctuStock("default", "default", 0, 0, 0)
stock4 = ctuStock("default", "default", 0, 0, 0)
#The functions that displays my menu's


def mainmenu():
    print("-----------------------------\nWelcome to CTU Technologies\n-----------------------------\n"
          "1.  Shop management\n2.  Sales\n3.  Returns\n4.  Stock\n99. Exit\n"
          "-----------------------------")
    option1 = int(input("Select an option: "))
    if option1 == 1:
        shopmanage()
    if option1 == 2:
        sales()


def shopmanage():
    print("1. Change Shop Name\n2. Change Shop Location\n3. Display Current Shops\n4. Display all Shops Information"
          "\n0. Back\n")
    option2 = int(input("Select an Option: "))
    if option2 == 1:
        changeshopname()
    if option2 == 2:
        changeshoplocal()
    if option2 == 3:
        dispcurrshops()
    if option2 == 4:
        dispallshops()
    if option2 == 0:
        mainmenu()


def changeshopname():
    print("1.", stock1.shopName, "\n2.", stock2.shopName, "\n3.", stock3.shopName, "\n4.", stock4.shopName, )
    option3 = int(input("\nSelect an Option: "))
    if option3 == 1:
        newshopnam = input("New Shop Name?:")
        stock1.shopName = newshopnam
        print("Shop name succecfully changed to", stock1.shopName)
    elif option3 == 2:
        newshopnam1 = input("New Shop Name?:")
        stock2.shopName = newshopnam1
        print("Shop name succecfully changed to", stock2.shopName)
    elif option3 == 3:
        newshopnam2 = input("New Shop Name?:")
        stock3.shopName = newshopnam2
        print("Shop name succecfully changed to", stock3.shopName)
    elif option3 == 4:
        newshopnam3 = input("New Shop Name?:")
        stock4.shopName = newshopnam3
        print("Shop name succecfully changed to", stock4.shopName)
    else:
        print("\nInvalid input, Select a Valid option\n")
        shopmanage()


def changeshoplocal():
    print("1.", stock1.shopName, ",", stock1.shopLocation, "\n2.", stock2.shopName, ",", stock2.shopLocation, "\n3.",
          stock3.shopName, ",", stock3.shopLocation, "\n4.", stock4.shopName, ",", stock4.shopLocation)
    option4 = int(input("\nSelect an Option:"))
    if option4 == 1:
        newshoplocal = input("New Shop Location?: KZN/Free State/Gauteng/Limpopo/Default/\n")
        if newshoplocal == "KZN" or "Free State" or "Gauteng" or "Limpopo" or "Default":
            stock1.shopLocation = newshoplocal
            print("Shop Location has officially been changed to", stock1.shopLocation)
        else:
            print("Invalid Location")
    elif option4 == 2:
        newshoplocal1 = input("New Shop Location?: KZN/Free State/Gauteng/Limpopo/Default/\n")
        if newshoplocal1 == "KZN" or "Free State" or "Gauteng" or "Limpopo" or "Default":
            stock2.shopLocation = newshoplocal1
            print("Shop Location has officially been changed to", stock2.shopLocation)
        else:
            print("Invalid Location")
    elif option4 == 3:
        newshoplocal2 = input("New Shop Location?: KZN/Free State/Gauteng/Limpopo/Default/\n")
        if newshoplocal2 == "KZN" or "Free State" or "Gauteng" or "Limpopo" or "Default":
            stock3.shopLocation = newshoplocal2
            print("Shop Location has officially been changed to", stock3.shopLocation)
        else:
            print("Invalid Location")
    elif option4 == 4:
        newshoplocal3 = input("New Shop Location?: KZN/Free State/Gauteng/Limpopo/Default/\n")
        if newshoplocal3 == "KZN" or "Free State" or "Gauteng" or "Limpopo" or "Default":
            stock4.shopLocation = newshoplocal3
            print("Shop Location has officially been changed to", stock4.shopLocation)
        else:
            print("Invalid Location")


def dispcurrshops():
    print("1. ",stock1.shopName, ",", stock1.shopLocation, "\n2. ", stock2.shopName, ",", stock2.shopLocation,
          "\n3. ", stock3.shopName, ",", stock3.shopLocation,"\n4. ", stock4.shopName, ",", stock4.shopLocation)

def incrementcustomers():
    print("1. ", stock1.shopName, "\n2. ", stock2.shopName, "\n3. ", stock3.shopName, "\n4. ", stock4.shopName)
    shop = input("What shop do you want the item to be shipped from")
    







def dispallshops():
    print("------------------------\nShop Name: ",stock1.shopName,"\nShopLocation: ",stock1.shopLocation,
          "\nNumber of Customers: ",stock1.customers,"\nCurrent Sales: ",stock1.sales,"\nReturns: ",stock1.returns)
    print("------------------------\nShop Name: ", stock2.shopName, "\nShopLocation: ", stock2.shopLocation,
          "\nNumber of Customers: ", stock2.customers, "\nCurrent Sales: ", stock2.sales, "\nReturns: ", stock2.returns)
    print("------------------------\nShop Name: ", stock3.shopName, "\nShopLocation: ", stock3.shopLocation,
          "\nNumber of Customers: ", stock3.customers, "\nCurrent Sales: ", stock3.sales, "\nReturns: ", stock3.returns)
    print("------------------------\nShop Name: ", stock4.shopName, "\nShopLocation: ", stock4.shopLocation,
          "\nNumber of Customers: ", stock4.customers, "\nCurrent Sales: ", stock4.sales, "\nReturns: ", stock4.returns,
          "\n------------------------")

def sales():
    item = int(input("Select an item you want to buy:\n1. Laptops\n2. Computer Parts\n3. Hardware Parts\n"
                     "4. Study Textbooks"))
    ammount = int(input("How much of these items do you need."))
    incrementcustomers()




    if item == 1:

        print("Your", ammount, "Laptops will be shipped to your chosen store.")
    elif item == 2:

        print("Your", ammount, "Computer Parts will be shipped to your chosen store.")
    elif item == 3:

        print("Your", ammount, "Hardware Parts will be shipped to your chosen store.")
    elif item == 4:

        print("Your", ammount, "Study Text books will be shipped to your chosen store.")
    else:
        print("invalid")









while True:
    mainmenu()
    input("\nPress ENTER to return to Main Menu")
