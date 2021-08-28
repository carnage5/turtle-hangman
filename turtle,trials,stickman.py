'''Python 3.8.9 (tags/v3.8.9:a743f81, Apr  2 2021, 11:10:41) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> s=turtle.setscreen()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s=turtle.setscreen()
AttributeError: module 'turtle' has no attribute 'setscreen'
>>> s=turtle.getscreen()
>>> t=turtle.Turtle()
>>> t.circle(90)
>>> t.dot(30)
>>> t.bgcolor("blue")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t.bgcolor("blue")
AttributeError: 'Turtle' object has no attribute 'bgcolor'
>>> turtle.bgcolor("blue")
>>> turtle.title("first")
>>> t.pensize(10)
>>> t.forward(100)
>>> t.pencolor("red")
>>> t.forward(100)
>>> t.clearstamp()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t.clearstamp()
TypeError: clearstamp() missing 1 required positional argument: 'stampid'
>>> t.reset()
>>> t.clear()
>>> turtle.bgcolor("white")
>>> t.circle(60)
>>> t.up()
>>> t.goto(0,120)
>>> t.clearstamp(0)
>>> t.home()
>>> t.down
<bound method TPen.pendown of <turtle.Turtle object at 0x0000027B41F878B0>>
>>> t.down()
>>> t.right(30)
>>> t.forward(100)
>>> t.home()
>>> t.right(120)
>>> t.forward(100)
>>> t.undo()
>>> t.right(150)
>>> t.home()
>>> t.right(150)
>>> t.forward(100)
>>> t.home()
>>> t.right(90)
>>> t.forward(100)
>>> t.right(30)
>>> t.forward(100)
>>> t.backward(100)
>>> t.left(60)
>>> t.forward(100)
>>> t.up()
>>> t.goto(0,120)
>>> t.home()
>>> t.goto(0,120)
>>> t.left(90)
>>> t.forward(25)
>>> t.undo()
>>> t.down()
>>> t.forward(25)
>>> t.left(90)
>>> t.forward(100)
>>> t.forward(50)
>>> t.left(90)
>>> t.forward(300)
>>> t.forward(100)'''
f=open('movie.txt','r')
c=0
print(f.readline().strip())
print(f.readline().strip())

f.close()

