from graphics import *
win=GraphWin('Design A House',500,500)
win.setCoords(0,0,100,100)

text1=Text(Point(50,10),"Click on lower left corner of the frame").draw(win)
text1.setTextColor('black')
p1 = win.getMouse()
p1.draw(win)
text1.undraw()

text2=Text(Point(50,10),"Click on upper right corner of the frame").draw(win)
text2.setTextColor('black')
p2 = win.getMouse()
text2.undraw()
p1.undraw()

frame = Rectangle(p1, p2)
frame.draw(win)

houseBottomY = min(p1.getY(), p2.getY())
houseTopY = max(p1.getY(), p2.getY())
houseLeftX = min(p1.getX(), p2.getX())
houseRighX = max(p1.getX(), p2.getX())

text3=Text(Point(50,10),"Click on the center of the top of the door").draw(win)
text3.setTextColor('black')
p3 = win.getMouse()
text3.undraw()

doorW = abs(p1.getX() - p2.getX()) * 0.2
doorH = abs(p3.getY() - houseBottomY)
doorP1 = Point(p3.getX() - doorW * 0.5, houseBottomY)
doorP2 = Point(p3.getX() + doorW * 0.5, p3.getY())

door = Rectangle(doorP1, doorP2)
door.draw(win)
door.setFill('red')

text3=Text(Point(50,10),"Click on the center of the window").draw(win)
text3.setTextColor('black')
p4 = win.getMouse()
text3.undraw()

windowH = doorW * 0.5
windowP1 = Point(p4.getX() - windowH * 0.5, p4.getY() - windowH * 0.5)
windowP2 = Point(p4.getX() + windowH * 0.5, p4.getY() + windowH * 0.5)

window = Rectangle(windowP1, windowP2)
window.draw(win)

text4=Text(Point(50,10),"Click on the peak of the roof").draw(win)
text4.setTextColor('black')
p5 = win.getMouse()
text4.undraw()

roofP1 = Point(houseLeftX, houseTopY)
roofP2 = Point(houseRighX, houseTopY)
roofP3 = p5

roof = Polygon(roofP1, roofP2, roofP3)
roof.draw(win)
roof.setFill('black')

text5=Text(Point(50,10),"Click anywhere to quit").draw(win)
text5.setTextColor('black')
win.getMouse()
win.close()
