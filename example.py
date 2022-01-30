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
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value=2)
        self.var_4 = tk.IntVar(value=12)
        self.var_5 = tk.IntVar(value=1)
        self.var_6 = tk.IntVar(value=1)
        # self.var_5 = tk.DoubleVar(value=75.0)

        # Create widgets :)
        self.setup_widgets()

    # Combobox event
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
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        # Show images
        global img, qrb_img  # 防止变量作用域超出范围，导致图片不显示
        img = Image.open("images/clear.png")
        qrb_img = ImageTk.PhotoImage(img)
        self.image_label = Label(self.image_frame, image=qrb_img, width=570, height=570)
        self.image_label.grid(
            row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew"
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
        self.spinbox_2 = ttk.Spinbox(self.widgets_frame, from_=0, to=100, increment=0.1)
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

        # Button save
        self.button = ttk.Button(self.widgets_frame, text="保存")
        self.button.grid(row=11, column=0, padx=5, pady=10, sticky="nsew")

        # Button reset
        self.button = ttk.Button(self.widgets_frame, text="重置")
        self.button.grid(row=12, column=0, padx=5, pady=10, sticky="nsew")


# ------------------------------modify here---------------------------------------

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
            columns=(1, 2),
            height=10,
        )
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        # Treeview columns
        self.treeview.column("#0", anchor="w", width=120)
        self.treeview.column(1, anchor="w", width=120)
        self.treeview.column(2, anchor="w", width=120)

        # Treeview headings
        self.treeview.heading(1, text="章节", anchor="center")
        # self.treeview.heading(1, text="Column 2", anchor="center")
        # self.treeview.heading(2, text="Column 3", anchor="center")

        # Define treeview data
        treeview_data = [
            ("", 1, "Parent", ("Item 1", "Value 1")),
            (1, 2, "Child", ("Subitem 1.1", "Value 1.1")),
            (1, 3, "Child", ("Subitem 1.2", "Value 1.2")),
            (1, 4, "Child", ("Subitem 1.3", "Value 1.3")),
            (1, 5, "Child", ("Subitem 1.4", "Value 1.4")),
            ("", 6, "Parent", ("Item 2", "Value 2")),
            (6, 7, "Child", ("Subitem 2.1", "Value 2.1")),
            (6, 8, "Sub-parent", ("Subitem 2.2", "Value 2.2")),
            (8, 9, "Child", ("Subitem 2.2.1", "Value 2.2.1")),
            (8, 10, "Child", ("Subitem 2.2.2", "Value 2.2.2")),
            (8, 11, "Child", ("Subitem 2.2.3", "Value 2.2.3")),
            (6, 12, "Child", ("Subitem 2.3", "Value 2.3")),
            (6, 13, "Child", ("Subitem 2.4", "Value 2.4")),
            ("", 14, "Parent", ("Item 3", "Value 3")),
            (14, 15, "Child", ("Subitem 3.1", "Value 3.1")),
            (14, 16, "Child", ("Subitem 3.2", "Value 3.2")),
            (14, 17, "Child", ("Subitem 3.3", "Value 3.3")),
            (14, 18, "Child", ("Subitem 3.4", "Value 3.4")),
            ("", 19, "Parent", ("Item 4", "Value 4")),
            (19, 20, "Child", ("Subitem 4.1", "Value 4.1")),
            (19, 21, "Sub-parent", ("Subitem 4.2", "Value 4.2")),
            (21, 22, "Child", ("Subitem 4.2.1", "Value 4.2.1")),
            (21, 23, "Child", ("Subitem 4.2.2", "Value 4.2.2")),
            (21, 24, "Child", ("Subitem 4.2.3", "Value 4.2.3")),
            (19, 25, "Child", ("Subitem 4.3", "Value 4.3")),
        ]

        # Insert treeview data
        for item in treeview_data:
            self.treeview.insert(
                parent=item[0], index="end", iid=item[1], text=item[2], values=item[3]
            )
            if item[0] == "" or item[1] in {8, 21}:
                self.treeview.item(item[1], open=True)  # Open parents

        # Select and scroll
        self.treeview.selection_set(10)
        self.treeview.see(7)


class QRP:
    def __init__(self, color_list=cmp.get_color_list(0), split_point=cmp.get_split_point(0), k_list=cmp.get_k_list(0),
                 mag=cmp.get_mag(0), tp=0, mtd=0):
        self._color_list = color_list
        self._split_point = split_point
        self._k_list = k_list
        self._mag = mag
        self._tp = tp
        self._mtd = mtd
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
