from turtle import *
sides = int(input("Chon so canh: "))
angle = 360 / sides

for i in range(sides):
  forward(100)
  left(angle)
mainloop()