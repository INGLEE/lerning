'''
tk 学习--贪吃蛇
***************** 思路分析 ***************
1. 首先就是对于蛇的操作，它应该有一个方向，这个方向用于改变蛇头的移动位置，然后后面的蛇身需要跟着蛇头
的移动而改变相应的位置。
2. 对于蛇的实现，可以每次从蛇的末尾截掉一截，然后拼接到蛇头上，让他当做新的蛇头，截掉的蛇尾即新的蛇头
应该知道蛇的移动方向，具体的数据结构可以用队列
3. 然后就是食物的实现，这个就很简单了，只需要随机出现就可以了。
4. 然后就是界面的绘制，这个我们也采取“一切从简”的思路，绘制一个黑色的背景，然后绘制上必要的元素即可。
5. 然后就是对键盘按键的响应，要是想实现对键盘的响应和蛇的移动不会发生任何的冲突，也就是按键的时候不影
响界面的刷新，可以考虑使用多线程，因为这里有用到一个死循环，如果在一个线程内做这件事，就不很方便了。
'''
from tkinter import *
import queue
import time
import threading
import random

class GUI(Tk):
	# __init__ 函数用于初始化，（顺便包括了需要导入的文件）
	def __init__(self,queue):
		Tk.__init__(self)
		self.queue=queue
		self.is_game_over =False
		self.canvas = Canvas(self,width =495,height =305 ,bg="#000000")
		self.canvas.pack()
		self.snake =self.canvas.create_line((0,0),(0,0),fill ="#FFCC4C",width =10)
		self.food = self.canvas.create_rectangle(0,0,0,0,fill ="#FFCC4C",outline ="#FFCC4C")
		self.points_earned =self.canvas.create_text(452,15,fill="white",text ="score:0",font=('Verdana',10,'bold'))
		# 创建完毕之后，调用一个queue_handler,用于处理该队列的一系列消息：
		self.queue_handler()

# 该 queue_handler ，用于从队列中不断的取出消息，然后判断它的类型，并执行相应的操作，
	def queue_handler(self):
		try:
			while True:
				task =self.queue.get(block =False)
				if task.get('game_over'):
					self.game_over()
				if task.get('move'):
					points =[x for point in task['move'] for x in point]
					self.canvas.coords(self.snake,*points)
				if task.get('food'):
					self.canvas.coords(self.food,*task['food'])
				elif task.get('points_earned'):
					self.canvas.itemconfigure(self.points_earned,text='score:{}'.format(task['points_earned']))
					self.queue.task_done()

		except queue.Empty:
				if not self.is_game_over:
					self.canvas.after(100,self.queue_handler)

# 这里需要该类完成的就是一个游戏结束的操作，因为游戏结束之后，需要绘制一个按钮来结束游戏
	def game_over(self):
		self.is_game_over =True
		self.canvas.create_text(200,150,fill="white",text ="Game Over")
		quitbtn =Button(self,text ="Quit",command =self.destroy)
		rebtn = Button(self,text ="Begin",command =self.__init__)
		self.canvas.create_window(200,100,anchor ='nw',window =quitbtn)



class Food():
	"""docstring for Food"""
	def __init__(self, queue):
		self.queue = queue
		self.generate_food()

	def generate_food(self):
		x =random.randrange(5,480,10)
		y =random.randrange(5,295,10)
		self.position =x,y
		self.exppos =x-5,y-5,x+5,y+5
		self.queue.put({'food':self.exppos})

'''
************* 蛇的实现 ***************
1. 可能蛇的实现是这些所有模块里最复杂的一个，我们先来分析一下思路，
蛇的移动的绘制部分是在 GUI 类里面完
成，即这里只能从逻辑上控制蛇的运动，但是不能用向屏幕上画出东西。
2. 这里我们分析该类，它的 __init__ 方法用于初始化该类，
它的 run 方法是继承自 Thread 类，实例化后会自动一直执
行， run 方法主要是维持蛇的运动
'''
class Snake(threading.Thread):
	def __init__(self, gui,queue):
		threading.Thread.__init__(self)
		self.gui =gui
		self.queue =queue
		self.daemon =True
		self.points_earned = 0
		self.snake_points =[(495,55),(485,55),(475,55),(465,55),(455,55)]
		self.food =Food(queue)
		self.direction ='Left'
		self.start()

	def run(self):
		if self.gui.is_game_over:
			self.delete()
		while not self.gui.is_game_over:
			self.queue.put({'move':self.snake_points})
			time.sleep(0.5)
			self.move()

	# 3.然后设置按键的响应和 move事件
	def key_pressed(self,e):
		self.direction =e.keysym

	def move(self):
		new_snake_point =self.calculate_new_coordinates()
		if self.food.position == new_snake_point:
			self.points_earned +=1
			self.queue.put({'points_earned':self.points_earned})
			self.food.generate_food()
		else:
			self.snake_points.pop(0)
			self.check_game_over(new_snake_point)
			self.snake_points.append(new_snake_point)

	# 4. 下面这两个方法一个用于计算新的位置，第二个方法用于在游戏结束后停止计算蛇的位置：
	def calculate_new_coordinates(self):
		last_x,last_y =self.snake_points[-1]
		if self.direction =='Up':
			new_snake_point =last_x,(last_y-10)
		elif self.direction =='Down':
			new_snake_point =last_x,(last_y+10)
		elif self.direction =='Left':
			new_snake_point = (last_x-10,last_y)
		elif self.direction == 'Right':
			new_snake_point =(last_x+10,last_y)
		return new_snake_point

	def check_game_over(self,snake_point):
		x,y = snake_point[0],snake_point[1]
		if not -5<x<505 or not -5<y<315 or snake_point in self.snake_points:
			self.queue.put({'game_over':True})



def main():
	global q,gui
	q= queue.Queue()
	gui =GUI(q)
	gui.title("Snake")
	snake =Snake(gui,q)
	gui.bind('<Key-Left>',snake.key_pressed)
	gui.bind('<Key-Right>',snake.key_pressed)
	gui.bind('<Key-Up>',snake.key_pressed)
	gui.bind('<Key-Down>',snake.key_pressed)
	gui.mainloop()


if __name__ == '__main__':
	main()
		
		
