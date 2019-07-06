#-*- coding: utf-8 -*-
# __author__ = 'Omega'
#created on 20190706 by omega for practice
#If any advice let me know---------emai: dk2086@126.com  

import tkinter as TK
# 主窗口
root = TK.Tk( )                     # 创建TK实例
root.title("King's Caculator")      # 设置窗口的显示名字
root.resizable(0,0)                 # 设置主窗口的宽度和高度是否可以通过鼠标进行拉伸改变，此处设置为不能
root.geometry('320x420')            # 这里设置主窗口的初始尺寸，因为我们在上面设定了主窗口大小  不可变，因此这个尺寸也就是主窗口一直不变的尺寸了

# 此处继续编写其他GUI部分或者回调函数）
result = TK.StringVar( )               # 用来显示结果的可变文本
equation = TK.StringVar( )             # 用来显示算式的可变文本
result.set(' ')                        # 赋初始值
equation.set('0')                      # 赋初始值


# 结果显示框
show_uresult = TK.Label(root,bg='white',fg = 'black',font =('Arail','15'),bd='0',textvariable =equation,anchor='se')
show_dresult = TK.Label(root,bg='white',fg = 'black',font = ('Arail','30'),bd='0',textvariable=result,anchor='se')
show_uresult.place(x='10',y='10',width='300',height='50')


root.mainloop( )

