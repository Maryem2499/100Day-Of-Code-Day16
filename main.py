# # import another_module
# # print(another_module.another_var)
# # How can I construct a new object 'timmy' solution 1 :
# import turtle
# timmy = turtle.Turtle()
# # How can I construct a new object 'timmy' solution 2 :
# from turtle import Turtle, Screen
# timmy = Turtle()
# # changer la forme de visage de l'objet "timmy" a l'écran :
# timmy.shape("turtle")
# # changer la couleur du timmy
# timmy.color("coral")
# # avancement du timmy certains pas :
# timmy.forward(250)
# # construct an object "my_screen" et accerder a l'attribut "conveheight"
# my_screen = Screen()
# print(my_screen.canvheight)
# # construct an object "my_screen" et accerder a la methode "exitonclick()"
# my_screen.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon Name",["Pikatchu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
# Change the align of the words of table right, left or center
table.align = "l"
print(table)


