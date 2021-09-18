from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import time
from UI.UNIT7000in import UNIT7000

class Main:
    # 用户登录状态标识
    user_stste = False

# 登录界面：
class Login():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

     #定义窗口
    def set_init_window(self):
        self.init_window_name.title('UNI-T MSO7000')
        self.init_window_name.geometry('1120x710+10+10')

        #背景图片
        global photo
        global photo1
        photo=PhotoImage(file=r'../img/UNIT3.gif')
        lable=Label(self.init_window_name, image=photo)
        lable.place(x=0, y=0)
        photo1=PhotoImage(file=r'../img/UNIT2.gif')
        lable1=Label(self.init_window_name,image=photo1)
        lable1.place(x=0,y=0)

        #用户接收参数
        self.User=StringVar()

        #密码接收参数
        self.Pw=StringVar()

        # 用户名
        lable_user=Label(self.init_window_name, text='用户名', font=('黑体', "16"))
        lable_user.place(x=700, y=300)

        #用户名输入窗口
        entry1=Entry(self.init_window_name, textvariable=self.User)
        entry1.place(x=800, y=300, height=30)

        #密码
        lable_pw=Label(self.init_window_name,text='密  码',font=('黑体','16'))
        lable_pw.place(x=700, y=350)

        #密码输入窗口
        entry2=Entry(self.init_window_name, textvariable=self.Pw)
        entry2.place(x=800, y=350, height=30)

        #按钮登录
        BUTT_LOGIN=Button(self.init_window_name,text='登 录',font=('黑体','14'),bg='white',command=self.check_password)
        BUTT_LOGIN.place(x=800,y=400)

        #按钮退出
        BUTT_ESC=Button(self.init_window_name,text="退出",font=('黑体','14'),bg='white',command=self.init_window_name.destroy)
        BUTT_ESC.place(x=900, y=400)

        #按钮技术支持
        BUTT_SUP=Button(self.init_window_name,text="技术支持",font=("黑体","14"),bg='#FFC125',command=self.Aup_hzy)
        BUTT_SUP.place(x=800,y=450)

    #技术支持
    def Aup_hzy(self):
        global photo2,top,photo3

        #用户名
        top=Toplevel()
        top.title('感谢技术支持')
        top.geometry('850x650+150+100')
        photo2=PhotoImage(file=r'../img/zfb.gif')
        lable2=Label(top, image=photo2)
        lable2.place(x=0, y=0)

        #微信转账
        photo3=PhotoImage(file=r'../img/wx.gif')
        lable3=Label(top, image=photo3)
        lable3.place(x=420, y=0)

        #返回按钮
        all_font=font.Font(family='宋体', size=20, weight=font.BOLD)
        retur=Button(top, text='返回', font=all_font, command=top.destroy)
        retur.place(x=425, y=550)

        #QQ联系方式
        Label(top, text='QQ:1140948966', font=20).place(x=30, y=530)

    #账户核对
    def check_password(self):
        User_Name="gh_hzy"
        Pass_word="UNIT123.."
        if self.User.get() == User_Name and self.Pw.get() == Pass_word:
            # 如果登录成功，修改用户状态标识
            Main.user_stste=True
            # 退出登录窗口
            self.init_window_name.destroy()
            time.sleep(1)
            UNIT7000(Tk()).set_init_window1()
        else:
            # 登录失败提示
            messagebox.showinfo('登录', '用户名或密码错误,请联系管理员：何曾益')
a=Tk()
Login(a).set_init_window()
a.mainloop()

