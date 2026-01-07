# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import matplotlib


class LinePlotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("交互式折线图绘制工具")

        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False

        # ====== 标题与坐标轴标签 ======
        tk.Label(root, text="图表标题:").grid(row=0, column=0, sticky="w")
        self.entry_title = tk.Entry(root, width=40)
        self.entry_title.grid(row=0, column=1, sticky="w")

        tk.Label(root, text="X轴标签:").grid(row=1, column=0, sticky="w")
        self.entry_xlabel = tk.Entry(root, width=40)
        self.entry_xlabel.grid(row=1, column=1, sticky="w")

        tk.Label(root, text="Y轴标签:").grid(row=2, column=0, sticky="w")
        self.entry_ylabel = tk.Entry(root, width=40)
        self.entry_ylabel.grid(row=2, column=1, sticky="w")

        # ====== 坐标范围输入 ======
        tk.Label(root, text="X最小值:").grid(row=3, column=0, sticky="w")
        self.entry_xmin = tk.Entry(root, width=10)
        self.entry_xmin.grid(row=3, column=1, sticky="w")

        tk.Label(root, text="X最大值:").grid(row=3, column=2, sticky="w")
        self.entry_xmax = tk.Entry(root, width=10)
        self.entry_xmax.grid(row=3, column=3, sticky="w")

        tk.Label(root, text="Y最小值:").grid(row=4, column=0, sticky="w")
        self.entry_ymin = tk.Entry(root, width=10)
        self.entry_ymin.grid(row=4, column=1, sticky="w")

        tk.Label(root, text="Y最大值:").grid(row=4, column=2, sticky="w")
        self.entry_ymax = tk.Entry(root, width=10)
        self.entry_ymax.grid(row=4, column=3, sticky="w")

        # ====== 单条折线输入 ======
        tk.Label(root, text="单条折线 X 数据:").grid(row=5, column=0, sticky="w")
        self.entry_x = tk.Entry(root, width=40)
        self.entry_x.grid(row=5, column=1, sticky="w")

        tk.Label(root, text="单条折线 Y 数据:").grid(row=6, column=0, sticky="w")
        self.entry_y = tk.Entry(root, width=40)
        self.entry_y.grid(row=6, column=1, sticky="w")

        tk.Label(root, text="线条样式:").grid(row=7, column=0, sticky="w")
        self.combo_style = ttk.Combobox(root, values=['-', '--', '-.', ':'], width=10)
        self.combo_style.grid(row=7, column=1, sticky="w")
        self.combo_style.set('-')  # 默认值

        tk.Label(root, text="颜色:").grid(row=8, column=0, sticky="w")
        self.combo_color = ttk.Combobox(root,
                                        values=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                                                'red', 'green', 'blue', 'black'],
                                        width=10)
        self.combo_color.grid(row=8, column=1, sticky="w")
        self.combo_color.set('#1f77b4')  # 默认值

        self.btn_single = tk.Button(root, text="绘制单条折线", command=self.draw_single_line)
        self.btn_single.grid(row=9, column=1, pady=5, sticky="w")

        # ====== 多条折线输入 ======
        tk.Label(root, text="折线条数:").grid(row=10, column=0, sticky="w")
        self.entry_num = tk.Entry(root, width=10)
        self.entry_num.grid(row=10, column=1, sticky="w")

        self.btn_create = tk.Button(root, text="生成输入框", command=self.create_multi_entries)
        self.btn_create.grid(row=10, column=2, sticky="w")

        self.frame_multi = tk.Frame(root)
        self.frame_multi.grid(row=11, column=0, columnspan=4, pady=10, sticky="w")

        self.btn_multi = tk.Button(root, text="绘制多条折线", command=self.draw_multi_line)
        self.btn_multi.grid(row=12, column=1, pady=5, sticky="w")

        self.simple_entries = []

    @staticmethod
    def parse_input(data_str):
        data_str = (data_str or "").replace("，", ",").replace("\n", " ").replace(",", " ")
        return [float(i) for i in data_str.split() if i.strip() != ""]

    def apply_axis_limits(self):
        try:
            x_min = float(self.entry_xmin.get()) if self.entry_xmin.get().strip() else None
            x_max = float(self.entry_xmax.get()) if self.entry_xmax.get().strip() else None
            y_min = float(self.entry_ymin.get()) if self.entry_ymin.get().strip() else None
            y_max = float(self.entry_ymax.get()) if self.entry_ymax.get().strip() else None
            return (x_min, x_max, y_min, y_max)
        except ValueError:
            messagebox.showerror("错误", "坐标范围输入有误，请输入数字！")
            return (None, None, None, None)

    def draw_single_line(self):
        try:
            x = self.parse_input(self.entry_x.get())
            y = self.parse_input(self.entry_y.get())
            if len(x) != len(y):
                messagebox.showerror("错误", "X 和 Y 长度必须一致！")
                return

            style = self.combo_style.get() or '-'
            color = self.combo_color.get() or '#1f77b4'

            plt.figure(figsize=(8, 5), dpi=120)
            plt.plot(x, y, linestyle=style, color=color, linewidth=2, marker='o', label="系列")
            plt.title(self.entry_title.get())
            plt.xlabel(self.entry_xlabel.get())
            plt.ylabel(self.entry_ylabel.get())
            plt.legend(loc="best")
            plt.grid(True, linestyle='--', alpha=0.4)

            x_min, x_max, y_min, y_max = self.apply_axis_limits()
            if x_min is not None or x_max is not None:
                plt.xlim(x_min, x_max)
            if y_min is not None or y_max is not None:
                plt.ylim(y_min, y_max)

            plt.tight_layout()
            plt.show()
        except Exception as e:
            messagebox.showerror("错误", f"数据格式有问题: {e}")

    def create_multi_entries(self):
        for widget in self.frame_multi.winfo_children():
            widget.destroy()
        self.simple_entries = []
        try:
            n = int(self.entry_num.get())
            for i in range(n):
                base = i * 5
                tk.Label(self.frame_multi, text=f"第 {i + 1} 条折线名称:").grid(row=base, column=0, sticky="w")
                name_entry = tk.Entry(self.frame_multi, width=20)
                name_entry.grid(row=base, column=1, sticky="w")

                tk.Label(self.frame_multi, text="X 数据:").grid(row=base + 1, column=0, sticky="w")
                x_entry = tk.Entry(self.frame_multi, width=40)
                x_entry.grid(row=base + 1, column=1, sticky="w")

                tk.Label(self.frame_multi, text="Y 数据:").grid(row=base + 2, column=0, sticky="w")
                y_entry = tk.Entry(self.frame_multi, width=40)
                y_entry.grid(row=base + 2, column=1, sticky="w")

                tk.Label(self.frame_multi, text="线条样式:").grid(row=base + 3, column=0, sticky="w")
                style_combo = ttk.Combobox(self.frame_multi, values=['-', '--', '-.', ':'], width=10)
                style_combo.grid(row=base + 3, column=1, sticky="w")
                style_combo.set('-')

                tk.Label(self.frame_multi, text="颜色:").grid(row=base + 4, column=0, sticky="w")
                color_combo = ttk.Combobox(self.frame_multi,
                                           values=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                                                   'red', 'green', 'blue', 'black'],
                                           width=10)
                color_combo.grid(row=base + 4, column=1, sticky="w")
                color_combo.set('#1f77b4')

                # 保存每条折线的输入控件
                self.simple_entries.append((name_entry, x_entry, y_entry, style_combo, color_combo))
        except ValueError:
            messagebox.showerror("错误", "请输入正确的折线条数！")

    def draw_multi_line(self):
        try:
            n = int(self.entry_num.get())
            if n != len(self.simple_entries):
                messagebox.showerror("错误", "请先点击“生成输入框”，并确保条数一致！")
                return

            plt.figure(figsize=(8, 5), dpi=120)

            for i in range(n):
                name = self.simple_entries[i][0].get().strip() or f"系列{i+1}"
                x = self.parse_input(self.simple_entries[i][1].get())
                y = self.parse_input(self.simple_entries[i][2].get())
                style = self.simple_entries[i][3].get() or '-'
                color = self.simple_entries[i][4].get() or '#1f77b4'

                if len(x) != len(y):
                    messagebox.showerror("错误", f"{name} 的 X 和 Y 长度不一致！")
                    return

                plt.plot(x, y, linestyle=style, color=color, linewidth=2, marker='o', label=name)

            plt.title(self.entry_title.get())
            plt.xlabel(self.entry_xlabel.get())
            plt.ylabel(self.entry_ylabel.get())
            plt.legend(loc="best")
            plt.grid(True, linestyle='--', alpha=0.4)

            # 应用坐标范围
            x_min, x_max, y_min, y_max = self.apply_axis_limits()
            if x_min is not None or x_max is not None:
                plt.xlim(x_min, x_max)
            if y_min is not None or y_max is not None:
                plt.ylim(y_min, y_max)

            plt.tight_layout()
            plt.show()
        except Exception as e:
            messagebox.showerror("错误", f"数据格式有问题: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = LinePlotApp(root)
    root.mainloop()
