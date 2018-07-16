'''
checkbutton 多选按钮
radiobutton 单选按钮
在菜单中，也有类似的概念，即单选菜单和复选菜单。它们分别用 add_radiobutton 和 add_checkbutton 来分别添加。

这两种菜单都是如果一旦被选定，那么前面会有一个√的标记出现， checkbutton 可以多个同时被选定，
但是 radiobutton 却只能被选定一个，即这个被选定了，会自动取消前一个的选定。
menu.add_checkbutton(label,command,..)
menu.add_radiobutton(label,command,..)
'''

from tkinter import *

root =Tk()

menubar =Menu(root)

fmenu = Menu(menubar)
vmenu = Menu(menubar)
pmenu = Menu(menubar)

for item in ['New File','Open File','Close File']:
	fmenu.add_command(label = item)

fmenu.add_separator()

for item in ['Save','Svae as','Save all']:
	fmenu.add_command(label =item)

fmenu.add_separator()
fmenu.add_command(label ='exit')

for item in ['python','php','java']:
	vmenu.add_checkbutton(label = item)

vmenu.add_separator()
for item in ['html5','css']:
	vmenu.add_radiobutton(label =item)

menubar.add_cascade(label ='File',menu = fmenu)
menubar.add_cascade(label = 'Option',menu=vmenu)

root['menu'] = menubar
if __name__ == '__main__':
	root.title('Sublime Text')
	root.geometry('800x600')
	root.mainloop()
