'''
屏保
'''
import tkinter as tk
from tkinter.ttk import *

'''
两个类，一个类RandomBall 画图 用来产生随机的球；两个方法：创建、移动
另一个类 主程序类 设计屏保大小，去边框，运行
'''
class RandomBall():
	"""docstring for RandomBall"""
	def __init__(self, arg):
		super(RandomBall, self).__init__()
		self.arg = arg

	def create_ball(self):
		pass

	def move_ball(self):
		pass

class ScreenSaver():
	"""docstring for ScreenSaver"""
	def __init__(self, arg):
		super(ScreenSaver, self).__init__()
		self.arg = arg
	
	def run_screen_saver(self):
		pass

	def my_quit(self,event):
		pass

if __name__ == '__main__':
	main()