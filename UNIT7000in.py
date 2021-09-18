import time
import pyvisa
from tkinter import *
from core.Core import api

class UNIT7000():
    def __init__(self,init_window_name):
        global txt
        txt=''
        self.H=0
        self.init_window_name = init_window_name
        self.rm = pyvisa.ResourceManager()

    #定义窗口
    def set_init_window1(self):
        #程序窗口
        self.init_window_name.title('UNI-T MSO7000自动化测试')
        self.init_window_name.geometry('1400x900+10+10')
        self.init_window_name['background'] = '#C6E2FF'

        #组件返回窗口
        s=LabelFrame(self.init_window_name,width=800,height=300)
        s.place(x=30,y=20)

        #返回窗口显示信息
        self.la = Label(s, text=txt, font=('黑体', "10"))
        self.la.place(x=10, y=10)

        #IP输入窗口
        lable_ip = Label(self.init_window_name, text='请输入设备IP地址', font=('黑体', "10"))
        lable_ip.place(x=900, y=50)

        global ip
        ip = StringVar()
        #IP文本输入框
        iput=Entry(self.init_window_name, textvariable=ip)
        iput.place(x=900, y=80, height=20,width=200)

        #IP连接按钮
        IP_BT=Button(self.init_window_name,text='连接测试',font=('黑体','10'),bg='white',command=self.ip_check)
        IP_BT.place(x=1150,y=79)

        #指令输入窗口
        lable_scpi = Label(self.init_window_name, text='请输入指令', font=('黑体', "10"))
        lable_scpi.place(x=900, y=200)

        global scpi
        # SCPI接收输入文本
        scpi = StringVar()

        # 指令输入框
        iput=Entry(self.init_window_name, textvariable=scpi)
        iput.place(x=900,y=240,height=30,width=300)

        #写入按钮
        scpi_wbt=Button(self.init_window_name,text='写 入',font=('黑体','10'),bg='white',command=self.scpi_wt_check)
        scpi_wbt.place(x=900,y=280)

        #查询按钮
        scpi_qbt = Button(self.init_window_name, text='查 询', font=('黑体', '10'), bg='white',command=self.scpi_qy_check)
        scpi_qbt.place(x=1040, y=280)

        #读取按钮
        scpi_bt = Button(self.init_window_name, text='读 取', font=('黑体', '10'), bg='white',command=self.scpi_rd_check)
        scpi_bt.place(x=970, y=280)

        #添加循环
        lc_bt=Button(self.init_window_name, text='添加列表', font=('黑体', '10'), bg='white',command=self.scpi_add)
        lc_bt.place(x=1110,y=280)

        global m
        m=StringVar()

        #循环输入框
        self.lc=Listbox(self.init_window_name,width=50, height=15,listvariable=m)
        self.lc.place(x=30, y=350)

        #删除按钮
        btn=Button(self.init_window_name, text="  删   除  ", command=lambda listbox=self.lc: listbox.delete(ANCHOR))
        btn.place(x=400,y=350)

        global sum
        #接收循环次数
        sum=StringVar()
        #循环次数输入框
        lct=Entry(self.init_window_name, textvariable=sum)
        lct.place(x=30,y=660,width=60, height=20)

        #循环标签
        ct=Label(self.init_window_name,text='请输入循环次数',font=('黑体', '10'))
        ct.place(x=30,y=630)

        #开始执行
        st=Button(self.init_window_name,text='开始循环',font=('黑体', '10'),command=self.scpi_xh)
        st.place(x=100,y=660)

        #顺序循环
        ord=Button(self.init_window_name,text='顺序循环',font=('黑体', '10'))
        ord.place(x=400,y=400)

        #接收指令的列表
        self.li=[]

    #得到用户输入ip
    def get_ip(self):
        g_ip=str(ip.get())
        return g_ip

    # 得到用户输入scpi指令
    def get_scpi(self):
        sp=str(scpi.get())
        return sp

    #返回ip检查的结果
    def ip_check(self):
        if self.H==False:
            self.la['text'] = api().ip_login(self.get_ip())
            if self.la['text']=='连接成功':
                self.H=True
        else:
            self.la['text']='连接成功'

    #返回SCPI命令写入是否成功命令
    def scpi_wt_check(self):
        if self.H==True:
            self.la['text'] = api().scpi_wt(self.get_scpi(),self.get_ip())
        else:
            self.la['text']='请先连接设备'

    def scpi_qy_check(self):
        if self.H==True:
            self.la['text'] = api().scpi_qy(self.get_scpi(),self.get_ip())
        else:
            self.la['text']='请先连接设备'

    def scpi_rd_check(self):
        if self.H==True:
            self.la['text'] = api().scpi_rd(self.get_scpi(),self.get_ip())
        else:
            self.la['text']='请先连接设备'

    def scpi_add(self):
        a=-1
        if self.H==True:
            self.li.append(self.get_scpi())
            a+=1
            self.lc.insert(a,'%s'%self.li[-1])
            self.la['text']='添加成功'
            print(m.get())
        else:
            self.la['text'] = '添加失败'

    def scpi_xh(self):
        li=[]
        xh=m.get()
        xh1=xh.split(',')
        cs=int(sum.get())
        for i in xh1:
            b = i.split('\'')[1]
            li.append(b)
        while (cs>0):
            cs-=1
            if self.H==True:
                for i in li:
                    self.la['text'] = api().scpi_qy(i, self.get_ip())
                    self.la.update()
                    time.sleep(1)
                    print(cs)
                    print(i)
            else:
                self.la['text']='请链接设备'
                break







