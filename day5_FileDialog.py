from tkinter import *
from tkinter.filedialog import *
from tkinter.colorchooser import *
from tkinter.ttk import *

'''
文件选择对话框；颜色选择器
'''
def callback_1():
	name =askopenfilename()
	print (name)


def callback_2():
	result =askcolor(color="#2b43ce",title ="Bernd's colorchooser")
	print (result)


Button(text= 'File Open',command =callback_1).pack(fill='x')

Button(text= 'Color Selector',command =callback_2).pack(side=LEFT,padx=10)

mainloop()