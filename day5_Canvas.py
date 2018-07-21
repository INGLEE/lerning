'''
手绘中国象棋
'''
from tkinter import *
root = Tk()

root.title("中国象棋棋盘手绘")
can =Canvas(root,width =400, height =450)
can.create_line((0,2),(400,2),width=2)
for i in range(10):
	can.create_line((0,i*50),(400,i*50),width=2)

can.create_line((3,0),(3,450),width=2)

for i in range(8):
	can.create_line((i*50,0),(i*50,200),width=2)

for i in range(8):
	can.create_line((i*50,250),(i*50,450),width=2)

can.create_line((397,0),(397,450),width=2)
can.create_line((150,0),(250,100),width=2)
can.create_line((150,100),(250,0),width=2)
can.create_line((150,450),(250,350),width=2)
can.create_line((150,350),(250,450),width=2)

can.create_text(20,220,text="楚河")
can.create_text(380,220,text="汉界")
can.pack()

# 去除窗口边框
root.overrideredirect(True)

# geometry 函数来控制窗口大小，它接受一个字符串类型的参数，‘ width x height + xoffset + yoffset ’
root.geometry("400x450+600+200")
root.mainloop() 
