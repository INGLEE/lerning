'''
	Python learning 
	day1.py
'''
from tkinter import *
from tkinter.ttk import *
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
grid() password LoginBox()
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
entry1=Entry(root,textvariable=e)
e.set("input your name here")
entry1.bind('<Button-1>',cls1)
# entry1.selection_clear()
entry1.grid(row=0,column=1,sticky=E)



Label(root,text="密码：").grid(row=1,sticky=W)
entry2=Entry(root,textvariable=u,show='*')
entry2.bind('<Button-1>',cls2)
entry2.grid(row=1,column=1,sticky=E)
def callback():
	t1 = entry1.get()
	t2 = entry2.get()
	t3=StringVar()
	if (t1 == "admin") & (t2 == "admin"):
		t3.set("登录成功")
	else:
		t3.set("登录失败")
		entry1.delete(0,len(t1))
		entry2.delete(0,len(t2))
	Label(root,textvariable=t3).grid(row=3,column=0,sticky=EW)
	

Button(root,text="登录",command=callback).grid(row=2,column=1,sticky=EW)

root.mainloop()

'''
e.delete()删除内容
-- 删除参数 first 到 last 范围内（包含 first 和 last）的所有内容
-- 如果忽略 last 参数，表示删除 first 参数指定的选项
-- 使用 delete(0, END) 实现删除输入框的所有内容
'''

'''
************tkinter 的布局 ****************
1. 其实我们已经接触过 tkinter 的一种布局，就是 pack 布局，它非常简单，我们不用做过多的设置，直接使用一个pack 函数就可以了。
2.grid 布局： grid 可以理解为网格，或者表格，它可以把界面设置为几行几列的网格，我们在网格里插入我们想要的元素。这种布局的好处
是不管我们如何拖动窗口，相对位置是不会变化的，而且这种布局也超简单。
3.place 布局：它直接使用死板的位置坐标来布局，这样做的最大的问题在于当我们向窗口添加一个新部件的时候，又得重新测一遍数据，且
我们不能随便地变大或者缩小窗口，否则，可能会导致混乱。
**************pack 布局 *************
1. 我们使用 pack 函数的时候，默认先使用的放到上面，然后 依次向下排，它会给我们的组件一个自认为合适的位置和大小，这是默认方式，
也是我们上面一直采用的方式。
2. pack 函数也可以接受几个参数， side 参数指定了它停靠在哪个方向，可以为 LEFT,TOP,RIGHT,BOTTOM, 分别代表左，上，右，下，它的 
fill 参数可以是 X,Y,BOTH 和 NONE,即在水平方向填充，竖直方向填充，水平和竖直方向填充和不填充。
3. 它的 expand 参数可以是 YES和 NO，它的 anchor 参数可以是 N,E,S,W（这里的 NESW分别表示北东南西，这里分别表示上右下左）以及
他们的组合或者是 CENTER（表示中间）。
4. 它的 ipadx 表示的是内边距的 x 方向，它的 ipady 表示的是内边距的 y 方向， padx 表示的是外边距的 x 方向，pady 表示的是外边距
的 y 方向。
**************grid 布局 *************
1. 由于我们的程序大多数都是矩形，因此特别适合于网格布局，也就是 grid 布局。
2. 使用 grid 布局的时候，我们使用 grid 函数，在里面指定两个参数，用 row 表示行，用 column 表示列，其中值得注意的是 row 和 column 
的编号都从 0 开始。
3.grid 函数还有个 sticky 参数，它可以用 N， E， S， W表示上右下左，它决定了这个组件是从哪个方向开始的，下面的例子可以很好的解释这一点。
4.grid 布局直接用后面的行和列的数字来指定了它位于哪个位置，而不必使用其他参数。
5.grid 函数也支持诸如 ipadx ， ipady ， padx， pady，它们的意思和 pack 函数是一样的，默认边距是 0。
6. 它还支持参数比如 rowspan ，表示跨越的行数，columnspan 表示跨越的列数。
 *************place 布局 *************
1. 关于 place 布局，可能是最有东西好讲的，但是，也是我最不愿意讲的。
2. 它使用 place 函数，它分为绝对布局和相对布局，绝对布局使用 x 和 y 参数，相对布局使用 relx ， rely ，relheight 和 relwidth 参数。
3. 由于该方法我极度不推荐大家用，因此也就不继续说了。
*************** 总结 **************
1. 由于 place 我不推荐大家用，也就 pack 和 grid 布局好一些。
2. 但是 pack 和 grid 不能同时用，通常对于较为复杂点的，我还是建议大家用 gird 。
'''