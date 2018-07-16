'''
*************Toplevel*************
1. 一个 toplevel 可以理解为一个新的窗口，它是一个顶层
窗口。
2. 新建一个 toplevel 很简单，只需要实例化该类即可，这
也是创建多窗口 应用的一个途径。
'''

from tkinter import *

root = Tk()
btn1 = Button(root,text ="我是root窗口按钮").pack()