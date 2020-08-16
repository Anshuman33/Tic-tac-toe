from tkinter import *
import tkinter.messagebox
root=Tk()
root.configure(background="lemon chiffon")
root.geometry('550x500')
root.title('Tic-Tac-Toe')

#Button-Input Holder
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()
var8=StringVar()
var9=StringVar()
scorCirc=StringVar()
scorCross=StringVar()
chanceVar=StringVar()
chanceVar.set('X')
#Player-Choice Making Logic

i=1
def control(var):
    global i,chanceVar
    if i%2!=0:
        var.set('X')
        chanceVar.set('O')
    else:        
        var.set('O')
        chanceVar.set('X')
    i=i+1
    answer=var.get()
    print (answer)

    return i,chanceVar
amul=0
class ScoreBoard:
    def __init__(self):
        self.circ=0
        self.cross=0
score_board=ScoreBoard()
#Winning condition Checking
    

def check(a,b,c):

    
    global amul
        
    if a.get()==b.get() and a.get()==c.get() and a.get()!='':
         
         def  incScore():
            if(a.get()=='O'):
                score_board.circ+=1
            else:
                score_board.cross+=1
         incScore()
         scorCirc.set(score_board.circ)
         scorCross.set(score_board.cross)
         
         tkinter.messagebox.showinfo('Congratulations','You won')
         amul+=1
         reset()
         
    return amul

    
'''Winning condition ends'''

def win(var):
    check(var1,var2,var3)
    check(var4,var5,var6)
    check(var7,var8,var9)
    check(var1,var4,var7)
    check(var2,var5,var8)
    check(var3,var6,var9)
    check(var1,var5,var9)
    check(var7,var5,var3)
    print(var.get())



def draw():
    global amul
    global i
    if i==10 and amul==0:
        print(i)
        print(amul)
        tkinter.messagebox.showinfo('Game Message','Draw! No One Wins')
        reset()          
        
def reset():
    global amul
    global i
    amul=0
    i=1
    var1.set('')
    var2.set('')
    var3.set('')
    var4.set('')
    var5.set('')
    var6.set('')
    var7.set('')
    var8.set('')
    var9.set('')
    chanceVar.set('X')
    button1.config(state=NORMAL)
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)
    button4.config(state=NORMAL)
    button5.config(state=NORMAL)
    button6.config(state=NORMAL)
    button7.config(state=NORMAL)
    button8.config(state=NORMAL)
    button9.config(state=NORMAL)
    return amul,i

#Button-Action
def click1():
    print("Single Click, Button-l")
    button1.config(state=DISABLED)
    control(var1)
    win(var1)
    print(i)
    draw()
    


def click2():
    print("Single Click, Button-2")
    button2.config(state=DISABLED)
    control(var2)
    win(var2)
    print(i)
    draw()

def click3():
    print("Single Click, Button-3")
    button3.config(state=DISABLED)
    control(var3)
    win(var3)
    print(i)
    draw()
    

def click4():
    print("Single Click, Button-4")
    button4.config(state=DISABLED)
    control(var4)
    win(var4)
    print(i)
    draw()

def click5():
    print("Single Click, Button-5")
    button5.config(state=DISABLED)
    control(var5)
    win(var5)
    draw()

def click6():
    print("Single Click, Button-6")
    button6.config(state=DISABLED)
    control(var6)
    win(var6)
    print(i)
    draw()

def click7():
    print("Single Click, Button-7")
    button7.config(state=DISABLED)
    control(var7)
    win(var7)
    print(i)
    draw()

def click8():
    print("Single Click, Button-8")
    button8.config(state=DISABLED)
    control(var8)
    win(var8)
    print(i)
    draw()

def click9():
    print("Single Click, Button-9")
    button9.config(state=DISABLED)
    control(var9)
    win(var9)
    print(i)
    draw()

def createBoard():
    
    global game
    game=Frame(root)
    game.grid(row=1,column=0,pady=5)
createBoard()

def resetgame():
    reset()
    score_board.circ=0
    score_board.cross=0
    scorCirc.set(0)
    scorCross.set(0)
    return score_board
def exitgame():
    root.destroy()


#Graphical Designing
title1=Label(root,text="TIC-TAC-TOE",bg="brown1",font=("Helvetica",18,"bold italic"),width=30,relief=RAISED,bd=2)
title1.grid(row=0,column=0,columnspan=2,pady=2)
button1=Button(game,text='',height=5,width=10,textvariable=var1,bd=2,bg='orange',fg="blue",command=click1)
button1.grid(row=0,column=0)


button2=Button(game,text='',height=5,width=10,textvariable=var2,bd=2,bg='orange',fg="blue",command=click2)
button2.grid(row=0,column=1)

button3=Button(game,text='',height=5,width=10,textvariable=var3,bd=2,bg='orange',fg="blue",command=click3)
button3.grid(row=0,column=2)

button4=Button(game,text='',height=5,width=10,textvariable=var4,bd=2,bg='orange',fg="blue",command=click4)
button4.grid(row=1,column=0)

button5=Button(game,text='',height=5,width=10,textvariable=var5,bd=2,bg='orange',fg="blue",command=click5)
button5.grid(row=1,column=1)

button6=Button(game,text='',height=5,width=10,textvariable=var6,bd=2,bg='orange',fg="blue",command=click6)
button6.grid(row=1,column=2)

button7=Button(game,text='',height=5,width=10,textvariable=var7,bd=2,bg='orange',fg="blue",command=click7)
button7.grid(row=2,column=0)

button8=Button(game,text='',height=5,width=10,textvariable=var8,bd=2,bg='orange',fg="blue",command=click8)
button8.grid(row=2,column=1)

button9=Button(game,text='',height=5,width=10,textvariable=var9,bd=2,bg='orange',fg="blue",command=click9)
button9.grid(row=2,column=2)

scoreBoard=Frame(root,bg="yellow2",bd=3,relief=RAISED)
scoreBoard.grid(row=1,column=1)
Label(scoreBoard,text="Chance Indicator",bg="yellow2",bd=4,font=("Helvetica",12,"bold italic")).grid(row=1,column=1,columnspan=2)
chanceBox=Label(scoreBoard,textvariable=chanceVar,bg="khaki1",bd=4,font=("Helvetica",8,"bold italic"),width=20)
chanceBox.grid(row=2,column=1,columnspan=2)
label1=Label(scoreBoard,text="SCOREBOARD",bg="yellow2",bd=4,font=("Helvetica",12,"bold italic"))
label2=Label(scoreBoard,text='O ==== >',bg="khaki1",width=10,font=("Helvetica",8,"bold italic"))
label3=Label(scoreBoard,text='X ==== >',bg="khaki1",width=10,font=("Helvetica",8,"bold italic"))
label4=Label(scoreBoard,textvariable=scorCirc,bg="khaki1",width=10,font=("Helvetica",8,"bold italic"),justify='left')
label5=Label(scoreBoard,textvariable=scorCross,bg="khaki1",width=10,font=("Helvetica",8,"bold italic"),justify='left')
label1.grid(row=3,column=1,columnspan=2)
label2.grid(row=4,column=1)
label3.grid(row=5,column=1)
label4.grid(row=4,column=2)
label5.grid(row=5,column=2)
resetB=Button(root,text="Reset game",command=resetgame,font=("Helvetica",16,"bold italic"),bg="green yellow")
resetB.grid(row=2,column=0,pady=10)
exitButton=Button(root,text="Exit game",command=exitgame,font=("Helvetica",16,"bold italic"),bg="green yellow")
exitButton.grid(row=2,column=1,pady=10)
root.mainloop()
