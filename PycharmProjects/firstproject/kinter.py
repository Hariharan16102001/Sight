from tkinter import*
import tkinter.messagebox

# def function1():
#     print("clicked")
#
# root = Tk()
#
# mymenu = Menu(root)
# root.config(menu = mymenu)
#
# submenu = Menu(mymenu)
#
# mymenu.add_cascade(label="file",menu=submenu)
#
# submenu.add_command(label="project",command= function1)
# submenu.add_command(label="save",command= function1)
#
# submenu.add_separator()
# submenu.add_command(label="exit",command= function1)
#
# newmenu = Menu(mymenu)
# mymenu.add_cascade(label="Edit",menu=newmenu)
# mymenu.add_command(label = "undo",command=function1)
#
# toolbar = Frame(root,bg="black")
# insertbutton = Button(toolbar,text="Insert Files",command=function1)
# insertbutton.pack(side=LEFT,padx = 2,pady =3)
#
# printbutton = Button(toolbar,text="print",command=function1)
# printbutton.pack(side=LEFT,padx=2,pady = 3)
#
# toolbar.pack(side = TOP,fill = X)
# root,mainloop()

# # message box
# root = Tk()
# tkinter.messagebox.showinfo("Title","This is awesome")
#
# response = tkinter.messagebox.askquestion("question","HI")
#
# if response== 'yes':
#     print("hello")
#
# root.mainloop()

# Tkinter drawing
root = Tk()

canvas = Canvas(root,width=200,height=100)
canvas.pack()

newline = canvas.create_line(0,0,100,100)
otherline = canvas.create_line(10,10,100,100,fill="green")

root.mainloop()