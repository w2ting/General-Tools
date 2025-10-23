import random

#function to show menu
def showoptions():
    print("========")
    print("Welcome to the huat huat greetings generator!")
    print("========")
    print("1. Generate a greeting")
    print("2. Quit")

showoptions()
option = input("\nPlease select option: ")

#loop the menu unless user quit
while option != "2":

    # generate greeting
    if option == "1":

            huatgreetings = ['新年快乐', '恭喜发财', '年年有余', '万事如意', '步步高升', '兔年快乐', '兔年大吉', '兔年兴旺', '好运连连', '财源广进', '事业有成','步步高升']
            huat = random.choice(huatgreetings)

            print(huat)

    else:
            print("Error: please select an option. Don't be a naughty bunny.\n")
            print("========")

    showoptions()
    option = input("\nPlease select option: ")
    print("========")