'''
实现简单网页爬虫
网络爬虫， 就是抓取网页数据的程序。
网络爬虫的实现流程包括三个部分： 获取网页、 解析网页、 存储数据。
首先通过 Requests 库向指定的 URL 地址发送 HTTP 请求， 从而把整个网页的
数据爬取下来， 接着通过 BeautifulSoup 模块对页面数据进行解析并对目标数据
进行定位， 从而将需要的信息抽取出来， 最后通过文件操作将数据存储到指定的
文本文件中
'''
import requests#引入http客户端库
from bs4 import BeautifulSoup#引入网页解析利器 BeautifulSoup 模块

# 1.获取网页
# 为了保证访问的“合法” 性， 需要通过添加一个请求头参数， 将爬虫的请求
# 伪装成合法浏览器的访问， 这服务器才不会拒绝这次请求而返回完整的数据。
user_agent ="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;)"
headers={"User-Agent":user_agent}
url ="http://www.cnblogs.com/ALittleBee/default.html?page="
for i in range(1,11):
	urlf =url +str(i)
	res =requests.get(urlf,headers=headers)
# 2.解析数据
	soup =BeautifulSoup(res.text,"lxml")
	titles =soup.find_all('a',{'class':'postTitle2'})
'''
通过 Requests 的 get()方法将网页的全部内容保存在 res 变量中， 将 res
变量作为参数以‘lxml’ 作为解析器产生一个 BeautifulSoup 对象 soup：
soup = BeautifulSoup( res.text, "lxml" )
通过对页面 HTML 源码的分析， 可以得到目标内容的元素定位：
<1> 文章标题和链接的目标内容均包含在“class” 属性值为“postTitle2”
的“a” 标签中。
<2> 文章标题为“a” 标签中字符串内容。
<3> 链接信息为“a” 标签中的“href” 属性值。
首先利用该 BeautifulSoup 对象 res 的 find_all()方法将符合元素定位信息
的“a” 标签全部抽取出来， 形成一个列表。 该列表中的每一个元素实际上就是
博客中每篇文章的标题和链接信息。 通过遍历列表中的每一个元素， 只要把其中
的字符串和“href” 属性值提取出来， 分别赋值给 title 和 link 变量， 就可以
很容易的获得目标数据
'''	
# 3.存储数据
print(titles)
for item in titles:
	title =item.text.strip()
	link = item['href']

	with open("E:\\MySpider\\blogs.txt","a+") as f:
		f.write(title+'\n'+link+'\n')
