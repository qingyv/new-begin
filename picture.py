import turtle as tl
import time
tl.pensize(3)
colors=("red","green","yellow","blue")
tl.bgcolor('black')
tl.tracer(False)
for i in range(400):
    tl.fd(i*2)
    tl.left(91)
    tl.color(colors[i%4])
tl.tracer(True)
time.sleep(4)




