from datetime import date

#function to show menu
def showoptions():
    print("------")
    print("Welcome to Booster calculator tool!\n------\nMenu:\n------")
    print("1. Check your booster deadline")
    print("2. Quit")

#function to calculate deadline
def showdeadline():
    print("------")
    print("Please get your booster jab by " + deadline)
    print("------")

showoptions()
print("------")
option = input("Please select option:")
print("------")

#loop the menu unless user quit
while option != "2":
    # option 1 check deadline
    if option == "1":
        #start tool
        dose1date = input("When did you take your first dose? (d/m/y)")
        dose2date = input("When did you take your second dose? (d/m/y)")
        boosterdate = input("When did you take your booster jab? (d/m/y)")
        infection = input("Have you been tested positive for COVID-19 before? (yes/no)").lower()
        deadline  = 10 + 270 #need to convert dose1date from string to datetime
        print("------")

        if dose1date is None:
            print("Error: please enter date of your first dose.")
            print("------")

        elif dose2date is None:
            print("Error: please enter date of your second dose.")
            print("------")

        elif infection is None:
            print("Error: please enter if you were tested positive before.")
            print("------")

        # elif boosterdate is not None:
        #     print("Congrats! You have already received your booster jab.")
        #     print("------")

        elif infection == "yes":
            print("There is currently no recommendation for you to get the booster jab. Please check the latest MOH regulations.")
            print("------")

        else:
            print("Please get your booster jab by ") #show deadline
            print("------")
            # showdeadline()

    # show error if user didn't input an option
    else:
        print("Error: please select an option.")
        print("------")

    showoptions()
    option = input("Please select option:")
    print("------")