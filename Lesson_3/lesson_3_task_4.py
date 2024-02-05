from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

# Нарисовать квадрат
#def draw_rect(t):
#    for x in range(0, 4):
#        t.right(90)
#        t.forward(100)

# Рисует квадраты в цикле
#for x in range(0, 360):
#    draw_rect(my_turtle)
#    my_turtle.right(1)

# рисуем слона

def elep(t):
    t.forward(50)
    t.right(45)
    t.forward(50)
    t.right(45)
    t.forward(100)
    t.right(45)
    t.forward(50)
    t.up()
    t.right(180)
    t.forward(50)
    t.left(45)
    t.forward(100)
    t.down()
    t.right(135)
    t.left(45)
    t.forward(150)
    t.right(45)
    t.forward(50)
    t.right(20)
    t.forward(100)
    t.up()
    t.left(180)
    t.forward(100)
    t.down()
    t.left(155)
    t.forward(100)
    t.right(45)
    t.forward(50)
    t.left(45)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(150)
    t.left(62.5)
    t.forward(100)
    t.right(27.5)
    t.forward(50)
    t.right(35)
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.goto(0,0)
    t.up()
    t.goto(0,-50)
    t.down()
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.ht()



elep(my_turtle)

# Необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()