import time
from tkinter import *
from PIL import ImageTk, Image
import turtle

root = Tk()

root.title('Turtle with Aastha')


def my_Button1():
    turtle.bgcolor("black")
    turtle.pensize(2)
    turtle.speed("fastest")
    for i in range(40):
        for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(7)

    time.sleep(5)
    turtle.done()


def my_Button2():
    t = turtle.Turtle()

    t.speed("fastest")
    turtle.bgcolor('black')

    for i in range(120):
        for colors in ["red", "cyan"]:
            t.color(colors)
            t.circle(i + 1)
            t.left(5)
    time.sleep(5)
    turtle.done()


def my_Button3():
    n = 50
    pen = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("purple")
    pen.width(3)
    pen.speed("fastest")
    for i in range(n):
        for colors in ["yellow", "orange", "pink"]:
            pen.color(colors)
            pen.forward(i * 10)
            pen.right(144)
    turtle.done()


def my_Button4():
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.pencolor("yellow")
    for i in range(155):
        turtle.rt(i)
        turtle.circle(125, i)
        turtle.fd(i)
        turtle.rt(90)
    turtle.done()


def my_Button5():
    turtle.bgcolor("black")
    turtle.right(90)
    turtle.forward(150)
    turtle.speed("fastest")

    for i in range(200):
        turtle.pencolor("red")
        turtle.left(200)
        turtle.circle(200 - i, 80)
        turtle.hideturtle()
    turtle.done()

def my_Button6():
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor('black')
    t.pensize(2)
    t.color('green')
    t.left(90)
    t.backward(100)
    t.speed("fastest")

    def tree(i):
        if i < 10:
            return
        else:
            t.forward(i)
            t.color("orange")
            t.circle(2)
            t.color("brown")
            t.left(30)
            tree(3*i/4)
            t.right(60)
            tree(3*i/4)
            t.left(30)
            t.backward(i)
    tree(100)
    turtle.done()


my_Text = Label(text="SELECT THE DESIGN", font=('cursive', 15))
my_Text.grid(row=0, column=1, pady=25)

my_img1 = ImageTk.PhotoImage(Image.open("screen1.png"))
my_Button1img = Button(root, image=my_img1, command=my_Button1)
my_Button1img.grid(row=1, column=0, padx=10)
my_button1text = Button(root, text="Circular Spiral", command=my_Button1)
my_button1text.grid(row=2, column=0, padx=10)

my_img2 = ImageTk.PhotoImage(Image.open("screen2.png"))
my_Button2img = Button(root, image=my_img2, command=my_Button2)
my_Button2img.grid(row=1, column=1, padx=10)
my_button2text = Button(root, text="Shell Spiral", command=my_Button2)
my_button2text.grid(row=2, column=1, padx=10)

my_img3 = ImageTk.PhotoImage(Image.open("screen3.png"))
my_Button3img = Button(root, image=my_img3, command=my_Button3)
my_Button3img.grid(row=1, column=2, padx=10)
my_button3text = Button(root, text="Star Spiral", command=my_Button3)
my_button3text.grid(row=2, column=2, padx=10)

my_img4 = ImageTk.PhotoImage(Image.open("screen4.png"))
my_Button4img = Button(root, image=my_img4, command=my_Button4)
my_Button4img.grid(row=3, column=0, padx=10)
my_button4text = Button(root, text="Star Icon", command=my_Button4)
my_button4text.grid(row=4, column=0, padx=10)

my_img5 = ImageTk.PhotoImage(Image.open("screen5.png"))
my_Button5img = Button(root, image=my_img5, command=my_Button5)
my_Button5img.grid(row=3, column=1, padx=10)
my_button5text = Button(root, text="Star Coiled", command=my_Button5)
my_button5text.grid(row=4, column=1, padx=10)

my_img6 = ImageTk.PhotoImage(Image.open("screen6.png"))
my_Button6img = Button(root, image=my_img6, command=my_Button6)
my_Button6img.grid(row=3, column=2, padx=10)
my_button6text = Button(root, text="Tree Art", command=my_Button6)
my_button6text.grid(row=4, column=2, padx=10)

root.mainloop()
