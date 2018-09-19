#https://www.geeksforgeeks.org/turtle-programming-python/
import turtle  #Inside_Out
w = turtle.Screen()
w.bgcolor("#00ff00")
t = turtle.Turtle()
t.color("#0000ff")

def sqrfunc(size):
    for i in range(4):
        t.fd(size)
        t.left(90)
        size = size + 5

sqrfunc(5)
sqrfunc(10)
sqrfunc(15)
sqrfunc(20)
sqrfunc(25)
sqrfunc(30)
sqrfunc(35)
sqrfunc(40)
holdit = input();
