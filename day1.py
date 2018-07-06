'''
	Python learning 
	day1.py
'''
from tkinter import *
########################################################################
'''
event
'''
# def display(event):
# 	global root
# 	w2=Label(root,text="Hello,World！")
# 	w2.pack()


# root =Tk()
# b1=Button(root,text="请点击!")
# b1['width']=20
# b1['height']=4
# # b1['background']='red'
# b1.bind("<Button-1>",display)
# b1.pack()

# root.mainloop()
########################################################################
'''
pack()
'''
# root =Tk()
# Button(root,text='A').pack(side=LEFT,expand=YES,fill=Y)
# Button(root,text='B').pack(side=TOP,expand=NO,fill=BOTH)
# Button(root,text='C').pack(side=RIGHT,expand=YES,fill=NONE,anchor=NE)
# Button(root,text='D').pack(side=LEFT,expand=NO,fill=Y,anchor=NW)
# Button(root,text='E').pack(side=TOP,expand=NO,fill=NONE,anchor=NW)
# Button(root,text='F').pack(side=BOTTOM,expand=NO,fill=NONE,anchor=NW)
# Button(root,text='G').pack(anchor=SE)
# root.mainloop()
########################################################################
'''
grid() password 
'''
root=Tk()
e=StringVar()
u=StringVar()

def cls1(event):
	global e
	e.set("")


def cls2(event):
	global u
	u.set("")


Label(root,text="账号：").grid(row=0,sticky=W)
entry1=Entry(root,textvariable=e,fg='#7f7f7f')
e.set("input your name here")
entry1.bind('<Button-1>',cls1)
# entry1.selection_clear()
entry1.grid(row=0,column=1,sticky=E)



Label(root,text="密码：").grid(row=1,sticky=W)
entry2=Entry(root,textvariable=u,show='*')
entry2.bind('<Button-1>',cls2)
entry2.grid(row=1,column=1,sticky=E)
def callback():
	global u
	print(u.get())

Button(root,text="登录",command=callback).grid(row=2,column=1,sticky=EW)
root.mainloop()


