from tkinter import *
from tkinter.messagebox import * 

# 1.showinfo显示消息提示框 ,显示确定按钮，返回OK字符串；点击右上角x号，同样显示OK字符串
showinfo(title="showinfo",message ="点燃梦想，就是现在")

# 2.askyesno返回一个bool类型，如果yes被点击，返回True，no被点击，返回False
askyesno("askyesno","显示yes和no按钮，问号图标")

# 3.askquetion和askyesno几乎一模一样的方法是
# 其实不同的只有返回值，askquetion返回一个字符串，如果yes被点击则返回yes，no被点击则返回no
askquestion("askquestion","显示yes和no按钮 问号图标 和askyesno大致相同，不同的是返回值")

# 4.askokcancel方法则是显示ok按钮和cancel（取消）按钮，如果ok被点击返回True，cancel被点击则返回False
askokcancel("askokcancel方法应用","您要继续安装吗？")

# 5.askyesnocancel方法显示3个按钮，分别是yes、no、cancel。当yes按钮被点击，返回True，no按钮被点击返回False，如果cancel被点击返回一个None.
askyesnocancel("askyenocancel方法应用","程序出现了某种错误，是否继续运行？点击取消撤销当前更改")

# 6.askretrycancel方法显示一个retry按钮（重试）和cancel按钮（取消），如果retry按钮被点击，返回True，cancel按钮被点击返回False
askretrycancel("askretrycancel方法应用","很不幸，读取***文件失败，是否重试？")

# 7.showwarning显示警告消息框 返回值和showinfo方法相同，同是返回一个ok字符串。
showwarning("showwarning方法应用","检测到您当前的系统版本不是正版，珍爱生命，远离盗版")

# shouwerror 显示错误信息，返回值一样是一个ok字符串
showerror("showerror","程序错误")

# 另外这些对话框的图标，要修改的小伙伴我们只能通过tk窗口的iconbitmap方法进行修改，假设C盘下有一个1.ico的图标文件的话。如下：
# import tkinter
# win = tkinter.Tk()
# win.iconbitmap("c:\\1.ico")
# tkinter.messagebox.showinfo("看图标哦","哈哈")
# win.mainloop()
# shouwerror("showerror","程序错误")
