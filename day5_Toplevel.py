'''
*************Toplevel*************
1. 一个 toplevel 可以理解为一个新的窗口，它是一个顶层
窗口。
2. 新建一个 toplevel 很简单，只需要实例化该类即可，这
也是创建多窗口 应用的一个途径。
'''

from tkinter import *
# 增加了这行代码，引入了ttf，button的样式变了
from tkinter.ttk import *

root = Tk()
root.title("我是root窗口")
btn1 = Button(root,text ="我是root窗口按钮").pack()

f = Toplevel(root,width =30,height =20)
f.title("我是Toplevel窗口")
btn2 = Button(f,text ="我是Toplevel窗口按钮").pack()

root.mainloop()


'''
ttk :因为 tkinter是一个跨平台的界面库，但是，这也就意味着它丧失了平
台优势。为了让它在 Windows 平台下运行更像 Windows，其
实是让它支持不同的风格，于是出现了这么一个文件，用
于弥补 tkinter 的不足
''' 
