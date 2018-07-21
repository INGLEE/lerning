import tkinter as tk
from tkinter import *
import os,re,time,random
from builtins import *
from tkinter import messagebox
from tkinter import simpledialog
import threading


def showinfo(errortitle,errormessage):
	messagebox.showinfo(title=errortitle,message=errormessage)


class Data_change():


    def __init__(self):
        pass

    def add_0x(self, arg_i=''):
        """
        The fun to add 0x

        :return: res
        """
        res = ''
        p = re.compile('\w', flags=re.M | re.I | re.S)
        w = re.findall(p, arg_i)
        arg_i = ''.join(w)
        while (arg_i):
            res += "0x" + arg_i[:2] + ","
            arg_i = arg_i[2:]
        return res.rstrip(',')

    def del_0x(self, arg_i):
        """
        The fun to delete 0x.

        2 bytes 有补0的选择,分隔符默认是逗号
        0x12,0x34 --> 1234
        0x1,0x23  --> 0123 补0



        :return:
        """
        p = re.compile('\w', flags=re.M | re.I | re.S)
        w = re.findall(p, arg_i)
        ww = ''.join(w).upper().split("0X")
        arg_i = ""
        for w in ww:
            if len(w) == 0:
                continue
            arg_i += w.zfill(2)
        return (arg_i)

    def del_space(self, arg_i):
        return arg_i.replace(' ','')

    def tocase(self, arg_i):
        return arg_i.upper()

    def reverse(self, arg_i):
        return arg_i[-2::-1]

    def tlv(self,arg_i):
        pass

    def del_comment(self,arg_i):
        pattern = re.compile('//.*')
        arg_i = re.sub(pattern, "", arg_i)
        pattern = re.compile('/\*.*\*/')
        arg_i = re.sub(pattern, "", arg_i)
        return arg_i

class Data_generate():

    def __init__(self):
        pass

    def data_rand(self):
        num = simpledialog.askstring("随机数据生成", '数据长度')
        if num is None:
            num = 8
        else:
            for n  in num:
                if n.isdigit() is not True:
                    showinfo("数据错误","请输入正确的十进制数据长度！")
                    return ""
            num = int(num)

        res = ""
        while(num):
            n = random.randint(0,255)
            res += str(hex(n)).lstrip("0x").zfill(2)
            num -= 1
        return res.upper()
 
    def data_order(self):
        num = simpledialog.askstring("顺序数据生成", '数据长度-起始（8-0-255）只有一个数，默认为数据长度')
        numn = 8
        nums = 0
        nume = 256
        if num is not None:
            num = num.split("-")
            for n  in num[0]:
                if n.isdigit() is not True:
                    showinfo("数据错误","请输入正确的十进制数据长度！")
                    return ""
                if len(num[0]) != 0:
                    numn = int(num[0],10)

            if (len(num) >= 2) :
                for n in num[1]:
                    if n.isdigit() is not True:
                        showinfo("数据错误", "请输入正确的十进制数据长度！")
                        return ""
                if len(num[1]) != 0:
                    nums = int(num[1],10)
                    if nums > 255:
                        nums = 255

            if (len(num) == 3) :
                for n in num[2]:
                    if n.isdigit() is not True:
                        showinfo("数据错误", "请输入正确的十进制数据长度！")
                        return ""
                if len(num[2]) != 0:
                    nume = int(num[2],10)
                    nume = 256 if nume > 255 else (nume+1)

        res = ""
        nums = (nume - 1) if nums>nume else nums
        while(numn):
            for n in range(nums,nume):
                res += str(hex(n)).lstrip("0x").zfill(2)
                numn -= 1
                if numn == 0:
                    break

        return res.upper()


class App_command(tk.Frame):

    def __init__(self, master=None, din=None, dout=None):
        tk.Frame.__init__(self, master)
        self.grid(row=0, column=1, sticky='ns')
        self.data_change = Data_change()
        self.data_generate = Data_generate()
        self.in_text = din
        self.out_text = dout
        self.state = "data_cahange"
        self.create_data_cahange()
        self.create_data_generate()
        self.data_cahange_grid()
        self.Acase = True


    def double_event(self, event):
        self.Acase = False

    def create_data_cahange(self):
        self.add_0 = tk.Button(self, text="增加 0x  ", command=lambda : self.change("add_0x"))
        self.add_1 = tk.Button(self, text="删除 0x  ", command=lambda : self.change("del_0x"))
        self.add_2 = tk.Button(self, text="删除空格", command=lambda : self.change("del_"))
        self.add_2.bind('<Double-1>', self.double_event)
        self.add_3 = tk.Button(self, text="逆序排列", command=lambda: self.change("reverse"))
        self.add_4 = tk.Button(self, text=" 大小写 ", command=lambda : self.change("case"))
        self.add_4.bind('<Double-1>', self.double_event)
        self.add_5 = tk.Button(self, text=" TLV ", command=lambda: self.change("tlv"))
        self.add_6 = tk.Button(self, text="删除注释", command=lambda: self.change("del_//"))
        self.add_6.bind('<Double-1>', self.double_event)

    def data_cahange_grid(self, arg=True):
        if self.state is not "data_cahange":
            self.data_generate_grid(False)
            self.state = "data_cahange"
        if arg :
            rownum = 0
            self.add_0.grid(row=rownum, column=0, sticky='ew')
            rownum+=1
            self.add_1.grid(row=rownum, column=0, sticky='ew')
            rownum+=1
            self.add_2.grid(row=rownum, column=0, sticky='ew')
            rownum+=1
            self.add_3.grid(row=rownum, column=0, sticky='ew')
            rownum+=1
            self.add_4.grid(row=rownum, column=0, sticky='ew')
            rownum+=1
            self.add_5.grid(row=rownum, column=0, sticky='ew')
            rownum += 1
            self.add_6.grid(row=rownum, column=0, sticky='ew')
        else:
            self.add_0.grid_forget()
            self.add_1.grid_forget()
            self.add_2.grid_forget()
            self.add_3.grid_forget()
            self.add_4.grid_forget()
            self.add_5.grid_forget()
            self.add_6.grid_forget()
            self.state = None

    def create_data_generate(self):
        self.gen_rand = tk.Button(self, text="随机序列", command=lambda : self.generate("rand"))
        self.gen_order = tk.Button(self, text="顺序序列", command=lambda: self.generate("order"))

    def data_generate_grid(self, arg=True):
        if self.state is not "data_generate":
            self.data_cahange_grid(False)
            self.state = "data_generate"
        if arg :
            rownum = 0
            self.gen_rand.grid(row=rownum, column=0, sticky='s')
            rownum+=1
            self.gen_order.grid(row=rownum, column=0, sticky='s')
            rownum+=1
        else:
            self.gen_rand.grid_forget()
            self.gen_order.grid_forget()
            self.state = None

    def change(self, type=None):
        mychange = {"add_0x": self.data_change.add_0x, "del_0x":self.data_change.del_0x, \
                    "del_": self.data_change.del_space, "case":self.data_change.tocase,\
                    "reverse":self.data_change.reverse, "del_//": self.data_change.del_comment\
                    }
        self.out_text.delete(1.0, END)

        if type is not None:
            if type == 'tlv':
                tlv_index = self.in_text.index(INSERT)
                msg = self.in_text.get(tlv_index, END)
                L = 0
                Sl = 1
                if '82' == msg[:2]:
                    L = int(msg[2:6],16)*2 + 6
                    Sl = 3*2
                elif '81' == msg[:2]:
                    L = int(msg[2:4], 16)*2 + 4
                    Sl = 2*2
                else:
                    L = int(msg[:2], 16)*2 + 2
                    Sl = 1 * 2
                if L > len(msg):
                    L = len(msg)

                tlv = tlv_index.split('.')
                tlv_n = int(tlv[0])
                tlv_m = int(tlv[1])
                self.in_text.insert(tlv[0]+'.'+str(tlv_m+L), "    ")
                self.in_text.insert(tlv[0] + '.' + str(tlv_m + Sl), "  ")
                # self.in_text.insert(tlv_index, "\n"+tlv_m*" ")
                self.in_text.insert(tlv_index,"  ")

            else:
                msg = self.in_text.get("0.0", "end")
                res = mychange[type](msg)
                if self.Acase is False and type is "case":
                    res = res.lower()
                    self.Acase = True
                if self.Acase is False and type is "del_":
                    res = res.replace('\n','').replace('\t', '').replace('\r', '')
                    self.Acase = True

                self.out_text.insert(INSERT,res)

    def generate(self, type=None):
        mygenerate = {"rand": self.data_generate.data_rand, "order": self.data_generate.data_order}
        self.in_text.delete(1.0, END)
        if type is not None:
            res = mygenerate[type]()
            self.in_text.insert(INSERT,res)

    def bytecod(self):
        pass

    def author(self):
        showinfo('作者信息','本软件由飞不起来完成')

    def about(self):
        showinfo('版权信息.copyright','版权融卡')

    def rfu_cmd(self):
        pass

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.menubar = Menu(master)
        self.create_text()
        self.command = App_command(master,self.text_in, self.text_out)
        self.create_menu()
        self.grid(row=0, column=0)

        self.create_in()
        self.create_grid()

        t1 = threading.Thread(target=self.shownum)
        t1.daemon = True
        t1.start()

        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        master.geometry("+%d+%d" % (x, y))
        master.config(menu=self.menubar)
        master.maxsize(800, 700)

    def create_menu(self):
        menu_dict = {
            'datamenu': [["数据转换", "数据生成", "数据计算"], \
                          {"数据转换":lambda : self.command.data_cahange_grid(), \
                           "数据生成":lambda : self.command.data_generate_grid(), \
                           "数据计算":lambda : self.command.change() \
                           }],
            'jcosmenu':[["工作路径","bytecode","mask自动替换", "build.xml版本切换", "mask.cfg平台切换"], \
                          {"工作路径":lambda : self.command.rfu_cmd(), \
                           "bytecode":lambda : self.command.rfu_cmd(), \
                           "mask自动替换":lambda : self.command.rfu_cmd(), \
                           "build.xml版本切换":lambda : self.command.rfu_cmd(), \
                           "mask.cfg平台切换":lambda : self.command.rfu_cmd() \
                           }]
        }


        datamenu = Menu(self.menubar)
        for i in menu_dict["datamenu"][0]:
            datamenu.add_command(label=i, command=menu_dict["datamenu"][1][i])
        self.menubar.add_cascade(label='数据功能', menu=datamenu)

        jcosmenu = Menu(self.menubar)
        for i in menu_dict["jcosmenu"][0]:
            jcosmenu.add_command(label=i, command=menu_dict["jcosmenu"][1][i])
        self.menubar.add_cascade(label='Jcos功能', menu=jcosmenu)

        aboutmenu = Menu(self.menubar)
        aboutmenu.add_command(label='作者', command=self.command.author)
        aboutmenu.add_command(label='版权', command=self.command.about)
        self.menubar.add_cascade(label='关于', menu=aboutmenu)

    def create_text(self):
        self.text_in =  Text(self, fg="red", relief=GROOVE, height=10, width=80)
        self.text_out = Text(self, fg="red", relief=GROOVE, height=10, width=80)

    def create_in(self):
        self.num = StringVar()
        self.nument = Entry(self, textvariable=self.num,relief=FLAT,state='disable')
        self.din_dout = tk.Button(self, text="数据交换", command=self.shift_data)
        self.QUIT = tk.Button(self, text="退出", fg="red", command=root.destroy)

    def create_grid(self):
        rownum = 0
        self.text_in.grid(row=rownum, column=0, sticky='ewns', columnspan=10,rowspan=5)
        rownum+=5
        self.nument.grid(row=rownum, column=9, sticky='e')
        self.din_dout.grid(row=rownum, column=0, sticky='w')
        rownum += 1
        self.text_out.grid(row=rownum, column=0, sticky='ewns', columnspan=10,rowspan=5)
        rownum += 5
        self.QUIT.grid(row=rownum, column=9, sticky='e')

    def shownum(self):
        while(1):
            msg = self.text_in.get("0.0", "end")
            if len(msg) < 3:
                time.sleep(5)
                continue
            if '0X' in msg.upper() and ','in msg.upper():
                msg = msg.upper().replace("0X",'')
            p = re.compile('\w',flags=re.M|re.I|re.S)
            w = re.findall(p,msg)
            msg = ''.join(w)
            self.num.set(str(len(msg)) + "  " + str(len(msg) >> 1) + "  0x" + str(hex(len(msg) >> 1)).lstrip("0x").zfill(2))
            time.sleep(2)

    def shift_data(self):
        msgi = self.text_in.get("1.0", "end")
        msgo = self.text_out.get("1.0", "end")
        self.text_in.delete("1.0", "end")
        self.text_out.delete("1.0", "end")
        self.text_out.insert(INSERT, msgi.rstrip("\n"))
        self.text_in.insert(INSERT, msgo.rstrip("\n"))

root = tk.Tk()
app = Application(master=root)
app.mainloop()
