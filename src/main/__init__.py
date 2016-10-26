



# coding = utf-8
# 本程序用于计算寝室内共用电表

import tkinter
from tkinter import *
import pymysql
from distutils.cmd import Command


# gui部分
root = tkinter.Tk()

# def outputletter():
#     print('out')
# 
# start = tkinter.Button(root,text='a')
# 
# tkinter.Button(root, text="外观装饰边界附近的标签", width=19,relief=GROOVE,bg="red").pack()
# 
# tkinter.Button(root, text="设置按钮状态",width=21,state=DISABLED).pack()
# 
# tkinter.Button(root, text = "输出文本", command = outputletter).pack()
# 
# tr_text = tkinter.Text(root)
# tr_text.insert(1.0, '这个是可输入的文本框')
# tr_text.pack()
# 
# tr_label = tkinter.Label(root,text='本周已工作')
# tr_label.pack()


# 第一页
me_contain = PanedWindow()
me_contain.pack(fill = BOTH, expand = 1)
left = Label(me_contain,text = "姓名")
me_contain.add(left)



# start.pack()

root.mainloop()



# 获取本次数据
# 包括：电网费用 电网电量 每个人的本次室内电表读数


