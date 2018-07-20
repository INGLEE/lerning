'''
干货满满！
参考资料：https://www.jianshu.com/p/571bb66bee1e
'''
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext  #导入滚动文本框模块

root = tk.Tk()
root.title("Python GUI")


# 创建一个容器 ttk.LabelFrame
monty = ttk.LabelFrame(root ,text ="Monty Python")
monty.grid(row = 0,column = 0,padx =10, pady=10)
aLabel =ttk.Label(monty,text ="A Label")

ttk.Label(monty , text ="Enter a name:").grid(row =0,column =0,padx =10)
ttk.Label(monty, text = "Choose a number").grid(row=0,column =1,padx =10)

# 输入文本框 ttk.Entry
name = tk.StringVar()
nameEntered = ttk.Entry(monty,textvariable = name,width =13)
nameEntered.grid(row = 1,column = 0,padx =10, sticky =tk.W)
# 当程序运行时,光标默认会出现在该文本框中
nameEntered.focus()

# 创建下拉列表 ttk.Combobox
number =tk.StringVar()
# 组合框，状态：只读
numberChosen =ttk.Combobox (monty,width =12,textvariable =number,state ='readonly')
# 设置下拉列表的值
numberChosen['values'] =(1,2,3,5,25,100)
numberChosen.grid(row =1,column =1)
# 设置下拉列表默认显示的值，这里的"0"为numberChosen['values']的下标值
numberChosen.current(0)


def clickMe():
	# 设置button显示的内容
	action.configure(text ='Hello ' +name.get()+' '+numberChosen.get())
	print('check3 is {0:1d}'.format(chvarEn.get()))



# 按钮  ttk.Button
action =ttk.Button(monty,text ="Click Me!",command =clickMe)
action.grid(row =1, column =2,padx=2)

# 复选框 tk.Checkbutton 
# variable 选项设置为 1 表示选中状态，反之设置为 0
chVarDis =tk.IntVar()
check1 = tk.Checkbutton(monty,text = "Disabled",variable = chVarDis,state ='disabled')
# 默认选择
check1.select()
check1.grid(row =4 ,column =0,sticky =tk.W)

chvarUn = tk.IntVar()
check2 = tk.Checkbutton(monty, text ="UnChacked",variable =chvarUn )
# 默认不选择
check2.deselect()
check2.grid(row =4,column =1 ,sticky =tk.W)

chvarEn =tk.IntVar()
check3 = tk.Checkbutton(monty,text ="Enabled",variable =chvarEn)
check3.select()
check3.grid(row = 4,column =2,sticky=tk.W)

# 单选按钮 Radiobutton
# 定义几个颜色的全局变量
colors =["Blue","Gold","Red"]

#
def radCall():
 	radSel =radVar.get()
 	if radSel == 0:
 		root.configure(background = colors[0])
 	elif radSel == 1:
 		root.configure(background =colors[1])
 	elif radSel == 2:
 		root.configure(background =colors[2])
 	print(radVar.get())

 # 通过tk.IntVar() 获取单选按钮value参数对应的值
radVar = tk.IntVar()
radVar.set(99)
for col in range(3):
	# variable:代表选中的单选按钮标签，可变；value 代表指定此单选按钮的标签，固定的值
	curRad =tk.Radiobutton(monty,text = colors[col],variable=radVar,value = col,command = radCall)
	curRad.grid(row =5,column =col,sticky=tk.W)

# 滚动文本框 scrolledtext.ScrolledText
scrolW = 30 
scrolH = 3
# wrap=tk.WORD 这个值表示在行的末尾如果有一个单词跨行，会将该单词放到下一行显示,
# 比如输入hello，he在第一行的行尾,llo在第二行的行首, 这时如果wrap=tk.WORD，则表示会将 hello 这个单词挪到下一行行首显示, wrap默认的值为tk.CHAR
scr =scrolledtext.ScrolledText(monty,width =scrolW,height = scrolH,wrap =tk.WORD)
# 三列合为一列
scr.grid(column =0 ,columnspan =3)

# 标签容器
# 创建一个容器，父容器为 monty
labelsFrame =ttk.LabelFrame(monty, text='Labels in a Frame')
labelsFrame.grid(row=7,column=1,sticky=tk.W)

# 将标签放入容器中
ttk.Label(labelsFrame,text='Label').grid(row =0,column =0)
ttk.Label(labelsFrame,text='Labe2').grid(row =0,column =1)
ttk.Label(labelsFrame,text='Labe3').grid(row =0,column =2)

# labelsFrame.winfo_children 可以获取labelsFrame容器的所有子部件的对象 
for child in labelsFrame.winfo_children(): 
	child.grid_configure(padx=8, pady=4) 
	# 通过子部件对象的grid_configure()方法可以修改部件的属性

root.mainloop()