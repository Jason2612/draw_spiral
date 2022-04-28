import turtle

count = int(input("Input a number you want: "))
t = turtle.Turtle()
t.speed(20)


a = 0
while a < count:
    t.forward(4 + a)
    t.right(40)
    a += 1
else: 
    
    turtle.done()