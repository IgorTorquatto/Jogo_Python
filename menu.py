from tkinter import *
import tkinter as tk
import time

#Constantes:
WIDTH = 480
HEIGHT = 300
xvel = 1
yvel = 1

window = Tk()
window.title("Escape from Earth")

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file='imagens/fundo.png')
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

tk.Button(window, text='Jogar',font=('Arial',14)).place(x=200, y=80)
tk.Button(window, text='Instruções',font=('Arial',14)).place(x=200, y=130)
tk.Button(window, text='Dificuldade',font=('Arial',14)).place(x=200, y=180)

photo_image = PhotoImage(file='imagens/nave.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordenadas = canvas.coords(my_image)
    if(coordenadas[0]>=WIDTH-image_width or coordenadas[0]<0):
        xvel = -xvel
    if (coordenadas[1] >= HEIGHT - image_height or coordenadas[1] < 0):
        yvel = -yvel
    canvas.move(my_image,xvel,yvel)
    window.update()
    time.sleep(0.01)



window.mainloop()