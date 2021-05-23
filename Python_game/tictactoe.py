from tkinter import *
import tkinter.messagebox

root=Tk()

# tkinter.messagebox.showinfo(title='RESULT',message='WON')
change=True
count=0
def game(b):
     global count,change
     if b["text"]=='' and change==True:
          b["text"] = 'X'
          change = False
          count += 1
     elif b["text"]=='' and change==False:
          b["text"]='O'
          change= True
          count +=1
     else:
          tkinter.messagebox.showwarning(title='error',message="can't modify")




def disableallbuttons():
     b1.config(state=DISABLED)
     b2.config(state=DISABLED)
     b3.config(state=DISABLED)
     b4.config(state=DISABLED)
     b5.config(state=DISABLED)
     b6.config(state=DISABLED)
     b7.config(state=DISABLED)
     b8.config(state=DISABLED)
     b9.config(state=DISABLED)

win=False
def winner():
     global win
     if b1["text"]=='X' and b2["text"]=='X' and b3["text"]=='X':
          win= True
          b1.config(bg='orange')
          b2.config(bg='orange')
          b3.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='X Won')
     elif b4["text"]=='X' and b5["text"]=='X' and b6["text"]=='X':
          win = True
          b4.config(bg='orange')
          b5.config(bg='orange')
          b6.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='X Won')
          
     elif b7["text"]=='X' and b8["text"]=='X' and b9["text"]=='X':
          win = True
          b7.config(bg='orange')
          b8.config(bg='orange')
          b9.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='X Won')
          

     
     elif b1["text"]=='X' and b4["text"]=='X' and b7["text"]=='X':
          win = True
          b1.config(bg='orange')
          b4.config(bg='orange')
          b7.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='X Won')  
     elif b2["text"]=='X' and b5["text"]=='X' and b8["text"]=='X':
          win = True
          b2.config(bg='orange')
          b5.config(bg='orange')
          b8.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='X Won')
     elif b3["text"]=='X' and b6["text"]=='X' and b9["text"]=='X':
          win = True
          b3.config(bg='orange')
          b6.config(bg='orange')
          b9.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='X Won')


     elif b1["text"]=='X' and b5["text"]=='X' and b9["text"]=='X':
          win = True
          b1.config(bg='orange')
          b5.config(bg='orange')
          b9.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='X Won')
     elif b3["text"]=='X' and b5["text"]=='X' and b7["text"]=='X':
          win = True
          b3.config(bg='orange')
          b5.config(bg='orange')
          b7.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='X Won')




     if b1["text"]=='O' and b2["text"]=='O' and b3["text"]=='O':
          win= True
          b1.config(bg='orange')
          b2.config(bg='orange')
          b3.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='O Won')
     elif b4["text"]=='O' and b5["text"]=='O' and b6["text"]=='O':
          win = True
          b4.config(bg='orange')
          b5.config(bg='orange')
          b6.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='O Won')
     elif b7["text"]=='O' and b8["text"]=='O' and b9["text"]=='O':
          win = True
          b7.config(bg='orange')
          b8.config(bg='orange')
          b9.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='O Won')
          

     
     elif b1["text"]=='O' and b4["text"]=='O' and b7["text"]=='O':
          win = True
          b1.config(bg='orange')
          b4.config(bg='orange')
          b7.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='O Won')
     elif b2["text"]=='O' and b5["text"]=='O' and b8["text"]=='O':
          win = True
          b2.config(bg='orange')
          b5.config(bg='orange')
          b8.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='O Won')
     elif b3["text"]=='O' and b6["text"]=='O' and b9["text"]=='O':
          win = True
          b3.config(bg='orange')
          b6.config(bg='orange')
          b9.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='X Won')


     elif b1["text"]=='O' and b5["text"]=='O' and b9["text"]=='O':
          win = True
          b1.config(bg='orange')
          b5.config(bg='orange')
          b9.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='O Won')
     elif b3["text"]=='O' and b5["text"]=='O' and b7["text"]=='O':
          win = True
          b3.config(bg='orange')
          b5.config(bg='orange')
          b7.config(bg='orange')
          disableallbuttons()
          tkinter.messagebox.showinfo(title='Winner',message='O Won')




def reset():
     global b1,b2,b3,b4,b5,b6,b7,b8,b9
     win=True
     b1=Button(root,text='',height=10,width=20,bg='SystemButtonFace',font=('helvectia',9),command= lambda : [game(b1),winner()])
     b1.grid(row=1,column=0)
     b2=Button(root,text='',height=10,width=20,bg='SystemButtonFace',command= lambda: [game(b2),winner()])
     b2.grid(row=1,column=1)
     b3=Button(root,text='' ,height=10,width=20,bg='SystemButtonFace',command= lambda: [game(b3),winner()])
     b3.grid(row=1,column=2)
     b4=Button(root,text='',height=10,width=20,bg='SystemButtonFace',command= lambda: [game(b4),winner()])
     b4.grid(row=2,column=0)
     b5=Button(root,text='',height=10,width=20,bg='SystemButtonFace',command= lambda: [game(b5),winner()])
     b5.grid(row=2,column=1)
     b6=Button(root,text='',height=10,width=20,bg='SystemButtonFace',command= lambda: [game(b6),winner()])
     b6.grid(row=2,column=2)
     b7=Button(root,text='',height=10,width=20,bg='SystemButtonFace',command= lambda: [game(b7),winner()])
     b7.grid(row=3,column=0)
     b8=Button(root,text='',height=10,width=20,bg='SystemButtonFace',command= lambda: [game(b8),winner()])
     b8.grid(row=3,column=1)
     b9=Button(root,text='',height=10,width=20,bg='SystemButtonFace',command= lambda: [game(b9),winner()])
     b9.grid(row=3,column=2)


reset()

mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
submenu2=Menu(mymenu)
mymenu.add_cascade(label='Format',menu=submenu)
mymenu.add_cascade(label='Logout',menu=submenu2)
submenu.add_command(label='Reset',command=reset)
submenu2.add_command(label="Exit",command=quit)

root.mainloop()


