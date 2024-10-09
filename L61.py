#Rylee Taylor, Liz Wyatt


import turtle

riley = turtle.Turtle()
riley.width(5)
riley.speed(0)


def draw_star(color):
    for side in range(5):
        riley.forward(100)
        riley.right(144)
        riley.color(color)

star_color = input("How are you feeling today? \n")
if star_color == ("happy"):
    draw_star("pink")
elif star_color == ("sad"):
    draw_star("blue")
elif star_color == ("scared"):
    draw_star("green")
elif star_color == ("angry"):
    draw_star("red")





