from random import randint
def fortune_teller():
    print("Please choose a color: red, blue, black, purple, orange or green")
    for turn in range(3):
        color = input("Enter a color: ")
        color_list = ["red", 'blue', 'black', 'purple', 'orange', 'green']
        if color in color_list:
                color_len = len(color)
        number = randint(1,5)
        print(number)
        if number == 5:
            print("nice man bun bro")
        elif number == 4:
            print("so you gonna give up and go full caveman?")
        elif number == 3:
            print("do you even rugby bro ?")
        elif number == 2:
            print('wanna listen to some folk music?')
        elif number == 1:
            print(" how many cans of recycled food did you eat this week? probably at least 5 ")
fortune_teller()        
        
