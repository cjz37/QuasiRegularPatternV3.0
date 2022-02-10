from tkinter import *
import tkinter as tk
from tkinter import ttk

import cv2 as cv
from PIL import Image, ImageTk
from lib import colormap as cmp
from lib import mathMoudel as mm
from lib import createImg as ci
from tkinter import messagebox


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        self.combo_list = ["颜色模式1", "颜色模式2", "颜色模式3", "颜色模式4", "颜色模式5", "颜色模式6", "颜色模式7", "颜色模式8"]

        # Create control variables
        self.var_0 = tk.StringVar()  # 文件名
        self.var_1 = tk.IntVar()  # 图像大小
        self.var_2 = tk.DoubleVar()  # 迭代次数
        self.var_3 = tk.StringVar()  # 颜色模式
        self.var_4 = tk.IntVar(value=12)  # 迭代次数
        self.var_5 = tk.IntVar(value=1)  # X轴偏移
        self.var_6 = tk.IntVar(value=1)  # Y轴偏移

        # Create widgets :)
        self.setup_widgets()

    # get param filename pic_size iter_time color_mode and create pic
    def createevent(self, event):
        self.var_0 = self.entry.get()
        self.var_1 = self.spinbox_1.get()
        self.var_2 = self.spinbox_2.get()
        self.var_3 = self.combobox.get()

        w = self.spinbox_1.get()
        q = self.spinbox_2.get()
        s = self.scale_1.get()
        xmin = self.scale_2.get()
        ymin = self.scale_2.get()

        print('w={}, q={}, s={}, xmin={}, ymin={}'.format(w, q, s, xmin, ymin))

        if q and w:
            if w == '图像大小' or w == '请输入图像大小' or w == '不得超过2048':
                self.spinbox_1.delete(0, "end")
                self.spinbox_1.insert(0, '请输入图像大小')
                self.spinbox_1.focus()
            elif q == '迭代次数' or q == '请输入迭代次数' or q == '不得超过28':
                self.spinbox_2.delete(0, "end")
                self.spinbox_2.insert(0, '请输入迭代次数')
                self.spinbox_2.focus()
            else:
                w = int(w)
                q = float(q)
                if w <= 0 or w > 2048:
                    self.spinbox_1.delete(0, "end")
                    self.spinbox_1.insert(0, '不得超过2048')
                    self.spinbox_1.focus()
                elif q <= 0 or q > 28:
                    self.spinbox_2.delete(0, "end")
                    self.spinbox_2.insert(0, '不得超过28')
                    self.spinbox_2.focus()
                else:
                    qrp.create(q=q, s=s, w=w-1, xmin=xmin, ymin=ymin)

                    global img, qrp_img
                    img = Image.open('images/temp.png')
                    size = 570, 570
                    img.thumbnail(size)
                    qrp_img = ImageTk.PhotoImage(img)
                    self.image_label.config(image=qrp_img)

    # reset param
    def resetevent(self, event):
        self.spinbox_1.set(value=600)
        self.spinbox_2.set(value=3)
        self.scale_1.set(value=12)
        self.scale_2.set(value=1)
        self.scale_3.set(value=1)

    # save image
    def saveevent(self, event):
        global qrp
        filename = self.entry.get()
        if filename and filename != '文件名' and filename != '请输入文件名':
            qrp.save(filename)
            messagebox.showinfo(title='信息提示', message='保存成功！')
        else:
            self.entry.delete(0, "end")
            self.entry.insert(0, '请输入文件名')
            self.entry.focus()

    # Combobox event color mode
    def cmbevent(self, event):
        if self.combo_list[0] == self.combobox.get():
            qrp.set_colormap(0, 0, 0)
        elif self.combo_list[1] == self.combobox.get():
            qrp.set_colormap(0, 1, 0)
        elif self.combo_list[2] == self.combobox.get():
            qrp.set_colormap(1, 2, 1)
        elif self.combo_list[3] == self.combobox.get():
            qrp.set_colormap(2, 3, 1)
        elif self.combo_list[4] == self.combobox.get():
            qrp.set_colormap(0, 4, 0)
        elif self.combo_list[5] == self.combobox.get():
            qrp.set_colormap(4, 5, 1)
        elif self.combo_list[6] == self.combobox.get():
            qrp.set_colormap(5, 6, 0)
        elif self.combo_list[7] == self.combobox.get():
            qrp.set_colormap(6, 7, 0)

    # Treeview event
    def tvevent(self, event):
        item = self.treeview.selection()
        if item:
            txt = self.treeview.item(item[0], 'text')
            if txt == '2.1.1':
                self.setparam(0, 0, 0, 0, 0, 0)
            elif txt == '2.1.2':
                self.setparam(0, 0, 1, 0, 0, 0)
            elif txt == '3.1.1.1':
                self.setparam(0, 1, 2, 1, 0, 0)
            elif txt == '3.1.1.2':
                self.setparam(0, 2, 3, 1, 0, 0)
            elif txt == '3.1.2.1':
                self.setparam(0, 0, 0, 0, 0, 1)
            elif txt == '3.1.2.2':
                self.setparam(0, 0, 0, 0, 1, 1)
            elif txt == '3.1.2.3':
                self.setparam(0, 3, 8, 1, 0, 0, False)
            elif txt == '3.2.1':
                self.setparam(0, 0, 0, 0, 0, 2)
            elif txt == '3.2.2':
                self.setparam(0, 0, 0, 0, 1, 2)
            elif txt == '3.3.1':
                self.setparam(1, 0, 4, 0, 0, 0)
            elif txt == '3.3.2':
                self.setparam(2, 0, 4, 0, 0, 0)
            elif txt == '4.1.1':
                self.setparam(0, 4, 5, 1, 0, 0)
            elif txt == '4.2.1':
                self.setparam(0, 0, 0, 0, 1, 0)
            elif txt == '4.2.2':
                self.setparam(0, 0, 0, 0, 2, 0)
            elif txt == '4.2.3':
                self.setparam(0, 0, 0, 0, 3, 0)
            elif txt == '4.2.4':
                self.setparam(0, 0, 0, 0, 4, 0)
            elif txt == '4.3.1':
                self.setparam(0, 0, 0, 0, 5, 0)
            elif txt == '4.3.2':
                self.setparam(0, 0, 0, 0, 6, 0)
            elif txt == '4.3.3':
                self.setparam(0, 0, 0, 0, 7, 0)
            elif txt == '4.3.4':
                self.setparam(0, 0, 0, 0, 8, 0)
            elif txt == '4.3.5':
                self.setparam(0, 0, 0, 0, 9, 0)
            elif txt == '5.1.1.1':
                self.setparam(0, 0, 0, 0, 10, 0)
            elif txt == '5.1.1.2':
                self.setparam(0, 0, 0, 0, 11, 0)
            elif txt == '5.1.1.3':
                self.setparam(0, 0, 0, 0, 12, 0)
            elif txt == '5.1.2.1':
                self.setparam(0, 0, 0, 0, 13, 0)
            elif txt == '5.2.1.1':
                self.setparam(0, 0, 0, 0, 14, 0)
            elif txt == '5.2.1.2':
                self.setparam(0, 0, 0, 0, 15, 0)
            elif txt == '5.2.1.3':
                self.setparam(0, 0, 0, 0, 16, 0)
            elif txt == '5.2.1.4':
                self.setparam(0, 0, 0, 0, 17, 0)
            elif txt == '5.2.1.5':
                self.setparam(0, 0, 0, 0, 18, 0)
            elif txt == '5.2.1.6':
                self.setparam(0, 0, 0, 0, 19, 0)
            elif txt == '5.2.1.7':
                self.setparam(0, 0, 0, 0, 20, 0)
            elif txt == '5.2.1.8':
                self.setparam(0, 0, 0, 0, 21, 0)
            elif txt == '5.2.2.1':
                self.setparam(0, 0, 0, 0, 22, 0)
            elif txt == '5.2.2.2':
                self.setparam(0, 0, 0, 0, 23, 0)
            elif txt == '5.2.2.3':
                self.setparam(0, 0, 0, 0, 24, 0)
            elif txt == '5.2.3.1':
                self.setparam(0, 0, 0, 0, 25, 0)
            elif txt == '5.2.3.2':
                self.setparam(0, 0, 0, 0, 26, 0)
            elif txt == '5.2.4.1':
                self.setparam(0, 0, 0, 0, 27, 0)
            elif txt == '5.2.4.2':
                self.setparam(0, 0, 0, 0, 28, 0)
            elif txt == '5.2.4.3':
                self.setparam(0, 0, 0, 0, 29, 0)
            elif txt == '5.2.4.4':
                self.setparam(0, 0, 0, 0, 30, 0)
            elif txt == '5.2.4.5':
                self.setparam(0, 0, 0, 0, 31, 0)
            elif txt == '5.3.1.1':
                self.setparam(0, 5, 6, 0, 32, 0)
            elif txt == '5.3.1.2':
                self.setparam(0, 5, 6, 0, 33, 0)
            elif txt == '5.3.1.3':
                self.setparam(0, 5, 6, 0, 34, 0)
            elif txt == '5.3.1.4':
                self.setparam(0, 5, 6, 0, 35, 0)
            elif txt == '5.3.1.5':
                self.setparam(0, 5, 6, 0, 36, 0)
            elif txt == '5.3.1.6':
                self.setparam(0, 5, 6, 0, 37, 0)
            elif txt == '5.3.1.7':
                self.setparam(0, 5, 6, 0, 38, 0)
            elif txt == '5.3.2.1':
                self.setparam(0, 5, 6, 0, 39, 0)
            elif txt == '5.3.2.2':
                self.setparam(0, 5, 6, 0, 40, 0)
            elif txt == '5.3.2.3':
                self.setparam(0, 5, 6, 0, 41, 0)
            elif txt == '5.3.2.4':
                self.setparam(0, 5, 6, 0, 42, 0)
            elif txt == '5.3.3.1':
                self.setparam(0, 5, 6, 0, 43, 0)
            elif txt == '5.3.3.2':
                self.setparam(0, 5, 6, 0, 44, 0)
            elif txt == '5.3.3.3':
                self.setparam(0, 5, 6, 0, 45, 0)
            elif txt == '5.3.3.4':
                self.setparam(0, 5, 6, 0, 46, 0)
            elif txt == '5.3.4.1':
                self.setparam(0, 5, 6, 0, 47, 0)
            elif txt == '5.3.4.2':
                self.setparam(0, 5, 6, 0, 48, 0)
            elif txt == '5.3.4.3':
                self.setparam(0, 5, 6, 0, 49, 0)
            elif txt == '5.3.4.4':
                self.setparam(0, 5, 6, 0, 50, 0)
            elif txt == '5.3.4.5':
                self.setparam(0, 5, 6, 0, 51, 0)

    # set param after selection
    def setparam(self, color_list_index, split_point_index, k_list_index, mag_index, tp, mtd, is_set_combobox=True):
        global qrp
        qrp = QRP(color_list=cmp.get_color_list(color_list_index), split_point=cmp.get_split_point(split_point_index),
                  k_list=cmp.get_k_list(k_list_index), mag=cmp.get_mag(mag_index), tp=tp, mtd=mtd)
        if is_set_combobox:
            self.combobox.set(self.combo_list[k_list_index])

    # Update label image density
    def getscale_1(self, text):
        self.label_1.config(text="图像密度: " + str(self.var_4.get()))

    # Update label x offset
    def getscale_2(self, text):
        self.label_2.config(text="X轴偏移: " + str(self.var_5.get()))

    # Update label y offset
    def getscale_3(self, text):
        self.label_3.config(text="Y轴偏移: " + str(self.var_6.get()))

    def setup_widgets(self):
        # Create a Frame for the images
        self.image_frame = ttk.LabelFrame(self, text="生成图像", padding=(20, 10))
        self.image_frame.grid(
            row=0, column=0, padx=(10, 10), pady=(20, 0), sticky="nsew"
        )

        # Create a Frame for show images
        global img, qrp_img  # 防止变量作用域超出范围，导致图片不显示
        img = Image.open("images/clear.png")
        qrp_img = ImageTk.PhotoImage(img)
        self.image_label = Label(self.image_frame, image=qrp_img, width=570, height=570)
        self.image_label.grid(
            row=0, column=0, sticky="nsew"
        )

        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # Entry filename
        self.entry = ttk.Entry(self.widgets_frame)
        self.entry.insert(0, "文件名")
        self.entry.grid(row=0, column=0, padx=5, pady=(25, 10), sticky="ew")

        # Spinbox image size
        self.spinbox_1 = ttk.Spinbox(self.widgets_frame, from_=500, to=1080, increment=100)
        self.spinbox_1.insert(0, "图像大小")
        self.spinbox_1.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

        # Spinbox iteration time
        self.spinbox_2 = ttk.Spinbox(self.widgets_frame, from_=0, to=100, increment=1)
        self.spinbox_2.insert(0, "迭代次数")
        self.spinbox_2.grid(row=2, column=0, padx=5, pady=10, sticky="ew")

        # Combobox color model
        self.combobox = ttk.Combobox(self.widgets_frame, values=self.combo_list)
        self.combobox.current(0)
        self.combobox.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

        # bing combobox event
        self.combobox.bind("<<ComboboxSelected>>", self.cmbevent)

        # label image density
        self.label_1 = ttk.Label(self.widgets_frame, text="图像密度: " + str(self.var_4.get()))
        self.label_1.grid(row=4, column=0, padx=10, pady=(10, 5), sticky="ew")

        # Scale image density
        self.scale_1 = ttk.Scale(
            self.widgets_frame,
            from_=1,
            to=128,
            value=12,
            variable=self.var_4,
            command=self.getscale_1,
        )
        self.scale_1.grid(row=5, column=0, padx=(10, 10), pady=(5, 10), sticky="ew")

        # label x offset
        self.label_2 = ttk.Label(self.widgets_frame, text="X轴偏移: " + str(self.var_5.get()))
        self.label_2.grid(row=6, column=0, padx=10, pady=(10, 5), sticky="ew")

        # Scale x offset
        self.scale_2 = ttk.Scale(
            self.widgets_frame,
            from_=-600,
            to=600,
            variable=self.var_5,
            command=self.getscale_2,
        )
        self.scale_2.grid(row=7, column=0, padx=(10, 10), pady=(5, 10), sticky="ew")

        # label y offset
        self.label_3 = ttk.Label(self.widgets_frame, text="Y轴偏移: " + str(self.var_6.get()))
        self.label_3.grid(row=8, column=0, padx=10, pady=(10, 5), sticky="ew")

        # Scale y offset
        self.scale_3 = ttk.Scale(
            self.widgets_frame,
            from_=-600,
            to=600,
            variable=self.var_6,
            command=self.getscale_3,
        )
        self.scale_3.grid(row=9, column=0, padx=(10, 10), pady=(5, 10), sticky="ew")

        # Accentbutton create
        self.accentbutton = ttk.Button(
            self.widgets_frame, text="生成", style="Accent.TButton"
        )
        self.accentbutton.grid(row=10, column=0, padx=5, pady=10, sticky="nsew")

        self.accentbutton.bind('<ButtonRelease-1>', self.createevent)

        # Button save
        self.button_save = ttk.Button(self.widgets_frame, text="保存")
        self.button_save.grid(row=11, column=0, padx=5, pady=10, sticky="nsew")

        self.button_save.bind('<ButtonRelease-1>', self.saveevent)

        # Button reset
        self.button_reset = ttk.Button(self.widgets_frame, text="重置")
        self.button_reset.grid(row=12, column=0, padx=5, pady=10, sticky="nsew")

        self.button_reset.bind('<ButtonRelease-1>', self.resetevent)


# ------------------------------tree view---------------------------------------

        # Panedwindow
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

        # Pane #1
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.treeview = ttk.Treeview(
            self.pane_1,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            columns=0,
            height=10,
        )
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        # Treeview columns
        self.treeview.column("#0", anchor="w", width=120)
        self.treeview.column(0, anchor="w", width=260)

        # Treeview headings
        self.treeview.heading(0, text="              章节", anchor="w")

        # Define treeview data
        treeview_data = [
            ("", 1, "第二章", "准规则斑图基本图形的生成方法"),
            (1, 2, "2.1.1", "基本图形生成"),
            (1, 3, "2.1.2", "两色化处理"),
            ("", 4, "第三章", "准规则斑图模型的色彩变化方法"),
            (4, 5, "3.1", "QBcolor模式等高线变量的控制方法"),
            (5, 6, "3.1.1", "等高线的切割方式"),
            (6, 7, "3.1.1.1", "等高线的切割方式之一"),
            (6, 8, "3.1.1.2", "等高线的切割方式之二"),
            (5, 9, "3.1.2", "等高线变量的赋值方式"),
            (9, 10, "3.1.2.1", "等高线变量的赋值方式之一"),
            (9, 11, "3.1.2.2", "等高线变量的赋值方式之二"),
            (9, 12, "3.1.2.3", "等高线变量的赋值方式之三"),
            (4, 13, "3.2", "RGB模式等高线变量的控制方法"),
            (13, 14, "3.2.1", "等高线变量的控制方式之一"),
            (13, 15, "3.2.2", "等高线变量的控制方式之二"),
            (4, 16, "3.3", "切割等高线的RGB色彩值赋值方法"),
            (16, 17, "3.3.1", "任意切割等高线的具体方法之一"),
            (16, 18, "3.3.2", "任意切割等高线的具体方法之二"),
            ("", 19, "第四章", "准规则斑图的参数变化方法"),
            (19, 20, "4.1", "参数q的非整数取值变化方法"),
            (20, 21, "4.1.1", "q值的非整数取值及其图形生成"),
            (19, 22, "4.2", "参数i的变化方法"),
            (22, 23, "4.2.1", "参数i的设计一"),
            (22, 24, "4.2.2", "参数i的设计二"),
            (22, 25, "4.2.3", "参数i的设计三"),
            (22, 26, "4.2.4", "参数i的设计四"),
            (19, 27, "4.3", "其他参数的变化方法"),
            (27, 28, "4.3.1", "其他参数设计一"),
            (27, 29, "4.3.2", "其他参数设计二"),
            (27, 30, "4.3.3", "其他参数设计三"),
            (27, 31, "4.3.4", "其他参数设计四"),
            (27, 32, "4.3.5", "其他参数设计五"),
            ("", 33, "第五章", "准规则斑图的函数变换方法"),
            (33, 34, "5.1", "绝对值函数变换"),
            (34, 35, "5.1.1", "基本模型的绝对值函数变换"),
            (35, 36, "5.1.1.1", "基本模型的整体变换"),
            (35, 37, "5.1.1.2", "基本模型的局部变换"),
            (35, 38, "5.1.1.3", "基本模型的复合变换"),
            (34, 39, "5.1.2", "结合参数变化的绝对值函数变换"),
            (39, 40, "5.1.2.1", "与参数变化结合的变换"),
            (33, 41, "5.2", "三角函数变换"),
            (41, 42, "5.2.1", "基本模型整体的三角函数变换"),
            (42, 43, "5.2.1.1", "基本模型整体简单变换一"),
            (42, 44, "5.2.1.2", "基本模型整体简单变换二"),
            (42, 45, "5.2.1.3", "基本模型整体简单变换三"),
            (42, 46, "5.2.1.4", "基本模型整体简单变换四"),
            (42, 47, "5.2.1.5", "基本模型整体简单变换五"),
            (42, 48, "5.2.1.6", "基本模型整体简单变换六"),
            (42, 49, "5.2.1.7", "基本模型整体简单变换七"),
            (42, 50, "5.2.1.8", "基本模型整体简单变换八"),
            (41, 51, "5.2.2", "基本模型的局部三角函数变换"),
            (51, 52, "5.2.2.1", "基本模型的局部函数变换之一"),
            (51, 53, "5.2.2.2", "基本模型的局部函数变换之二"),
            (51, 54, "5.2.2.3", "基本模型的局部函数变换之三"),
            (41, 55, "5.2.3", "基本模型的自变量三角函数变换"),
            (55, 56, "5.2.3.1", "自变量三角函数变换之一"),
            (55, 57, "5.2.3.2", "自变量三角函数变换之二"),
            (41, 58, "5.2.4", "整体、局部以及自变量之间的复合变换"),
            (58, 59, "5.2.4.1", "整体与局部复合变换之一"),
            (58, 60, "5.2.4.2", "整体与局部复合变换之二"),
            (58, 61, "5.2.4.3", "整体与自变量之间的复合变换之一"),
            (58, 62, "5.2.4.4", "整体与自变量之间的复合变换之二"),
            (58, 63, "5.2.3.5", "局部与自变量之间的复合变换之一"),
            (33, 64, "5.3", "幂函数变换"),
            (64, 65, "5.3.1", "基本模型的整体变换"),
            (65, 66, "5.3.1.1", "基本模型的整体变换一"),
            (65, 67, "5.3.1.2", "基本模型的整体变换二"),
            (65, 68, "5.3.1.3", "基本模型的整体变换三"),
            (65, 69, "5.3.1.4", "基本模型的整体变换四"),
            (65, 70, "5.3.1.5", "基本模型的整体变换五"),
            (65, 71, "5.3.1.6", "基本模型的整体变换六"),
            (65, 72, "5.3.1.7", "基本模型的整体变换七"),
            (64, 73, "5.3.2", "基本模型的局部变换"),
            (73, 74, "5.3.2.1", "基本模型的局部变换一"),
            (73, 75, "5.3.2.2", "基本模型的局部变换二"),
            (73, 76, "5.3.2.3", "基本模型的局部变换三"),
            (73, 77, "5.3.2.4", "基本模型的局部变换四"),
            (64, 78, "5.3.3", "基本模型的自变量变换"),
            (78, 79, "5.3.3.1", "基本模型的自变量变换一"),
            (78, 80, "5.3.3.2", "基本模型的自变量变换二"),
            (78, 81, "5.3.3.3", "基本模型的自变量变换三"),
            (78, 82, "5.3.3.4", "基本模型的自变量变换四"),
            (64, 83, "5.3.4", "基本模型的整体、局部与自变量之间的复合变换"),
            (83, 84, "5.3.4.1", "整体与局部的复合变换"),
            (83, 85, "5.3.4.2", "整体与自变量的复合变换"),
            (83, 86, "5.3.4.3", "局部与自变量的复合变换一"),
            (83, 87, "5.3.4.4", "局部与自变量的复合变换二"),
            (83, 88, "5.3.4.5", "整体、局部与自变量同时进行的复合变换"),

        ]

        # Insert treeview data
        for item in treeview_data:
            self.treeview.insert(
                parent=item[0], index="end", iid=item[1], text=item[2], values=item[3]
            )
            if item[0] == "":
                self.treeview.item(item[1], open=True)  # Open parents

        # Select and scroll
        self.treeview.selection_set(2)
        # self.treeview.see(7)

        # Click event
        self.treeview.bind('<ButtonRelease-1>', self.tvevent)


class QRP:
    def __init__(self, color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
                 mag=cmp.get_mag(0), tp=0, mtd=0):
        self._color_list = color_list
        self._split_point = split_point
        self._k_list = k_list
        self._mag = mag
        self._tp = tp  # index of func: get_*_set(h\k\color)
        self._mtd = mtd  # method
        self._cImg = None

    def create(self, q, s, w, xmin, ymin):
        # 生成色彩索引
        if 0 == self._mtd:
            color_index = cmp.build_color_index(split_point=self._split_point, k_list=self._k_list, mag=self._mag)
            h_set = mm.list_of_get_h_set[self._tp](q=q, s=s, w=w, xmin=xmin, ymin=ymin, mag=self._mag)
            self._cImg = ci.draw_image_h_set(w=w, color_index=color_index, mag=self._mag, color_list=self._color_list,
                                             split_point=self._split_point, h_set=h_set)
        elif 1 == self._mtd:
            k_set = mm.list_of_get_k_set[self._tp](q=q, s=s, w=w, xmin=xmin, ymin=ymin)
            self._cImg = ci.draw_image_k_set(w=w, color_list=self._color_list, k_set=k_set)
        elif 2 == self._mtd:
            color_set = mm.list_of_get_color_set[self._tp](q=q, s=s, w=w, xmin=xmin, ymin=ymin)
            self._cImg = ci.draw_image_color_set(w=w, color_set=color_set)

    def save(self, name):
        path = 'images/save/' + name + '.png'
        cv.imwrite(path, self._cImg)

    def set_colormap(self, split_point_index, k_list_index, mag_index):
        self._split_point = cmp.get_split_point(split_point_index)
        self._k_list = cmp.get_k_list(k_list_index)
        self._mag = cmp.get_mag(mag_index)


if __name__ == "__main__":
    qrp = QRP()

    root = tk.Tk()
    root.title("准规则斑图")
    root.resizable(False, False)

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()
