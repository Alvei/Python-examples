import turtle


def createFilledSquare(start_X, start_Y, height):
    turtle.penup()
    turtle.goto(start_X, start_Y)

    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(start_X + height, start_Y)
    turtle.goto(start_X + height, start_Y + height)
    turtle.goto(start_X, start_Y + height)
    turtle.goto(start_X, start_Y)
    turtle.end_fill()
    turtle.penup()


def main():

    turtle.reset()

    start = 'yes'
    while (start == 'yes' or start == 'y'):
        turtle.speed(2)
        # color = input('pick color (blue, red)')
        color = "blue"
        turtle.color(color)
        turtle.penup()

        # height = int(input("length of square: "))
        # start_X = int(input("X coord of square: "))
        # start_Y = int(input("Y coord of square: "))

        height = 200
        start_X = -100
        start_Y = -100

        createFilledSquare(start_X, start_Y, height)
        color = "red"
        turtle.color(color)
        moveRight = 50
        start_X += moveRight

        # turtle.reset()

        createFilledSquare(start_X, start_Y, height)

        createFilledSquare(start_X / 2, start_Y / 2, height / 2)
        start = input("do you want to continue (y/n)")


main()
