from tkinter import *
a=[]
cal=Tk()
cal.geometry("270x150")
cal['bg']='gray'

def one():
    e1.insert(END,1)
def two():
    e1.insert(END,2)
def three():
    e1.insert(END,3)
def four():
    e1.insert(END,4)
def five():
    e1.insert(END,5)
def six():
    e1.insert(END,6)
def seven():
    e1.insert(END,7)
def eight():
    e1.insert(END,8)
def nine():
    e1.insert(END,9)
def zero():
    e1.insert(END,0)

def add():
    e=int(e1.get())
    clr()
    a.append(e)
    a.append("+")
    e1.delete(0,last=END)
def sub():
    e=int(e1.get())
    clr()
    a.append(e)
    a.append("-")
    e1.delete(0,last=END)
def mul():
    e=int(e1.get())
    clr()
    a.append(e)
    a.append("*")
    e1.delete(0,last=END)
def div():
    e=int(e1.get())
    clr()
    a.append(e)
    a.append("/")
    e1.delete(0,last=END)
def clr():
    e1.delete(0,last=END)
    a.clear()


def eq():
    e=int(e1.get())
    a.append(e)
    e1.delete(0,last=END)
    for i in a:
        if a[1]=="+":
            a.pop(1)
            sum=a[0]+a[1]
            e1.delete(0,last=END)
            e1.insert(0,sum)
        elif a[1]=="-":
            a.pop(1)
            sum=a[0]-a[1]
            e1.delete(0,last=END)
            e1.insert(0,sum)
        elif a[1]=="*":
            a.pop(1)
            sum=a[0]*a[1]
            e1.delete(0,last=END)
            e1.insert(0,sum)
        elif a[1]=="/":
            a.pop(1)
            sum=a[0]/a[1]
            e1.delete(0,last=END)
            e1.insert(0,sum)
            

global e1,e2,e3,n



e1 = Entry(cal,width=20,bg="black",fg="white")
e1.grid(columnspan=4,ipadx=75)

one= Button(cal, text="1",height=1,bg="light blue", width=6, command=one ,activeforeground ="white", activebackground="black" )
one.grid(row = 2,column = 0)


two= Button(cal, text="2",command = two ,bg="light blue",height=1, width=6, activeforeground ="white", activebackground="black")
two.grid(row = 2,column = 1)

three= Button(cal, text="3",command = three,bg="light blue", height=1, width=6, activeforeground ="white", activebackground="black")
three.grid(row = 2,column = 2)

four= Button(cal, text="4",command = four,bg="light blue", height=1, width=6, activeforeground ="white", activebackground="black")
four.grid(row = 3,column = 0)

five= Button(cal, text="5",command = five ,bg="light blue", height=1, width=6, activeforeground ="white", activebackground="black")
five.grid(row = 3,column = 1)

six= Button(cal, text="6",command = six,bg="light blue", height=1, width=6, activeforeground ="white", activebackground="black")
six.grid(row = 3,column = 2)

seven= Button(cal, text="7",command =seven,bg="light blue", height=1, width=6, activeforeground ="white", activebackground="black")
seven.grid(row = 4,column = 0)

eight= Button(cal, text="8",command = eight,bg="light blue", height=1, width=6, activeforeground ="white", activebackground="black")
eight.grid(row = 4,column = 1)

nine= Button(cal, text="9",command = nine,bg="light blue", height=1, width=6, activeforeground ="white", activebackground="black")
nine.grid(row = 4,column = 2)

clear= Button(cal, text="Clear",command =clr,bg="red", height=1, width=6, activeforeground ="white", activebackground="black")
clear.grid(row = 5,column = 0)

zero= Button(cal, text="0",command = zero,bg="light blue", height=1, width=6, activeforeground ="white", activebackground="black")
zero.grid(row = 5,column = 1)

equal= Button(cal, text="=",command = eq,bg="orange", height=1, width=6, activeforeground ="white", activebackground="black")
equal.grid(row = 5,column = 2)

add= Button(cal, text="+",command = add,bg="blue", height=1, width=6, activeforeground ="white", activebackground="black")
add.grid(row = 2,column = 3)

sub= Button(cal, text="-",command = sub,bg="blue",height=1, width=6, activeforeground ="white", activebackground="black")
sub.grid(row = 3,column = 3)

mul= Button(cal, text="*",command = mul,bg="blue", height=1, width=6, activeforeground ="white", activebackground="black")
mul.grid(row = 4,column = 3)

div= Button(cal, text="/",command = div,bg="blue", height=1, width=6, activeforeground ="white", activebackground="black")
div.grid(row = 5,column = 3)

cal.mainloop()
