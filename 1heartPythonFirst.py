import turtle

t=turtle.Turtle()

t.begin_fill()
t.fillcolor("red")
t.left(140)
t.fd(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.fd(180)
t.end_fill()
t.up()
t.goto(-200,-60)
t.down()
t.write("Happy Valentine Day Baby!",font=('arial',25,'bold'))
t.hideturtle()

turtle.mainloop()
