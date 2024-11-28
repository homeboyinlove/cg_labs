from tkinter import *
from math import *

root = Tk()
button = Button(text='Click')
height = 1920
width = 1080
xmin = 150
xmax = 350
ymin = 150
ymax = 350
pointsX = []
pointsY = []
x = 0
y = 0
j = 0

left = 0
right = 1
bottom = 2
top = 3
inToIn = 0
inToOut = 1
outToIn = 2
outToOut = 3


def scal(x0, y0, x1, y1):
    return (x0 * x1) * (y0 * y1)


def pscal(x0, y0, x1, y1):
    return (x0 * y1) - (y0 * x1)


def CyrusBeck(x1, y1, x2, y2, pointsX, pointsY, j):
    xvec = x2 - x1
    yvec = y2 - y1

    tin = 0
    tout = 1
    clockwise = True

    if pscal((pointsX[2] - pointsX[3]), (pointsY[2] - pointsY[3]), (pointsX[4] - pointsX[3]),
             (pointsY[4] - pointsY[3])) < 0:
        clockwise = False

    for i in range(2, j - 1):
        if clockwise:
            nx = pointsY[i + 1] - pointsY[i]
            ny = -(pointsX[i + 1] - pointsX[i])
        else:
            nx = -(pointsY[i + 1] - pointsY[i])
            ny = pointsX[i + 1] - pointsX[i]

        d = scal(xvec, yvec, nx, ny)
        thit = float(scal(nx, ny, pointsX[i] - x1, pointsY[i] - y1) / d)

        if d > 0 and thit > tin:
            tin = thit
        if d < 0 and thit < tout:
            tout = thit

    if clockwise:
        nx = pointsY[2] - pointsY[j - 1]
        ny = -(pointsX[2] - pointsX[j - 1])
    else:
        nx = -(pointsY[2] - pointsY[j - 1])
        ny = pointsX[2] - pointsX[j - 1]

    d = scal(xvec, yvec, nx, ny)
    thit = float(scal(nx, ny, pointsX[i] - x1, pointsY[i] - y1) / d)

    if d > 0 and thit > tin:
        tin = thit
    if d < 0 and thit < tout:
        tout = thit

    if tin > tout:
        return

    if tin < tout:
        x3 = x1 + int(xvec * tin)
        y3 = y1 + int(yvec * tin)
        x4 = x1 + int(xvec * tout)
        y4 = y1 + int(yvec * tout)
        draw_line(x3, y3, x4, y4)


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


def click(event):
    global pointsY, pointsX, g, xmax, xmin, ymax, ymin, j
    img.put('red', (event.x, event.y))
    pointsX.append(event.x)
    pointsY.append(event.y)
    j += 1
    xmin = event.x
    xmax = event.x
    ymin = event.y
    ymax = event.y


def dclick(event):
    global x, y
    if x == 0:
        img.put('red', (event.x, event.y))
        x = event.x
        y = event.y
    else:
        # clipPolygon(xmin, xmax, ymin, ymax,  x, y, event.x, event.y)
        CyrusBeck(x, y, event.x, event.y, pointsX, pointsY, j)
        x = 0
        y = 0


def qcl(event):
    global xmax, xmin, ymax, ymin
    draw_line(x1=pointsX[0], y1=pointsY[0], x2=pointsX[-1], y2=pointsY[-1])
    for i in range(0, len(pointsY) - 1):
        draw_line(x1=pointsX[i], y1=pointsY[i], x2=pointsX[i + 1], y2=pointsY[i + 1])

    for i in range(0, len(pointsX) - 1):
        if pointsX[i] > xmax:
            xmax = pointsX[i]
        if pointsX[i] < xmin:
            xmin = pointsX[i]

    for i in range(0, len(pointsY) - 1):
        if pointsY[i] > ymax:
            ymax = pointsY[i]
        if pointsY[i] < ymin:
            ymin = pointsY[i]


root['bg'] = '#fafafa'
root.title('ÐŸÐµÑ€Ð²Ð°Ñ Ð»Ð°Ð±Ð¾Ñ€Ð°Ñ‚Ð¾Ñ€Ð½Ð°Ñ')
root.geometry('1920x1080')

canvas = Canvas(root, height=height, width=width, bg='white', cursor='pencil')
canvas.pack()
img = PhotoImage(height=height, width=width)
canvas.create_image((width / 2, height / 2), image=img, state='normal')

root.bind("<Double-Button-1>", dclick)
root.bind("<Button-1>", click)
root.bind("q", qcl)

root.mainloop()
