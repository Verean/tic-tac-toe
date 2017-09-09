def board():
    L1 = (250,100,250,400)
    L1a= (249,100,249,400)
    L1b= (251,100,251,400)
    L2 = (350,100,350,400)
    L2a= (349,100,349,400)
    L2b= (351,100,351,400)
    L3 = (150,200,450,200)
    L3a= (150,199,450,199)
    L3b= (150,201,450,201)
    L4 = (150,300,450,300)
    L4a= (150,299,450,299)
    L4b= (150,301,450,301)
    T1 = ("Tic-Tac-Toe",300,450,25)
    T2 = ("Verean Patel",300,10,8)
    return[L1,L1a,L1b,L2,L2a,L2b,L3,L3a,L3b,L4,L4a,L4b,T1,T2]

def initialState():
    return ['E','E','E','E','E','E','E','E','E']

def successor(S,pt):
    C = pTC(pt)
    p = turn(S)
    p1 = 'X'
    p2 = 'O'
    if C == None:
        return S
    if threeInRow(p1,S) or threeInRow(p2,S):
        S = ['E','E','E','E','E','E','E','E','E']
        return initialState()
    else:
        return insert(p,C,S)

def threeInRow(p,S):
    if p == S[0] and p == S[1] and p == S[2]:
        return True
    if p == S[3] and p == S[4] and p == S[5]:
        return True
    if p == S[6] and p == S[7] and p == S[8]:
        return True
    if p == S[0] and p == S[3] and p == S[6]:
        return True
    if p == S[1] and p == S[4] and p == S[7]:
        return True
    if p == S[2] and p == S[5] and p == S[8]:
        return True
    if p == S[0] and p == S[4] and p == S[8]:
        return True
    if p == S[2] and p == S[4] and p == S[6]:
        return True
    else:
        return False

def insert(p,C,S):
    p = turn(S)   
    if C == (1,1) and S[0] == 'E': 
        S[0] = p
    elif C == (1,2)and S[1] == 'E': 
        S[1] = p
    elif C == (1,3)and S[2] == 'E': 
        S[2] = p
    elif C == (2,1)and S[3] == 'E': 
        S[3] = p
    elif C == (2,2)and S[4] == 'E': 
        S[4] = p
    elif C == (2,3)and S[5] == 'E': 
        S[5] = p
    elif C == (3,1)and S[6] == 'E': 
        S[6] = p
    elif C == (3,2)and S[7] == 'E': 
        S[7] = p
    elif C == (3,3)and S[8] == 'E': 
        S[8] = p
    return S

def pTC(pt):
    (x,y) = pt
    col = xToCol(x)
    row = yToRow(y)
    if row == None or col == None:
        return None
    else:
        return (row,col)

def xToCol(x):
    col = 0
    if 150<x<250:
        col = 1
    elif 250<x<350:
        col = 2
    elif 350<x<450:
        col = 3
    else:
        col = None
    return col

def yToRow(y):
    row = 0
    if 300<y<400:
        row = 1
    elif 200<y<300:
        row = 2
    elif 100<y<200:
        row = 3
    else:
        row = None
    return row

def turn(S):
    p = ''
    a = 0
    for i in S:
        if i=='E':
            a += 1
    if a%2==0:
        p = 'O'
    else:
        p = 'X'
    return p

def full(S):
    a = 0
    for i in S:
        if i=='E':
            a += 1
    if a>0:
        return True
    else:
        return False

def displayImages(S):
    images = []
    p1 = 'X'
    p2 = 'O'
    L = []
    if full(S) != False:
        images.append(("", 150, 375, 15))
    if (p1 == S[0] and p1 == S[1] and p1 == S[2]) or (p2 == S[0] and p2 == S[1] and p2 == S[2]):
        L = [(150,350,450,350)]
    if (p1 == S[3] and p1 == S[4] and p1 == S[5]) or (p2 == S[3] and p2 == S[4] and p2 == S[5]):
        L = [(150,250,450,250)]
    if (p1 == S[6] and p1 == S[7] and p1 == S[8]) or (p2 == S[6] and p2 == S[7] and p2 == S[8]):
        L = [(150,150,450,150)]
    if (p1 == S[0] and p1 == S[3] and p1 == S[6]) or (p2 == S[0] and p2 == S[3] and p2 == S[6]):
        L = [(200,100,200,400)]
    if (p1 == S[1] and p1 == S[4] and p1 == S[7]) or (p2 == S[1] and p2 == S[4] and p2 == S[7]):
        L = [(300,100,300,400)]
    if (p1 == S[2] and p1 == S[5] and p1 == S[8]) or (p2 == S[2] and p2 == S[5] and p2 == S[8]):
        L = [(400,100,400,400)]
    if (p1 == S[0] and p1 == S[4] and p1 == S[8]) or (p2 == S[0] and p2 == S[4] and p2 == S[8]):
        L = [(150,400,450,100)]
    if (p1 == S[2] and p1 == S[4] and p1 == S[6]) or (p2 == S[2] and p2 == S[4] and p2 == S[6]):
        L = [(450,400,150,100)]
    if ((turn(S) == 'X') and (full(S) != False and (threeInRow(p2,S) == False and threeInRow(p1,S) == False))):
        images.append(("X's Turn", 300, 50, 15))
    if ((turn(S) == 'O') and (full(S) != False and (threeInRow(p2,S) == False and threeInRow(p1,S) == False))):
         images.append(("O's Turn", 300, 50, 15))
    if ((full(S) != True) and ((threeInRow(p1,S)== False) and (threeInRow(p2,S)== False))):
        images.append(("It's a draw.", 300, 50, 15))
    if threeInRow(p1,S) == True:
        images.append(("X wins!", 300, 50, 15))
    if threeInRow(p2,S) == True:
        images.append(("O wins!", 300, 50, 15))
    if S[0] == p1:
        images.append((p1, 200, 350, 15))
    if S[1] == p1:
        images.append((p1, 300, 350, 15))
    if S[2] == p1:
        images.append((p1, 400, 350, 15))
    if S[3] == p1:
        images.append((p1, 200, 250, 15))
    if S[4] == p1:
        images.append((p1, 300, 250, 15))
    if S[5] == p1:
        images.append((p1, 400, 250, 15))
    if S[6] == p1:
        images.append((p1, 200, 150, 15))
    if S[7] == p1:
        images.append((p1, 300, 150, 15))
    if S[8] == p1:
        images.append((p1, 400, 150, 15))
    if S[0] == p2:
        images.append((p2, 200, 350, 15))
    if S[1] == p2:
        images.append((p2, 300, 350, 15))
    if S[2] == p2:
        images.append((p2, 400, 350, 15))
    if S[3] == p2:
        images.append((p2, 200, 250, 15))
    if S[4] == p2:
        images.append((p2, 300, 250, 15))
    if S[5] == p2:
        images.append((p2, 400, 250, 15))
    if S[6] == p2:
        images.append((p2, 200, 150, 15))
    if S[7] == p2:
        images.append((p2, 300, 150, 15))
    if S[8] == p2:
        images.append((p2, 400, 150, 15))
    return board() + images + L

######################################################################
######################################################################
# TPGE GAME ENGINE
#
# Student code is linked with this code to create a game.

# displaySize() is the size of the display window, (width, height)

def displaySize() : return (600,500)
from graphics import *

# If x is an image, imageKind(x) is the type of image x is:
# 'circle', 'text', or 'lineSegment'

def imageKind(x):
    if len(x)==3 : return 'circle'
    elif type(x[0])== str :return 'text'
    else : return 'lineSegment'

    
# If x is an image, convert(x) is the corresponding image in the
# graphics.py library. We turn the screen upside down so that the origin
# is in the lower left corner, so it matches what they learn in algebra
# class.

def convert(x):
    if imageKind(x)=='circle': return convertCircle(x)
    elif imageKind(x)=='lineSegment': return convertLine(x)
    elif imageKind(x)=='text' : return convertText(x)


def convertLine(x):
    (W,H) = displaySize()
    P1 = Point(x[0],H - x[1])
    P2 = Point(x[2],H - x[3])
    return Line(P1,P2)

def convertText(x):
    (W,H) = displaySize()
    center = Point(x[1],H-x[2])
    string = x[0]
    size = x[3]
    T = Text(center,string)
    T.setSize(size)
    return T

def convertCircle(x):
    (W,H) = displaySize()
    center = Point(x[0],H-x[1])
    radius = x[2]
    return Circle(center,radius)

# Create a window to play in
display = GraphWin("My game", displaySize()[0], displaySize()[1])


# The main loop
#
# Set the state, draw the display, get a mouse click, set the new state,
# and repeat until the user closes the window.

S = initialState()
images = [convert(x) for x in displayImages(S)]

while(True):
    for x in images: x.draw(display)
    c = display.getMouse()
    click = (c.getX(),displaySize()[1] - c.getY())
    S = successor(S,click)
    for I in images: I.undraw()
    images = [convert(x) for x in displayImages(S)]
  

  

