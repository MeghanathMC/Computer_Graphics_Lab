import turtle,colorsys


t=turtle.Turtle()

turtle.bgcolor("white")
t.speed(0)


for i in range(360):
    t.color(colorsys.hsv_to_rgb(i/70,1,0.4))
    t.left(1)
    t.forward(1)
    
    for _ in range(2):
        t.left(2)
        t.circle(90)