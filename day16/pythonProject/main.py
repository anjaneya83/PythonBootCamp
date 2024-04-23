#from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
# my_screen = Screen()
# print(my_screen.canvheight,my_screen.canvwidth)
# timmy.onclick(timmy.forward(),100)
# timmy.color("brown")
# print(my_screen.canvheight,my_screen.canvwidth)
# timmy.left(50)
# timmy.color("coral")
# print(my_screen.canvheight,my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name",["Pikachu", "charmindar", "squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)

