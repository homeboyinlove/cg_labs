from tkinter import *
from math import *

root = Tk()
button = Button(text='Click')
height = 1920
width = 1080
x, y, x0, y0 = 0, 0, 0, 0


INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000


x_max = 900
y_max = 800
x_min = 200
y_min = 200


# Ð¤ÑƒÐ½ÐºÑ†Ð¸Ñ Ð´Ð»Ñ Ð²Ñ‹Ñ‡Ð¸ÑÐ»ÐµÐ½Ð¸Ñ ÐºÐ¾Ð´Ð° Ñ€ÐµÐ³Ð¸Ð¾Ð½Ð° Ð´Ð»Ñ Ñ‚Ð¾Ñ‡ÐºÐ¸ (x, y)
def computeCode(x, y):
    code = INSIDE
    if x < x_min:  # ÑÐ»ÐµÐ²Ð° Ð¾Ñ‚ Ð¿Ñ€ÑÐ¼Ð¾ÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ°
        code |= LEFT
    elif x > x_max:  # ÑÐ¿Ñ€Ð°Ð²Ð° Ð¾Ñ‚ Ð¿Ñ€ÑÐ¼Ð¾ÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ°
        code |= RIGHT
    if y < y_min:  # Ð¿Ð¾Ð´ Ð¿Ñ€ÑÐ¼Ð¾ÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ¾Ð¼
        code |= BOTTOM
    elif y > y_max:  # Ð½Ð°Ð´ Ð¿Ñ€ÑÐ¼Ð¾ÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ¾Ð¼
        code |= TOP

    return code


# Ð ÐµÐ°Ð»Ð¸Ð·Ð°Ñ†Ð¸Ñ Ð°Ð»Ð³Ð¾Ñ€Ð¸Ñ‚Ð¼Ð° ÐšÐ¾ÑÐ½Ð°-Ð¡Ð°Ð·ÐµÑ€Ð»ÐµÐ½Ð´Ð°
def cohenSutherlandClip(x1, y1, x2, y2, g):
    # Ð’Ñ‹Ñ‡Ð¸ÑÐ»Ð¸Ñ‚ÐµÐ»ÑŒÐ½Ñ‹Ðµ ÐºÐ¾Ð´Ñ‹ Ñ€ÐµÐ³Ð¸Ð¾Ð½Ð¾Ð² Ð´Ð»Ñ P1, P2
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = True

    while True:
        # Ð•ÑÐ»Ð¸ Ð¾Ð±Ðµ ÐºÐ¾Ð½ÐµÑ‡Ð½Ñ‹Ðµ Ñ‚Ð¾Ñ‡ÐºÐ¸ Ð½Ð°Ñ…Ð¾Ð´ÑÑ‚ÑÑ Ð²Ð½ÑƒÑ‚Ñ€Ð¸ Ð¿Ñ€ÑÐ¼Ð¾ÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ°
        if code1 == 0 and code2 == 0:
            break

        # Ð•ÑÐ»Ð¸ Ð¾Ð±Ðµ ÐºÐ¾Ð½ÐµÑ‡Ð½Ñ‹Ðµ Ñ‚Ð¾Ñ‡ÐºÐ¸ Ð½Ð°Ñ…Ð¾Ð´ÑÑ‚ÑÑ Ð·Ð° Ð¿Ñ€ÐµÐ´ÐµÐ»Ð°Ð¼Ð¸ Ð¿Ñ€ÑÐ¼Ð¾ÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ°
        elif (code1 & code2) != 0:
            accept = False
            break

        # ÐÐµÐºÐ¾Ñ‚Ð¾Ñ€Ñ‹Ð°Ñ Ñ‡Ð°ÑÑ‚ÑŒ Ð½Ð°Ñ…Ð¾Ð´Ð¸Ñ‚ÑÑ Ð²Ð½ÑƒÑ‚Ñ€Ð¸ Ð¿Ñ€ÑÐ¼Ð¾ÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ°
        else:
            # Ð›Ð¸Ð½Ð¸Ñ Ð½ÑƒÐ¶Ð´Ð°ÐµÑ‚ÑÑ Ð² Ð¾Ð±Ñ€ÐµÐ·ÐºÐµ
            # Ð¾Ð´Ð½Ð° Ð¸Ð· Ñ‚Ð¾Ñ‡ÐµÐº Ð½Ð°Ñ…Ð¾Ð´Ð¸Ñ‚ÑÑ ÑÐ½Ð°Ñ€ÑƒÐ¶Ð¸,
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # ÐÐ°Ð¹Ñ‚Ð¸ Ñ‚Ð¾Ñ‡ÐºÑƒ Ð¿ÐµÑ€ÐµÑÐµÑ‡ÐµÐ½Ð¸Ñ
            # Ñ Ð¸ÑÐ¿Ð¾Ð»ÑŒÐ·Ð¾Ð²Ð°Ð½Ð¸ÐµÐ¼ Ñ„Ð¾Ñ€Ð¼ÑƒÐ»
            if code_out & TOP:
                # Ñ‚Ð¾Ñ‡ÐºÐ° Ð½Ð°Ð´ Ð¿Ñ€ÑÐ¼Ð¾ÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ¾Ð¼
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max

            elif code_out & BOTTOM:
                # Ñ‚Ð¾Ñ‡ÐºÐ° Ð¿Ð¾Ð´ Ð¿Ñ€ÑÐ¼Ð¾ÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ¾Ð¼
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min

            elif code_out & RIGHT:
                # Ñ‚Ð¾Ñ‡ÐºÐ° ÑÐ¿Ñ€Ð°Ð²Ð° Ð¿Ñ€ÑÐ¼Ð¾ÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ¾Ð¼
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max

            elif code_out & LEFT:
                # Ñ‚Ð¾Ñ‡ÐºÐ° ÑÐ»ÐµÐ²Ð° Ð¿Ñ€ÑÐ¼Ð¾ÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ¾Ð¼
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            # Ð¢ÐµÐ¿ÐµÑ€ÑŒ Ñ‚Ð¾Ñ‡ÐºÐ° Ð¿ÐµÑ€ÐµÑÐµÑ‡ÐµÐ½Ð¸Ñ x, y Ð½Ð°Ð¹Ð´ÐµÐ½Ð°
            # ÐœÑ‹ Ð·Ð°Ð¼ÐµÐ½ÑÐµÐ¼ Ñ‚Ð¾Ñ‡ÐºÑƒ ÑÐ½Ð°Ñ€ÑƒÐ¶Ð¸ Ð¾Ð±Ñ‚Ñ€Ð°Ð²Ð¾Ñ‡Ð½Ð¾Ð³Ð¾ Ð¿Ñ€ÑÐ¼Ð¾ÑƒÐ³Ð¾Ð»ÑŒÐ½Ð¸ÐºÐ°
            # Ð¿Ð¾ Ñ‚Ð¾Ñ‡ÐºÐµ Ð¿ÐµÑ€ÐµÑÐµÑ‡ÐµÐ½Ð¸Ñ
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)
    if accept:
        if g == 0:
            draw_line(int(x1), int(y1), int(x2), int(y2))
        else:
            DrawRectangle(int(x1), int(y1), int(x2), int(y2))


def dclick(event):
    global x, y
    if x == 0:
        img.put('red', (event.x, event.y))
        x = event.x
        y = event.y
    else:
        cohenSutherlandClip(x1=x, y1=y, x2=event.x, y2=event.y, g=0)
        x = event.x
        y = event.y

def click(event):
    global x0, y0
    x0 = event.x
    y0 = event.y


def noclick(event):
    cohenSutherlandClip(x1=x0, y1=y0, x2=event.x, y2=event.y, g=1)

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


def draw_line(x1, y1, x2, y2):
    # Ð¿Ñ€Ð¾ÐµÐºÑ†Ð¸Ñ Ð½Ð° Ð¾ÑÐ¸
    dx = x2 - x1
    dy = y2 - y1
    # Ð¾Ð¿Ñ€ÐµÐ´ÐµÐ»ÑÐµÐ¼ Ð² ÐºÐ°ÐºÑƒÑŽ ÑÑ‚Ð¾Ñ€Ð¾Ð½Ñƒ Ð´Ð²Ð¸Ð³Ð°Ñ‚ÑŒÑÑ
    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
    # ÑÑ€Ð°Ð²Ð½Ð¸Ð²Ð°ÐµÐ¼
    if dx < 0: dx = -dx
    if dy < 0: dy = -dy
    # Ð¾Ð¿Ñ€ÐµÐ´ÐµÐ»ÑÐµÐ¼ Ð½Ð°ÐºÐ»Ð¾Ð½ Ð¾Ñ‚Ñ€ÐµÐ·ÐºÐ°
    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
        # Ð¿Ñ€ÑÐ¼Ð°Ñ Ð²Ñ‹Ñ‚ÑÐ½ÑƒÑ‚Ð° Ð¿Ð¾ Ð¾ÑÐ¸ Ñƒ
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy

    x, y = x1, y1

    error, t = el / 2, 0
    # ÑÑ‚Ð°Ð²Ð¸Ð¼ Ð¿ÐµÑ€Ð²ÑƒÑŽ Ñ‚Ð¾Ñ‡ÐºÑƒ
    img.put('red', (x, y))
    # Ð¸Ð´ÐµÐ¼ Ð¿Ð¾ Ð²ÑÐµÐ¼ Ñ‚Ð¾Ñ‡ÐºÐ°Ð¼
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

root.bind("<Double-Button-1>", dclick)
root.bind("<Button-1>", click)
root.bind("<ButtonRelease-1>", noclick)
# DrawRectangle(x_min, y_min, x_max, y_max)

root.mainloop()
