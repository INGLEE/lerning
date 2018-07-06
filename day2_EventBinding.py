from tkinter import *
'''
	Label 替换 Button,实现事件绑定
'''
root = Tk()
num = 0
def  add_new_Label(event):
	global root ,num
	
	print (num)
	if  num <=5:
		Label(root,text="我是第 "+str(num)+" 个Label").pack()
		num +=1
	else :
		w1.unbind(add_new_Label)
		

w1 = Label(root,text="Label 替换 Button,实现事件绑定")
w1.pack()
w1.bind('<Button-1>',add_new_Label)

if __name__ == '__main__':
			root.mainloop()


'''
可以在全程序级 别的绑定，使用 bind_all ，它的参数类
型和 bind 一样，它通常用于全局的快捷键，比如 F1 通常
是用来打开帮助文档

还可以绑定某些类别，使用 bind_class, 它接受三个参数，
第一个参数是类名，第二个参数是事件类型，第三个参数
是相应的操作，比如 w.bind_class( “ Entry ” ,
“ <Control-V> ” ,my_paste) 。它就是绑定了所有的所有的
输入框的 Ctrl+V 表示粘贴

*************** 常用的事件 ************
1. 我们在使用 bind 函数的时候，它的第一个参数就是事件
的类型了。
2.<Button-1> 表示鼠标左键单击，其中的 1 换成 3 表示右
键被单击，为 2 的时候表示鼠标中键，感觉不算常用。辛星 2014 年度辛星 tkinter 教程第二版 tkinter
33 / 103
3.<KeyPress-A> 表示 A 键被按下，其中的 A 可以换成其他
的键位。
4.<Control-V> 表示按下的是 Ctrl 和 V键， V可以换成其他
键位。
5.<F1> 表示按下的是 F1 键，对于 Fn 系列的，都可以随便
换。


************* 解除绑定 **************
1. 接触绑定我们使用 unbind 方法，它和 bind 的使用很相
似。
2. 不过 unbind 方法只需要一个参数就可以了，它只需要解
除绑定的事件类型，因为它会解除该绑定事件类型的所有
回调函数。

'''