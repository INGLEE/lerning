from tkinter import *

colours = ['red','green','orange','white','yellow','blue']

r = 0 
for c in colours:
	#relief =RIDGE 丘岭
	Label(text = c , relief = RIDGE ,width =15).grid(row = r,column = 0)
	#relief =SUNKEN 凹陷
	Entry(bg =c ,relief =SUNKEN,width =10).grid(row = r,column = 1)
	r +=1

mainloop() 
