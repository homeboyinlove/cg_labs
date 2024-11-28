from graphics import *
import numpy as np

win1 = GraphWin("Sutherland-Hodgman: Initial Polygon", 500, 500)

left = 0
right = 1
bottom = 2
top = 3
inToIn = 0
inToOut = 1
outToIn = 2
outToOut = 3


def findCase(xmin, xmax, ymin, ymax, boundary, p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2

    if boundary == left:
        if x1 >= xmin and x2 >= xmin:
            return inToIn
        elif x1 >= xmin:
            return inToOut
        elif x2 >= xmin:
            return outToIn
        else:
            return outToOut

    elif boundary == right:
        if x1 <= xmax and x2 <= xmax:
            return inToIn
        elif x1 <= xmax:
            return inToOut
        elif x2 <= xmax:
            return outToIn
        else:
            return outToOut

    elif boundary == bottom:
        if y1 >= ymin and y2 >= ymin:
            return inToIn
        elif y1 >= ymin:
            return inToOut
        elif y2 >= ymin:
            return outToIn
        else:
            return outToOut

    elif boundary == top:
        if y1 <= ymax and y2 <= ymax:
            return inToIn
        elif y1 <= ymax:
            return inToOut
        elif y2 <= ymax:
            return outToIn
        else:
            return outToOut


def findIntersection(xmin, xmax, ymin, ymax, boundary, p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2

    m = 0
    if x1 != x2:
        m = (y2 - y1) / (x2 - x1)

    if boundary == left:
        return (xmin, y1 + m * (xmin - x1))
    elif boundary == right:
        return (xmax, y1 + m * (xmax - x1))
    elif boundary == bottom:
        if x1 == x2:
            return (x1, ymin)
        else:
            return (x1 + (ymin - y1) / m, ymin)
    elif boundary == top:
        if x1 == x2:
            return (x1, ymax)
        else:
            return (x1 + (ymax - y1) / m, ymax)


def clipPolygon(xmin, xmax, ymin, ymax, points):
    for boundary in range(4):
        new_points = []
        for i in range(len(points)):
            p1 = points[i]
            p2 = points[(i + 1) % (len(points))]

            case = findCase(xmin, xmax, ymin, ymax, boundary, p1, p2)

            if case == inToIn:
                new_points.append(p2)
            elif case == inToOut:
                p = findIntersection(xmin, xmax, ymin, ymax, boundary, p1, p2)
                new_points.append(p)
            elif case == outToIn:
                p = findIntersection(xmin, xmax, ymin, ymax, boundary, p1, p2)
                new_points.append(p)
                new_points.append(p2)

        points = new_points

    return points


def main():
    xmin = 150
    xmax = 350
    ymin = 150
    ymax = 350
    how = 0
    # points = ((250, 125), (125, 250), (175, 275), (240, 175))
    points = ((250, 125), (400, 250), (175, 275), (240, 175))

    r1 = Polygon(Point(xmin, ymin), Point(xmin, ymax), Point(xmax, ymax), Point(xmax, ymin))
    r1.setOutline("blue")
    r1.setWidth(5)
    r1.draw(win1)

    for i in range(len(points)):
        (x1, y1) = points[i]
        (x2, y2) = points[(i + 1) % len(points)]
        l = Line(Point(x1, y1), Point(x2, y2))
        l.setWidth(3)
        l.draw(win1)

    new_points = clipPolygon(xmin, xmax, ymin, ymax, points)

    for i in range(len(new_points)):
        (x1, y1) = new_points[i]
        (x2, y2) = new_points[(i + 1) % len(new_points)]
        l = Line(Point(x1, y1), Point(x2, y2))
        l.setOutline("red")
        l.setWidth(3)
        l.draw(win1)
    win1.getMouse()


main()
