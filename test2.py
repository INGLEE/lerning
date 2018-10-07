'''
python 基础试题五	
用字典值对字典进行排序，{1：2,3：4,4：3,2:1,0:0}
按照字典的值从大到小排序
'''
import operator
x ={1:2,3:4,4:3,2:1,0:0}
sorted_x =sorted(x.items(),key =operator.itemgetter(1))
print(sorted_x)
# 对字典排序是不可能的，因为字典本身是无序的。只有转换成类似列表元组这种类型

# python中的对象有两种：可变对象和不可变对象
# 可变：list,dict
# 不可变：tuples，strings,numbers