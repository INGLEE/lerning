import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
import hashlib
import time
import ctypes

LOG_LINE_NUM =0

class MY_GUI():
	
	def __init__(self, init_window):
		self.init_window =init_window
		self.str_trans =STR_TRANS(self)
		# 设置状态栏显示工具小图标
		ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
	# 设置窗口
	def set_init_window(self):
		self.init_window.title("文本处理工具V1.0  By :Lirj ") 
		self.init_window.geometry('1068x680+10+10')
		# self.init_window['bg']='white'
		# 设置工具小图标
		self.init_window.iconbitmap("rongcard.ico")

		self.init_window.attributes('-alpha',0.9)# 虚化，值越小虚化程度越高
		# 输入界面
		self.init_label_frame = ttk.LabelFrame(self.init_window,text ="待处理的数据",relief ="raised")
		self.init_label_frame.grid(row = 0,column = 0,padx =10, pady=10,sticky='W')
		self.init_data_text =tk.Text(self.init_label_frame,width=60,height=30)
		self.init_data_text.grid(row =0,column =0,columnspan=2)
		self.init_data_openfile=ttk.Button(self.init_label_frame,text ="打开文件",command=lambda:self.str_trans.input_init_data("openfile"))
		self.init_data_openfile.grid(row =1 ,column =0,padx=2,pady=2)
		self.clear_btn1 = ttk.Button(self.init_label_frame,text ="一键清空",command=lambda:self.str_trans.clear("clear_btn1"))
		self.clear_btn1.grid(row =1,column =1,padx=2,pady=2)
		# 日志界面
		self.separator_label =ttk.Label(self.init_label_frame,text='-'*100)
		self.separator_label.grid(row=2,column=0,columnspan=2,sticky='W')
		self.log_label_frame =ttk.LabelFrame(self.init_label_frame,text="日志",relief ='raised')
		self.log_label_frame.grid(row =3,column =0,columnspan=3,padx=10,pady =10)
		self.log_data_text =tk.Text(self.log_label_frame,width=60,height =10)
		self.log_data_text.grid(row =0,column =0,columnspan=3,sticky='W')
		self.clear_btn2 = ttk.Button(self.log_label_frame,text ="一键清空",command =lambda:self.str_trans.clear("clear_btn2"))
		self.clear_btn2.grid(row =1,column =0,columnspan=2,padx=2,pady=2) 

		# 输出界面
		self.output_label_frame =ttk.LabelFrame(self.init_window,text = "输出结果",relief ="raised")
		self.output_label_frame.grid(row = 0,column =2,padx =10,pady =10,sticky='N')
		self.output_data_text = tk.Text(self.output_label_frame,width =53,height =45)
		self.output_data_text.grid(row =0,column =0 ,columnspan = 2,padx =10 ,pady =10,sticky='W')
		self.clear_btn3 = ttk.Button(self.output_label_frame,text ="一键清空",command =lambda:self.str_trans.clear("clear_btn3"))
		self.clear_btn3.grid(row =1,column =0,columnspan=2,padx=2,pady=2) 

		# 滚动条对于展示长文本，需要在Text文本框侧翼（或下方）提供滚动条；tkinter库中提供Scrollbar()方法创建一个滚动条
		# ps1：滚动条与待绑定的组件（Text或其他）时，需要二者相互绑定，从而达到拖动任意一方，对应方同步移动；
		# ps2：grid()中rowspan的值最好取Text文本框的值，可以使滚动条长度完美贴合文本框
		self.output_data_scrollbar_y = tk.Scrollbar(self.output_label_frame) #创建scrollbar
		self.output_data_scrollbar_y.config(command =self.output_data_text.yview) #将scrollbar与text y方向绑定
		self.output_data_text.config(yscrollcommand = self.output_data_scrollbar_y.set) #将Text反向绑定
		self.output_data_scrollbar_y.grid(row =0,column =100,rowspan=2,sticky='NS')

		self.init_data_scrollbar_y = tk.Scrollbar(self.init_label_frame)
		self.init_data_scrollbar_y.config(command = self.init_data_text.yview)
		self.init_data_text.config(yscrollcommand =self.init_data_scrollbar_y.set)
		self.init_data_scrollbar_y.grid(row =0,column=100,rowspan=2,sticky='NS')

		self.log_data_scrollbar_y = tk.Scrollbar(self.log_label_frame)
		self.log_data_scrollbar_y.config(command = self.log_data_text.yview)
		self.log_data_text.config(yscrollcommand = self.log_data_scrollbar_y.set)
		self.log_data_scrollbar_y.grid(row =0,column =100,rowspan=2,sticky='NS')

		#功能 按钮
		self.btn_label_frame =ttk.LabelFrame(self.init_window)
		self.btn_label_frame.grid(row=0,column =1)
		self.str_trans_to_md5_button =ttk.Button(self.btn_label_frame,text="字符串转MD5",command=lambda:self.str_trans.data_change("str_trans_to_md5"))
		self.str_trans_to_md5_button.grid(row = 0,column =1,pady =2)
		self.str_trans_to_reverse_button =ttk.Button(self.btn_label_frame,text="字符串反转",command =lambda:self.str_trans.data_change("str_trans_to_reverse"))
		self.str_trans_to_reverse_button.grid(row = 1,column =1,pady =2) 
		self.str_trans_bytes_to_str_button =ttk.Button(self.btn_label_frame,text="bytes 转 str",command =lambda:self.str_trans.data_change("str_trans_bytes_to_str"))
		self.str_trans_bytes_to_str_button.grid(row = 2,column =1,pady =2) 
		self.str_trans_all_to_upper_button =ttk.Button(self.btn_label_frame,text="全部转大写",command =lambda:self.str_trans.data_change("str_trans_all_to_upper"))
		self.str_trans_all_to_upper_button.grid(row = 3,column =1,pady =2) 
		self.str_trans_all_to_lower_button =ttk.Button(self.btn_label_frame,text="全部转小写",command= lambda:self.str_trans.data_change("str_trans_all_to_lower"))
		self.str_trans_all_to_lower_button.grid(row = 4,column =1,pady =2) 
		self.str_trans_to_tlv_button =ttk.Button(self.btn_label_frame,text ="TLV解析",command =lambda:self.str_trans.data_change("str_trans_to_tlv"))
		self.str_trans_to_tlv_button.grid(row =5,column=1,pady =2)

	# 功能函数
class STR_TRANS():
		def __init__(self, gui):
			self.gui =gui

		def data_change(self,type=None):
			# 向Text组件中文本的位置，跟python的序列索引一样，Text的组件索引也是对应实际字符之间的位置。值得注意的是： 行号以1开始 列号以0开始
			src=self.gui.init_data_text.get(1.0,tk.END).strip().replace("\n","").encode()
			# print("src:",src)
			if type is not None:							
				if src:
					if type == "str_trans_to_md5":
						try:
							myMd5 = hashlib.md5()
							myMd5.update(src)
							myMd5_Digest = myMd5.hexdigest()
							print("myMd5_Digest：",myMd5_Digest)
							# 输出到界面
							self.gui.output_data_text.delete(1.0,tk.END)
							self.gui.output_data_text.insert(1.0,myMd5_Digest)
							self.write_log_to_Text("INFO:str_trans_to_md5 success")
						except Exception as e:
							self.gui.output_data_text.delete(1.0,tk.END)
							self.gui.output_data_text.insert(1.0,"字符串转MD5失败,原因是：{}".format(e)) 
					elif type == "str_trans_to_reverse":
						try:
							src=list(src.decode())#字符串转列表
							src.reverse()#列表元素反转
							reverse_data ="".join(src)#列表转字符串
							# 输出到界面
							self.gui.output_data_text.delete(1.0,tk.END)
							self.gui.output_data_text.insert(1.0,reverse_data)
							self.write_log_to_Text("INFO:str_trans_to_reverse success")
						except Exception as e:
							self.gui.output_data_text.delete(1.0,tk.END)
							self.gui.output_data_text.insert(1.0,"字符串反转失败,原因是：{}".format(e)) 
					elif type == "str_trans_bytes_to_str":
						try:
							bytes_to_str =src.decode()
							# 输出到界面
							self.gui.output_data_text.delete(1.0,tk.END)
							self.gui.output_data_text.insert(1.0,bytes_to_str)
							self.write_log_to_Text("INFO:str_trans_bytes_to_str success")
						except Exception as e:
							self.gui.output_data_text.delete(1.0,tk.END)
							self.gui.output_data_text.insert(1.0,"字节转字符串失败,原因是：{}".format(e)) 
					elif type == "str_trans_all_to_upper":
						try:
							str_upper =src.upper()
							# 输出到界面
							self.gui.output_data_text.delete(1.0,tk.END)
							self.gui.output_data_text.insert(1.0,str_upper)
							self.write_log_to_Text("INFO:str_trans_all_to_upper success")
						except Exception as e:
							self.gui.output_data_text.delete(1.0,tk.END)
							self.gui.output_data_text.insert(1.0,"字符串小写转大写失败,原因是：{}".format(e)) 
					elif type == "str_trans_all_to_lower":
						try:
							str_lower =src.lower()
							# 输出到界面
							self.gui.output_data_text.delete(1.0,tk.END)
							self.gui.output_data_text.insert(1.0,str_lower)
							self.write_log_to_Text("INFO:str_trans_all_to_lower success")							
						except Exception as e:
							self.gui.output_data_text.delete(1.0,tk.END)
							self.gui.output_data_text.insert(1.0,"字符串大写转小写失败,原因是：{}".format(e)) 
					elif type == "str_trans_to_tlv":
						src=src.decode()
						time = 0
						self.gui.output_data_text.delete(1.0,tk.END)
						try:
							while True:
								if src[0:1] in ['8','9','A','B','C','D','E','F','3','6']:
									
									if '81' ==src[2:4]:
										l=int(src[4:6],16)*2+6
										# print("["+src[:2]+"] "+src[2:6]+" "+src[6:l])
										# 输出到界面
										self.gui.output_data_text.insert(tk.INSERT,"["+src[:2]+"] "+src[2:6]+" "+src[6:l]+"\n")									
										if l ==len(src):
											src =src[6:]
										else:
											src = src[l:]
										time +=1
										continue							
									elif '82' == src[2:4]:
										l=(int(src[4:8],16))*2+8
										# print("["+src[:2]+"] "+src[2:10]+" "+src[10:l])
										# 输出到界面
										self.gui.output_data_text.insert(tk.INSERT,"["+src[:2]+"] "+src[2:8]+" "+src[8:l]+"\n")
										print(l,len(src))	
										if l == len(src):
											src =src[8:]
										else:	
											src = src[l:]
										time +=1
										continue
									else:
										l=(int(src[2:4],16))*2+4
										# print("["+src[:2]+"] "+src[2:4]+" "+src[4:l])
										# 输出到界面
										self.gui.output_data_text.insert(tk.INSERT,"["+src[:2]+"] "+src[2:4]+" "+src[4:l]+"\n")
										
										if l ==len(src):
											src =src[4:]
										else:
											src = src[l:]
										# print(src)
										time +=1
										continue	
								else:
									if time > 0:
										# 输出到界面
										self.write_log_to_Text("INFO:str_trans_to_tlv success")
									else:
										# 输出到界面
										self.write_log_to_Text("INFO:str_trans_to_tlv failed")
									break							
						except Exception as e:
							raise e
				else:
					self.write_log_to_Text("ERROR:{} failed".format(type))#支持日志动态打印

		def input_init_data(self,type=None):
			if  type is not None:
				if type =="openfile":
					self.gui.init_data_text.delete(1.0,tk.END)
					name=askopenfilename()
					f =open(name,'r+')
					init_data=f.readlines()
					for i in init_data:
						# print(i)
						# 输出到界面
						self.gui.init_data_text.insert(tk.INSERT,i)
		def get_current_time(self):
			current_time =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			return current_time

		# 日志动态打印
		def write_log_to_Text(self,logmsg):
			global LOG_LINE_NUM
			current_time =self.get_current_time()
			logmsg_in =str(current_time)+" "+str(logmsg)+"\n"
			# if LOG_LINE_NUM <=7:
			self.gui.log_data_text.insert(tk.END,logmsg_in)
			LOG_LINE_NUM +=1
			# else:
			# 	self.gui.log_data_text.delete(1.0,2.0)
			# 	self.gui.log_data_text.insert(tk.END,logmsg_in)
			# 移动光标
			self.gui.log_data_text.focus_force()

		def clear(self,type=None):
			if type is not None:
				if type =="clear_btn1":
					self.gui.init_data_text.delete(1.0,tk.END)
				elif type == "clear_btn2":
					self.gui.log_data_text.delete(1.0,tk.END)
				elif type == "clear_btn3":
					self.gui.output_data_text.delete(1.0,tk.END)


def main():
	root =tk.Tk()
	mytool=MY_GUI(root)
	mytool.set_init_window()

	root.mainloop()

if __name__ == '__main__':
	main()


	