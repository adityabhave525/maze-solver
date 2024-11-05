from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    l = Line(Point(50,50), Point(400, 400))
    win.draw_line(l, "black")
    l2 = Line(Point(100,50), Point(450, 400))
    win.draw_line(l2, "red")
    win.wait_for_close()

main()