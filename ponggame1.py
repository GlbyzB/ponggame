import turtle
import random

#create a window.
window = turtle.Screen()
window.title("Pong Game by GB")
window.bgcolor("blue")
window.setup(width=800, height=600)

#creat stick1 and design it.
stick1 = turtle.Turtle()
stick1.shape("triangle")
stick1.color("white")
stick1.speed(10)
stick1.shapesize(stretch_wid=5, stretch_len=3)
stick1.penup()
stick1.goto(330, 0)

#create stick2 and design it.
stick2 = turtle.Turtle()
stick2.shape("triangle")
stick2.color("red")
stick2.speed(10)
stick2.shapesize(stretch_wid=5, stretch_len=3)
stick2.penup()
stick2.left(180)
stick2.goto(-330, 0)

# create a ball and design it.
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
speed_ofball = 2
ball.speed(speed_ofball)
ball.penup()
x_direction = random.randint(-390, 390)
y_direction = random.randint(-290, 290)
ball.goto(x_direction,y_direction)
ball.dx = 2 #directions
ball.dy = -2

#set scores points
score1 = 0
score2 = 0

#create a scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0, 250)
pen.hideturtle()
pen.write('Player1 vs Player2 ', align='center', font=('Courier', 24, 'normal'))

penscore = turtle.Turtle()
penscore.speed(0)
penscore.color('white')
penscore.penup()
penscore.goto(-14.5, 220)
penscore.hideturtle()
penscore.write('0    0', align='center', font=('Courier', 24, 'normal'))


#write movements functions
def stick1_up():
    y = stick1.ycor()
    y += 20
    stick1.sety(y)

def stick1_down():
    y = stick1.ycor()
    y -= 20
    stick1.sety(y)

def stick1_right():
    x = stick1.xcor()
    x += 20
    stick1.setx(x)

def stick1_left():
    x = stick1.xcor()
    x -= 20
    stick1.setx(x)

def stick2_up():
    y = stick2.ycor()
    y += 20
    stick2.sety(y)

def stick2_down():
    y = stick2.ycor()
    y -= 20
    stick2.sety(y)

def stick2_right():
    x = stick2.xcor()
    x += 20
    stick2.setx(x)

def stick2_left():
    x = stick2.xcor()
    x -= 20
    stick2.setx(x)

def exit_game():
    exit_game = turtle.Turtle()
    exit_game.speed(0)
    exit_game.color('white')
    exit_game.penup()
    exit_game.hideturtle()
    exit_game.write('Game is closing', align='center', font=('Courier', 24, 'normal'))
    window.exitonclick()


#listen for the user's inputs and set the keys for each movement.
window.listen()
window.onkeypress(stick2_up, 'w')
window.onkeypress(stick2_down, 's')
window.onkeypress(stick2_right, 'd')
window.onkeypress(stick2_left, 'a')
window.onkeypress(stick1_up, 'Up')
window.onkeypress(stick1_down, 'Down')
window.onkeypress(stick1_right, 'Right')
window.onkeypress(stick1_left, 'Left')
window.onkeypress(exit_game, 'q')

#main loop
while True:
    #update screen and the ball's location
    window.update()
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #get random x and y directions everytime for the ball's location
    x_direction = random.randint(-390, 390)
    y_direction = random.randint(-290, 290)


    # Border check for the goal.
    if ball.xcor() > 390:
        ball.goto(x_direction, y_direction)
        ball.dx *= -1
        ball.dy *= -1
        score1 += 1
        penscore.clear()
        penscore.write('{}   {}'.format(score1, score2), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(x_direction, y_direction)
        ball.dx *= -1
        score2 += 1
        penscore.clear()
        penscore.write('{}   {}'.format(score1, score2), align='center', font=('Courier', 24, 'normal'))

    # Border check for the ball.
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-280)
        ball.dy *= -1

    # Border check for stick1
    if stick1.ycor() > 260:
        stick1.sety(260)
    if stick1.ycor() < -240:
        stick1.sety(-240)

    if stick1.xcor() > 360:
        stick1.setx(360)
    if stick1.xcor() < -360:
        stick1.setx(-360)

    # Border check for stick2
    if stick2.ycor() > 260:
        stick2.sety(260)
    if stick2.ycor() < -240:
        stick2.sety(-240)

    if stick2.xcor() > 360:
        stick2.setx(360)
    if stick2.xcor() < -360:
        stick2.setx(-360)

    # Collision for sticks and ball
    if (stick1.xcor() - 40 < ball.xcor() < stick1.xcor()) and (stick1.ycor() + 40 > ball.ycor() > stick1.ycor() - 40):
        ball.setx(stick1.xcor() - 40)
        ball.dx *= -1

    if (stick2.xcor() < ball.xcor() < stick2.xcor() + 40) and (stick2.ycor() + 40 > ball.ycor() > stick2.ycor() - 40):
        ball.setx(stick2.xcor() + 40)
        ball.dx *= -1

    # Collision for sticks
    if (stick2.xcor() + 40 > stick1.xcor() > stick2.xcor()) and (stick2.ycor() + 40 > stick1.ycor() > stick2.ycor() - 40):
        stick1.setx(stick1.xcor() + 40)

    if (stick1.xcor() + 40 > stick2.xcor() > stick1.xcor() - 40) and (stick1.ycor() + 40 > stick2.ycor() > stick1.ycor() - 40):
        stick2.setx(stick2.xcor() - 40)



