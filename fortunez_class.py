from random import randint
class Fortune_Teller:

    

    def __init__(self, color, color_list, random_number):
        self.color = color
        self.color_list = color_list
        self.random_number = random_number
        self.value = value


    def get_color():
        color = input("enter a color: ")
        color_list = ["red", "blue", "black", 'purple', "orange", "green"]
        if color in color_list:
            color_len = len(color)
        return(color_len)

    def get_number():
        number = randint(1,5)
        return(number)

    def give_fortune(number):
        if number == 5:
            print("you gonna be a rich homie, quan! ")
        elif number == 4:
            print("you gonna have the all seeing eye of fetty wapp")
        elif number == 3:
            print("you on how many dating apps ?! ...dass right, ALL OF EM")
        elif number == 2:
            print("Tha TIND is strong in you")
        elif number == 1:
            print("Don't hinge on the girls on hinge being sincere")
    
    
