print "Welcome to the menu programme!"
menu={}
while True:
    dish=raw_input("Please enter the name of the dish")
    price=raw_input("Please enter the price of the '%s': " % dish)
    menu[dish]=price
    new=raw_input("Would you like to add another dish? (yes/no) ")
    if new.lower==no:
        break
    print "Menu %s " %menu
    with open("menu.txt", "w+") as menu_file:
        for dish in menu:
            menu_file.write("%s,%s EUR\n" %(dish, menu[dish]))
    print "Goodbye!"
