'''
在新建一个对话框的时候， title 属性， text
属性， bitmap 属性等等都是不可缺少的，否则会报错，我
第一次写的时候就报错了，后来看了下源代码，发现这些
都必须自己填写，因为没有设置默认值
'''
from tkinter import *
from tkinter.dialog import *



def confirm():
	# None这里表示没有父窗口，新建   default 设置默认选择的元素ID
	d = Dialog(None, title ="Dialog",text ="confirm?",bitmap =DIALOG_ICON,default = 0,strings=("YES","NO"))
	# d.num 返回用户点击的元素ID
	print(d.num)


b1 = Button(None,text ="确定",command = confirm)
b1.pack()
b2 = Button(None,text ="取消",command =b1.quit).pack()
b1.mainloop()