import turtle, time


#1.
# turtle.shape("turtle")
# time.sleep(5)

#2.
# turtle.shape("turtle")
# turtle.bgcolor("black")
# turtle.color("green")
# turtle.forward(100)
#
# time.sleep(5)

#3.
# turtle.shape("turtle")
# turtle.color("green")
#
#
# def writeA():
#     turtle.left(60)
#     turtle.forward(100)
#     turtle.right(120)
#     turtle.forward(100)
#     turtle.backward(50)
#     turtle.right(120)
#     turtle.penup()
#     turtle.forward(50)
#     turtle.right(180)
#     turtle.pendown()
#     turtle.forward(50)
#     turtle.penup()
#     turtle.right(90)
#     turtle.forward(45)
#
# writeA()
#
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.pendown()
# turtle.forward(90)
# turtle.right(90)
#
# for i in range(17):
#     turtle.right(10)
#     turtle.forward(8)
#     i = i / 2
#
# turtle.left(170)
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()
#
# writeA()
#
# time.sleep(50)


# 4.
def zeichne_quadrat():
    turtle.shape("turtle")
    turtle.color("green")
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

# 5.
for i in range(32):
    zeichne_quadrat()
    turtle.right(11.25)


