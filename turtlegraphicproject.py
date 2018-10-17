#turtlegraphicproject.py jb
from turtle import *
color('blue', 'red')
begin_fill()
while True:
    forward(300)
    left(150)
    if abs(pos()) < 1:
        break
end_fill()
done()
