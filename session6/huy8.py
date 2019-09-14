from turtle import *
sides = int(input("Chon so canh: "))
angle = sides / 360

for count in range(sides):
  turtle.fd(50)
  turtle.lt(angle)
mainloop()