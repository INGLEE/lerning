# -*- coding:utf-8 -*-
'''
python 基础试题一
使用python中循环打出1~100的奇数
'''
for i in range(1,101):
	if i%2 !=0:
		print(i,end =" ")


'''
python 基础试题二
请将字符串“你好$$$我正在学Python@#@#现在需要&*&*&修改字符串”
中的符号变成一个空格，
'''
str1 = "你好$$$我正在学Python@#@#现在需要&*&*&修改字符串"
import re
str2=re.sub("[$@#&*]+"," ",str1)# +表示 1次或多次
print(str2)

'''
python 基础试题三
请输出9*9乘法表
'''
for i in range(1,10):
	for j in range(1,i+1):
		print(i*j," = ",i,"*",j ,end =" ")#不换行
	print(" ")#回车换行
