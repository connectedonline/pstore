# analog_clock.py
import turtle
import time

def klok():
    wn = turtle.Screen()
    wn.title("Analoge klok")
    wn.bgcolor("white")
    wn.setup(width=600, height=600)

    klok = turtle.Turtle()
    klok.hideturtle()
    klok.speed(0)

    # Tekenen van klokcirkel
    klok.penup()
    klok.goto(0, -250)
    klok.pendown()
    klok.circle(250)

    # Uurmarkeringen
    for i in range(12):
        klok.penup()
        klok.goto(0,0)
        klok.setheading(90 - i*30)
        klok.forward(220)
        klok.pendown()
        klok.forward(20)

    # Wijzers
    uur = turtle.Turtle()
    minuut = turtle.Turtle()
    seconde = turtle.Turtle()
    for wijzer in (uur, minuut, seconde):
        wijzer.shape("arrow")
        wijzer.shapesize(stretch_wid=0.3, stretch_len=10)
        wijzer.speed(0)

    while True:
        t = time.localtime()
        uur.setheading(90 - (t.tm_hour % 12) * 30 - t.tm_min * 0.5)
        minuut.setheading(90 - t.tm_min * 6)
        seconde.setheading(90 - t.tm_sec * 6)
        wn.update()

if __name__ == "__main__":
    klok()
