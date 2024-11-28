from tkinter import *
from math import *

root = Tk()
button = Button(text='Click')
height = 1920
width = 1080
x0, y0, x1, x2, a, b = 0, 0, 0, 0, 0, 0


def click(event):
    global x0, y0
    x0 = event.x
    y0 = event.y


def noclick(event):
    global a, b, x1, y1
    x1 = event.x
    y1 = event.y
    DrawRectangle(x0, y0, x1, y1)
    a = int(abs(x0 - x1) / 2)
    b = int(abs(y0 - y1) / 2)
    draw_ellipse(abs(x0 - x1), abs(y0 - y1), a, b)


def DrawRectangle(x1, y1, x2, y2):
    X1 = x1
    Y1 = y1
    X2 = x1
    Y2 = y1
    # Ð¿Ñ€Ð¾ÐµÐºÑ†Ð¸Ñ Ð½Ð° Ð¾ÑÐ¸
    dx = x2 - x1
    dy = y2 - y1
    # Ð¾Ð¿Ñ€ÐµÐ´ÐµÐ»ÑÐµÐ¼ Ð² ÐºÐ°ÐºÑƒÑŽ ÑÑ‚Ð¾Ñ€Ð¾Ð½Ñƒ Ð´Ð²Ð¸Ð³Ð°Ñ‚ÑŒÑÑ
    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

    while X1 != x2:
        img.put('black', (X1, Y1))
        X1 += sign_x

    while Y1 != y2:
        img.put('black', (X2, Y1))
        Y1 += sign_y

    while X2 != x2:
        img.put('black', (X2, Y1))
        X2 += sign_x

    while Y2 != y2:
        img.put('black', (X1, Y2))
        Y2 += sign_y


def pix(x, y, _x, _y):
    if x0 < x1 and y0 < y1:  # 4 Ñ‡ÐµÑ‚Ð²ÐµÑ€Ñ‚ÑŒ
        img.put('red', (_x + x0 + a, _y + y0 + b))
        img.put('red', (_x + x0 + a, - _y + y0 + b))
        img.put('red', (- _x + x0 + a, - _y + y0 + b))
        img.put('red', (-_x + x0 + a, _y + y0 + b))
    if x0 < x1 and y0 > y1:  # 1
        img.put('red', (_x + x0 + a, _y + y0 - b))
        img.put('red', (_x + x0 + a, - _y + y0 - b))
        img.put('red', (- _x + x0 + a, - _y + y0 - b))
        img.put('red', (-_x + x0 + a, _y + y0 - b))
    if x0 > x1 and y0 > y1:  # 2
        img.put('red', (_x + x0 - a, _y + y0 - b))
        img.put('red', (_x + x0 - a, - _y + y0 - b))
        img.put('red', (- _x + x0 - a, - _y + y0 - b))
        img.put('red', (-_x + x0 - a, _y + y0 - b))
    if x0 > x1 and y0 < y1:  # 3
        img.put('red', (_x + x0 - a, _y + y0 + b))
        img.put('red', (_x + x0 - a, - _y + y0 + b))
        img.put('red', (- _x + x0 - a, - _y + y0 + b))
        img.put('red', (-_x + x0 - a, _y + y0 + b))


def draw_ellipse(x, y, a, b):
    a_sqr = a * a
    b_sqr = b * b
    _y = b
    _x = 0
    d = 4 * b_sqr * ((_x + 1) * (_x + 1)) + a_sqr * ((2 * _y - 1) * (2 * _y - 1)) - 4 * a_sqr * b_sqr
    while a_sqr * (2 * _y - 1) > 2 * b_sqr * (_x + 1):
        pix(x, y, _x, _y)
        if d < 0:
            _x += 1
            d += 4 * b_sqr * (2 * _x + 3)
        else:
            _x += 1
            d = d - 8 * a_sqr * (_y - 1) + 4 * b_sqr * (2 * _x + 3)
            _y -= 1
    d = b_sqr * ((2 * _x + 1) * (2 * _x + 1)) + 4 * a_sqr * ((_y + 1) * (_y + 1)) - 4 * a_sqr * b_sqr
    while _y + 1 != 0:
        pix(x, y, _x, _y)
        if d < 0:
            _y -= 1
            d += 4 * a_sqr * (2 * _y + 3)
        else:
            _y -= 1
            d = d - 8 * b_sqr * (_x + 1) + 4 * a_sqr * (2 * _y + 3)
            _x += 1


root['bg'] = '#fafafa'
root.title('Ð’Ñ‚Ð¾Ñ€Ð°Ñ Ð»Ð°Ð±Ð¾Ñ€Ð°Ñ‚Ð¾Ñ€Ð½Ð°Ñ')
root.geometry('1920x1080')

canvas = Canvas(root, height=height, width=width, bg='white', cursor='pencil')
canvas.pack()
img = PhotoImage(height=height, width=width)
canvas.create_image((width / 2, height / 2), image=img, state='normal')

root.bind("<Button-1>", click)
root.bind("<ButtonRelease-1>", noclick)

root.mainloop()
