from graphics import *

win = GraphWin("Board", 800, 650)
pixel = 800 // 16

entry = Entry(Point(400, 250), 20)
entry.draw(win)
entry_label = Text(Point(200, 250), "Enter Any Letter : ")
entry_label.draw(win)

win.getMouse()

user_letter = entry.getText().upper()
user_letter = user_letter[0]

entry.undraw()
entry_label.undraw()












def A():
    if row ==3 and 6 <=col<= 10:
        square.setFill("white")
    elif row ==6 and 6 <=col<= 10:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 6:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 10:
        square.setFill("white")


def B():
    if row ==3 and 6 <=col<= 9:
        square.setFill("white")
    elif row ==6 and 6 <=col<= 9:
        square.setFill("white")
    elif row ==9 and 6 <=col<= 9:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 6:
        square.setFill("white")
    elif 4 <=row<= 5 and col == 10:
        square.setFill("white")
    elif 7 <=row<= 8 and col == 10:
        square.setFill("white")


def C():
    if row ==3 and 6 <=col<= 10:
        square.setFill("white")
    elif row ==9 and 6 <=col<= 10:
        square.setFill("white")
    elif 4 <=row<= 8 and col == 5:
        square.setFill("white")


def D():
    if row ==3 and 6 <=col<= 10:
        square.setFill("white")
    elif row ==9 and 6 <=col<= 10:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 6:
        square.setFill("white")
    elif 4 <=row<= 8 and col == 11:
        square.setFill("white")



def E():
    if row ==3 and 6 <=col<= 9:
        square.setFill("white")
    elif row ==6 and 6 <=col<= 9:
        square.setFill("white")
    elif row ==9 and 6 <=col<= 9:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 6:
        square.setFill("white")


def F():
    if row ==3 and 6 <=col<= 9:
        square.setFill("white")
    elif row ==6 and 6 <=col<= 8:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 6:
        square.setFill("white")


def G():
    if row ==3 and 7 <=col<= 10:
        square.setFill("white")
    if row ==6 and 9 <=col<= 10:
        square.setFill("white")
    elif row ==8 and 7 <=col<= 9:
        square.setFill("white")
    elif 4 <=row<= 7 and col == 6:
        square.setFill("white")
    elif 6 <=row<= 8 and col == 10:
        square.setFill("white")


def H():
    if row ==6 and 6 <=col<= 10:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 6:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 10:
        square.setFill("white")


def I():
    if 3 <=row<= 9 and col == 8:
        square.setFill("white")


def J():
    if row ==9 and 6 <=col<= 8:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 8:
        square.setFill("white")
    elif 8 <=row<= 8 and col == 6:
        square.setFill("white")

def K():
    if 3 <=row<= 9 and col == 6:
        square.setFill("white")
    elif row == 6 and col == 7:
        square.setFill("white")
    elif row == 5 and col == 8:
        square.setFill("white")
    elif row == 7 and col == 8:
        square.setFill("white")
    elif 3 <=row<= 4 and col == 9:
        square.setFill("white")
    elif 8 <=row<= 9 and col == 9:
        square.setFill("white")


def L():

    if row ==9 and 6 <=col<= 9:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 6:
        square.setFill("white")


def M():

    if 3 <=row<= 9 and col == 5:
        square.setFill("white")
    elif 3 <=row<= 8 and col == 8:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 11:
        square.setFill("white")
    elif row ==3 and 6 <=col<= 10:
        square.setFill("white")


def N():

    if 3 <=row<= 9 and col == 5:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 11:
        square.setFill("white")
    elif row == 4 and col == 6:
        square.setFill("white")
    elif row == 5 and col == 7:
        square.setFill("white")
    elif row == 6 and col == 8:
        square.setFill("white")
    elif row == 7 and col == 9:
        square.setFill("white")
    elif row == 8 and col == 10:
        square.setFill("white")



def O():
    if row ==3 and 6 <=col<= 10:
        square.setFill("white")
    elif row ==8 and 6 <=col<= 10:
        square.setFill("white")
    elif 3 <=row<= 8 and col == 6:
        square.setFill("white")
    elif 3 <=row<= 8 and col == 11:
        square.setFill("white")


def P():
    if row ==3 and 6 <=col<= 10:
        square.setFill("white")
    elif row ==7 and 6 <=col<= 10:
        square.setFill("white")
    elif 3 <=row<= 11 and col == 6:
        square.setFill("white")
    elif 4 <=row<= 6 and col == 11:
        square.setFill("white")


def Q():
    if row ==3 and 6 <=col<= 10:
        square.setFill("white")
    elif row ==8 and 6 <=col<= 9:
        square.setFill("white")
    elif 3 <=row<= 8 and col == 6:
        square.setFill("white")
    elif 3 <=row<= 6 and col == 11:
        square.setFill("white")
    elif row == 6 and col == 9:
        square.setFill("white")
    elif row == 7 and col == 10:
        square.setFill("white")
    elif row == 8 and col == 11:
        square.setFill("white")
    elif row == 9 and col == 12:
        square.setFill("white")


def R():
    if row ==3 and 6 <=col<= 10:
        square.setFill("white")
    elif row ==7 and 6 <=col<= 10:
        square.setFill("white")
    elif 3 <=row<= 11 and col == 6:
        square.setFill("white")
    elif 4 <=row<= 6 and col == 11:
        square.setFill("white")
    elif row == 8 and col == 7:
        square.setFill("white")
    elif row == 9 and col == 8:
        square.setFill("white")
    elif row == 10 and col == 9:
        square.setFill("white")
    elif row == 11 and col == 10:
        square.setFill("white")



def S():
    if row ==3 and 6 <=col<= 9:
        square.setFill("white")
    elif row ==6 and 6 <=col<= 9:
        square.setFill("white")
    elif row ==9 and 6 <=col<= 9:
        square.setFill("white")
    elif 3 <=row <=6 and col == 6:
        square.setFill("white")
    elif 6 <=row <=9 and col == 9:
        square.setFill("white")


def T():
    if row ==3 and 6 <=col<= 10:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 8:
        square.setFill("white") 


def U():
    if 3 <=row<= 9 and col == 5:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 10:
        square.setFill("white") 
    elif row == 10 and 6 <=col<= 9:
        square.setFill("white") 


def V():
    if 3 <=row<= 9 and col == 5:
        square.setFill("white")
    elif 3 <=row<= 9 and col == 9:
        square.setFill("white") 
    elif row == 10 and 6 <=col<= 8:
        square.setFill("white") 
    elif row == 11 and col == 7:
        square.setFill("white") 


def W():
    if 3 <=row<= 9 and col == 5:
        square.setFill("white")
    elif 4 <=row<= 9 and col == 9:
        square.setFill("white") 
    elif row == 10 and 6 <=col<= 8:
        square.setFill("white") 

    elif 3 <=row<= 9 and col == 13:
        square.setFill("white") 
    elif row == 10 and 10 <=col<= 12:
        square.setFill("white") 


def X():
    if row == 5 and col == 6:
        square.setFill("white")
    elif row == 7 and col == 6:
        square.setFill("white")
    elif row == 7 and col == 8:
        square.setFill("white")
    elif 3 <=row<= 4 and col == 5:
        square.setFill("white")
    elif 8 <=row<= 9 and col == 5:
        square.setFill("white")
    elif row == 6 and col == 7:
        square.setFill("white")
    elif row == 5 and col == 8:
        square.setFill("white")
    elif 3 <=row<= 4 and col == 9:
        square.setFill("white")
    elif 8 <=row<= 9 and col == 9:
        square.setFill("white")


def Y():
    if 3 <=row<= 6 and col == 5:
        square.setFill("white")
    elif 3 <=row<= 6 and col == 9:
        square.setFill("white") 
    elif row == 7 and 6 <=col<= 8:
        square.setFill("white") 
    elif 8 <=row<= 11 and col == 7:
        square.setFill("white") 

def Z():
    if row ==3 and 6 <=col<= 9:
        square.setFill("white")
    elif row ==6 and 6 <=col<= 9:
        square.setFill("white")
    elif row ==9 and 6 <=col<= 9:
        square.setFill("white")
    elif 3 <=row <=6 and col == 9:
        square.setFill("white")
    elif 6 <=row <=9 and col == 6:
        square.setFill("white")


















for row in range(16):
    for col in range(16):
        x1 = col * pixel
        y1 = row * pixel
        x2 = x1  + pixel
        y2 = y1  + pixel

        square = Rectangle(Point(x1, y1), Point(x2, y2))
        square.setFill("black")

        if user_letter   == "A":
            A()
        elif user_letter == "B":
            B()
        elif user_letter == "C":
            C()
        elif user_letter == "D":
            D()
        elif user_letter == "E":
            E()
        elif user_letter == "F":
            F()
        elif user_letter == "G":
            G()
        elif user_letter == "H":
            H()
        elif user_letter == "I":
            I()
        elif user_letter == "J":
            J()
        elif user_letter == "K":
            K()
        elif user_letter == "L":
            L()
        elif user_letter == "M":
            M()
        elif user_letter == "N":
            N()
        elif user_letter == "O":
            O()
        elif user_letter == "P":
            P()
        elif user_letter == "Q":
            Q()
        elif user_letter == "R":
            R()
        elif user_letter == "S":
            S()
        elif user_letter == "T":
            T()
        elif user_letter == "U":
            U()
        elif user_letter == "V":
            V()
        elif user_letter == "W":
            W()
        elif user_letter == "X":
            X()
        elif user_letter == "Y":
            Y()
        elif user_letter == "Z":
            Z()

        square.draw(win)

win.getMouse()
win.close()