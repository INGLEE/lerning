from tkinter import *

root = Tk()
time1 =0
time2 =0
e =StringVar()



def btn1():
	global time1,l,e
	if time1%2 == 0:
		time1 +=1
		e.set("2017-12-12被选中")
	else:
		time1 +=1
		e.set("2017-12-12被取消")

def btn2():
	global time2,l,e
	if time2%2 == 0:
		time2 +=1
		e.set("2018-12-12被选中")
	else:
		time2 +=1
		e.set("2018-12-12被取消")

# Checkbutton（复选） 和Radiobutton（单选） 用法类似

b1 = Checkbutton(root,text="2017-12-12",command =btn1)
b1.pack()
b2 = Checkbutton(root,text="2018-12-12",command =btn2)
b2.pack()

l=Label(root,textvariable = e)

l.pack()
root.mainloop()