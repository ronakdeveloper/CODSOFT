from tkinter import *

def click(event):
    global calc
    text = event.widget.cget('text')
    print(text)
    if text == '=':
        if calc.get().isdigit():
            value = int(calc.get())
        else:
            value = eval(screen.get())
            
        calc.set(value)
        screen.update()
        
    elif text == 'C':
        calc.set('')
        screen.update()
    else:
        calc.set(calc.get() + text)
        screen.update()

root = Tk()
root.geometry('300x450')
root.title('Simple Calculator')
calc = StringVar()
calc.set('')
screen = Entry(root,textvar=calc,font='lucida 40 bold')
screen.pack()

f=Frame(root,bg='gray')

b1 = Button(f,text='7',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='8',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)


b1 = Button(f,text='9',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='/',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

f.pack()


f=Frame(root,bg='gray')

b1 = Button(f,text='4',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='5',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='6',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='*',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

f.pack()

f=Frame(root,bg='gray')

b1 = Button(f,text='1',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='2',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='3',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='-',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

f.pack()

f=Frame(root,bg='gray')

b1 = Button(f,text='0',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=5,pady=10)

b1 = Button(f,text='C',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='=',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='+',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

f.pack()

root.mainloop()
