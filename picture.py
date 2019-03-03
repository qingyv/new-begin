# import turtle as tl
# import time
# tl.pensize(3)
# colors=("red","green","yellow","blue")
# tl.bgcolor('black')
# tl.tracer(False)
# for i in range(400):
#     tl.fd(i*2)
#     tl.left(91)
#     tl.color(colors[i%4])
# tl.tracer(True)
# time.sleep(4)


#sun flower
import time
import turtle as tl
tl.penup()
tl.goto(-100,0)
tl.pendown()
tl.color('red','yellow')
tl.speed(10)
tl.begin_fill()
for i in range(50):
    tl.fd(200)
    tl.left(170)
tl.end_fill()
time.sleep(5)





