# -*- coding: UTF-8 -*- 
import tkinter.filedialog as filedialog
from tkinter import *
import os
from tkinter import *
import chardet
pathlist=[]
namelist=[]
filepath1=""
filepath2=""
def sel_src():
    entry1.delete(0,END) #清空entry里面的内容
    # listbox_filename.delete(0,END)
    # #调用filedialog模块的askdirectory()函数去打开文件夹
    global filepath1
    filepath1 = filedialog.askdirectory() 
    if filepath1:
        entry1.insert(0,filepath1) #将选择好的路径加入到entry里面
    # print (filepath1)

 
def sel_dst():
    entry2.delete(0,END) #清空entry里面的内容
    # listbox_filename.delete(0,END)
    # #调用filedialog模块的askdirectory()函数去打开文件夹
    global filepath2
    filepath2 = filedialog.askdirectory() 
    if filepath2:
        entry2.insert(0,filepath2) #将选择好的路径加入到entry里面
    # print (filepath2)

    
def destroy():
	root.destroy()

def dealFile(filepath):
	# print(filepath)
	pattern = '(.*?通信功能测试脚本 - RSP)'
	newfilepath=re.sub(pattern,filepath2+'/通信功能测试脚本 - RSP',filepath)
	pattern ='log'
	newfilepath=re.sub(pattern,'txt',newfilepath)
	path=os.path.split(newfilepath)[0]

	if not os.path.exists(path):
		
		os.makedirs(path)
	# else:
	# 	print('文件夹已存在！')
		
	f1 = open(filepath,'r+',encoding='ISO-8859-1')#打开传进来的路径
	log=f1.readlines()	
	f2 =open(newfilepath,'w+')

	if os.path.getsize(filepath)!=0:
		f2.write('Main:\r')
		f2.write('\n')
		for i in log:

			if i[0:13]=='AH:0012000000':
				f2.write('\tReset SmartCard\n')
			elif i[0:3]=='AH:':
				f2.write('\t'+i[3:-1])
			elif i[0:3]=='ES:':
				if '/' in i:
					i=re.sub('/','|',i)
				if '00~'in i:
					if '0000~FFFF' in i:						
						i=re.sub('0000~FFFF','XXXX',i)
						f2.write(';SW='+i[3:-1])
						f2.write('\n')
					else:	
						i=re.sub('00~','XX|',i)
						f2.write(';SW='+i[3:-1])
						f2.write('\n')
				else:
					f2.write(';SW='+i[3:-1])
					f2.write('\n')
			elif i[0:3]=='ED:':
				f2.write(';DE='+i[3:-1])
			
		f2.write('End\n')	
		
	f2.close()
	f1.close()


# def dealFile(filepath,filename):
# 	f1 = open(filepath,'r+',encoding='ISO-8859-1')#打开传进来的路径
# 	log=f1.readlines()
# 	# print(filename)
# 	newpath=os.path.join("G:\\桌面\新建文件夹",filename)
# 	newpath=newpath.replace('/','_')
# 	# newpath
# 	# print(newpath)
# 	f2 =open(newpath,'w+')
# 	f2.write('Main:\r')
# 	f2.write('\n')
# 	count=0D
# 	for i in log:
# 		if i[0:13]=='AH:0012000000':
# 			f2.write('\tReset SmartCard\n')
# 		elif i[0:3]=='AH:':
# 			f2.write('\t'+i[3:-1])
# 		elif i[0:3]=='ES:':
# 			f2.write(';SW='+i[3:-1])
# 			f2.write('\n')
# 		elif i[0:3]=='ED:':
# 			f2.write(';DE='+i[3:-1])
			
# 	f2.write('End\n')	
# 	f2.close()
# 	f1.close()




def conversion():
	eachFile(filepath1)
	pass


def eachFile(filepath):
    """
    用于获取目录下的文件列表
    """
    cf = os.listdir(filepath)
    for i in cf:
       # print(i)
       child=os.path.join('%s/%s' % (filepath, i))
       # print(child)
       if os.path.isfile(child) : #如果是文件
       	if os.path.splitext(child)[1]==".log":#判断是否是log
       		# print("是log")
       		path=os.path.split(child)[0]
       		global pathlist
       		pathlist.append(path)

       		filename=os.path.split(child)[1]
       		global namelist
       		namelist.append(filename)
       		dealFile(child)

       		# filename=child.split()      		
       		# dealFile(child,filename[2])
       	pass
       else:
       	eachFile(child) #如果不是文件，递归这个文件夹的路径
 
if __name__ == "__main__":
    root = Tk()
    root.title("Conversion tool for communication scripts")
    root.geometry("400x130")
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=8)
 
    entry1 = Entry(root, width=40)
    entry1.grid(sticky=W+N, row=0, column=0, padx=10, pady=15)
 
    button1 = Button(root,text="选择log文件夹",command=sel_src)
    button1.grid(sticky=W+N, row=0, column=1, padx=2, pady=10)

    entry2 = Entry(root, width=40)
    entry2.grid(sticky=W+N, row=1, column=0, padx=10, pady=5)
 
    button2 = Button(root,text="选择目标文件夹",command=sel_dst)
    button2.grid(sticky=W+N, row=1, column=1, padx=2)

    button3 = Button(root,text="转换",command=conversion,width=8)
    button3.grid(row=2, column=0, pady=5)

    button4 = Button(root,text="取消",command=destroy,width=8)
    button4.grid(row=2, column=1, pady=5)

    #  #创建loistbox用来显示所有文件名
    # listbox_filename = Listbox(root, width=60)
    # listbox_filename.grid(row=2, column=0, columnspan=4, rowspan=4, padx=5, pady=5, sticky=W+E+S+N)
 
    root.mainloop()