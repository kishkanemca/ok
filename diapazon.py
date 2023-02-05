import tkinter
import random
from tkinter import PhotoImage


def prepare_and_start():
    global player

    canvas.delete('all')
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    player = canvas.create_image(
    (player_pos[0], player_pos[1]), image=player_pic,anchor='nw')
    label.config(text='найди выход!')
    master.bind('<KeyPress>', key_pressed)


def move_wrap(obj, move_x, move_y):
    xy = canvas.coords(obj)
    canvas.move(obj, move_x, move_y)
    print(xy)
    if xy[0] <= 0:
        canvas.move(obj, WIDTH, 0)
    if xy[0] >= WIDTH:
        canvas.move(obj, -WIDTH, 0)
    if xy[1] <= 0:
        canvas.move(obj, HEIGHT, 0)
    if xy[1] >= HEIGHT:
        canvas.move(obj, HEIGHT, 0)


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, 0, -step)
    if event.keysym == 'Down':
        move_wrap(player, 0, step)
    if event.keysym == 'Right':
        move_wrap(player, step, 0)
    if event.keysym == 'Left':
        move_wrap(player, -step, 0)


master = tkinter.Tk()

step = 50
N_X = 10
N_Y = 10
WIDTH = step * N_X
HEIGHT = step * N_Y

player_pic = tkinter.PhotoImage(file=r'pixil-frame-0.png')

canvas = tkinter.Canvas(master,bg='#0cf032',
                        width=WIDTH, height=HEIGHT)

player_pos = (random.randint(0,N_X - 1) * step,
              random.randint(0, N_Y - 1) * step)

print(player_pos)
label = tkinter.Label(master,  text='не попадись!')
restart = tkinter.Button(master, text='Начать заново',
                         command=prepare_and_start)

restart.pack()
label.pack()
canvas.pack()
prepare_and_start()
master.bind('<KeyPress>', key_pressed)
master.mainloop()