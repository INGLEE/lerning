'''
************ 弹出菜单 *****************
1. 弹出菜单又叫“上下文菜单”，也叫“右键菜单”，它
通常是鼠标单击右键产生的菜单，因此会有“右键菜单”
的说法。
2. 其实很多界面库里面都是给出了弹出菜单的简单的制作
方法的，但是 tkinter 里面我们却只能使用比较原始的事
件绑定的方式去做。
3. 大体思路就是：我们先新建一个菜单，然后向菜单项中
添加各种功能，最后我们监听鼠标右键消息，如果是鼠标
右键被单击，此时可以根据需要判断下鼠标位置来确定是
哪个弹出菜单被弹出，然后使用 Menu类的 pop 方法来弹出
菜单。
4. 大体思路就是如此，至于具体的细节，让我们到代码实
战中一探究竟。
************ 提前说明 *************
1.Menu 类里面有一个 post 方法，它接收两个参数，即 x 和
y 坐标(event.x_root,event.y_root)，它会在相应的位置弹出菜单。
2. 还记得用 bind 方法来绑定事件吗 ?而且要记得鼠标右键
是用的 <Button-3> 。

'''

from tkinter import *

root =Tk()
menubar = Menu(root)

for item in ['java','php','C++','VB']:
	menubar.add_command(label = item)

def rJocket():
	Label(root,text= 'New Label').pack()

menubar.add_command(label = 'python',command = rJocket)

# 请求弹出菜单
def pop(event):
	menubar.post(event.x_root,event.y_root)


root.bind('<Button-3>',pop)

if __name__ == '__main__':
	root.mainloop()
