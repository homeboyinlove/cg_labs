from tkinter import *
from math import *

root = Tk()
button = Button(text='Click')
height = 1920
width = 1080
x = 0
y = 0


def click(event):
    global x, y
    if x == 0:
        img.put('red', (event.x, event.y))
        x = event.x
        y = event.y
    else:
        img.put('red', (event.x, event.y))
        draw_line(x1=x, y1=y, x2=event.x, y2=event.y)
        x = event.x
        y = event.y


def draw_line(x1=0, y1=0, x2=0, y2=0):
    #Ð¿Ñ€Ð¾ÐµÐºÑ†Ð¸Ñ Ð½Ð° Ð¾ÑÐ¸
    dx = x2 - x1
    dy = y2 - y1
    #Ð¾Ð¿Ñ€ÐµÐ´ÐµÐ»ÑÐµÐ¼ Ð² ÐºÐ°ÐºÑƒÑŽ ÑÑ‚Ð¾Ñ€Ð¾Ð½Ñƒ Ð´Ð²Ð¸Ð³Ð°Ñ‚ÑŒÑÑ
    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
    #ÑÑ€Ð°Ð²Ð½Ð¸Ð²Ð°ÐµÐ¼
    if dx < 0: dx = -dx
    if dy < 0: dy = -dy
    #Ð¾Ð¿Ñ€ÐµÐ´ÐµÐ»ÑÐµÐ¼ Ð½Ð°ÐºÐ»Ð¾Ð½ Ð¾Ñ‚Ñ€ÐµÐ·ÐºÐ°
    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
        #Ð¿Ñ€ÑÐ¼Ð°Ñ Ð²Ñ‹Ñ‚ÑÐ½ÑƒÑ‚Ð° Ð¿Ð¾ Ð¾ÑÐ¸ Ñƒ
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy

    x, y = x1, y1

    error, t = el / 2, 0
    #ÑÑ‚Ð°Ð²Ð¸Ð¼ Ð¿ÐµÑ€Ð²ÑƒÑŽ Ñ‚Ð¾Ñ‡ÐºÑƒ
    img.put('red', (x, y))
    #Ð¸Ð´ÐµÐ¼ Ð¿Ð¾ Ð²ÑÐµÐ¼ Ñ‚Ð¾Ñ‡ÐºÐ°Ð¼
    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        img.put('red', (x, y))


root['bg'] = '#fafafa'
root.title('ÐŸÐµÑ€Ð²Ð°Ñ Ð»Ð°Ð±Ð¾Ñ€Ð°Ñ‚Ð¾Ñ€Ð½Ð°Ñ')
root.geometry('1920x1080')

canvas = Canvas(root, height=height, width=width, bg='white', cursor='pencil')
canvas.pack()
img = PhotoImage(height=height, width=width)
canvas.create_image((width / 2, height / 2), image=img, state='normal')

root.bind("<Button-1>", click)

root.mainloop()
