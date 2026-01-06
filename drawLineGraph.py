# -*- coding: utf-8 -*-
"""
Tkinter交互式折线图绘制工具
- 用户可选择单条或多条折线模式
- 支持自定义标题、坐标轴标签
- 支持自定义坐标轴显示范围
- 自动绘制并显示图例、网格
"""

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib


def parse_input(data_str):
    """
    将输入字符串解析为浮点数列表
    支持分隔符：英文逗号, 中文逗号，空格，换行
    """
    data_str = data_str.replace("，", ",")
    data_str = data_str.replace("\n", " ")
    data_str = data_str.replace(",", " ")
    return [float(i) for i in data_str.split() if i.strip() != ""]


def apply_axis_limits():
    """读取用户输入的坐标范围（可选）"""
    try:
        x_min = float(entry_xmin.get()) if entry_xmin.get().strip() else None
        x_max = float(entry_xmax.get()) if entry_xmax.get().strip() else None
        y_min = float(entry_ymin.get()) if entry_ymin.get().strip() else None
        y_max = float(entry_ymax.get()) if entry_ymax.get().strip() else None
        return (x_min, x_max, y_min, y_max)
    except ValueError:
        messagebox.showerror("错误", "坐标范围输入有误，请输入数字！")
        return (None, None, None, None)


def draw_single_line():
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 或者 ['Microsoft YaHei']
    matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    try:
        x = parse_input(entry_x.get())
        y = parse_input(entry_y.get())

        if len(x) != len(y):
            messagebox.showerror("错误", "X 和 Y 长度必须一致！")
            return

        plt.figure(figsize=(8, 5), dpi=120)
        plt.plot(x, y, linestyle='-', color='#1f77b4', linewidth=2, marker='o', label="系列")
        plt.title(entry_title.get())
        plt.xlabel(entry_xlabel.get())
        plt.ylabel(entry_ylabel.get())
        plt.legend(loc="best")
        plt.grid(True, linestyle='--', alpha=0.4)

        # 应用坐标范围
        x_min, x_max, y_min, y_max = apply_axis_limits()
        if x_min is not None or x_max is not None:
            plt.xlim(x_min, x_max)
        if y_min is not None or y_max is not None:
            plt.ylim(y_min, y_max)

        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("错误", f"数据格式有问题: {e}")


def draw_multi_line():
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 或者 ['Microsoft YaHei']
    matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    try:
        n = int(entry_num.get())
        series = {}
        for i in range(n):
            name = simple_entries[i][0].get()
            x_data = simple_entries[i][1].get()
            y_data = simple_entries[i][2].get()
            x = parse_input(x_data)
            y = parse_input(y_data)
            if len(x) != len(y):
                messagebox.showerror("错误", f"{name} 的 X 和 Y 长度不一致！")
                return
            series[name] = (x, y)

        plt.figure(figsize=(8, 5), dpi=120)
        line_styles = ['-', '--', '-.', ':']
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

        for i, (name, (sx, sy)) in enumerate(series.items()):
            style = line_styles[i % len(line_styles)]
            color = colors[i % len(colors)]
            plt.plot(sx, sy, linestyle=style, color=color, linewidth=2, marker='o', label=name)

        plt.title(entry_title.get())
        plt.xlabel(entry_xlabel.get())
        plt.ylabel(entry_ylabel.get())
        plt.legend(loc="best")
        plt.grid(True, linestyle='--', alpha=0.4)

        # 应用坐标范围
        x_min, x_max, y_min, y_max = apply_axis_limits()
        if x_min is not None or x_max is not None:
            plt.xlim(x_min, x_max)
        if y_min is not None or y_max is not None:
            plt.ylim(y_min, y_max)

        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("错误", f"数据格式有问题: {e}")


def create_multi_entries():
    global simple_entries
    for widget in frame_multi.winfo_children():
        widget.destroy()
    simple_entries = []
    try:
        n = int(entry_num.get())
        for i in range(n):
            tk.Label(frame_multi, text=f"第 {i + 1} 条折线名称:").grid(row=i * 3, column=0)
            name_entry = tk.Entry(frame_multi, width=20)
            name_entry.grid(row=i * 3, column=1)

            tk.Label(frame_multi, text="X 数据:").grid(row=i * 3 + 1, column=0)
            x_entry = tk.Entry(frame_multi, width=40)
            x_entry.grid(row=i * 3 + 1, column=1)

            tk.Label(frame_multi, text="Y 数据:").grid(row=i * 3 + 2, column=0)
            y_entry = tk.Entry(frame_multi, width=40)
            y_entry.grid(row=i * 3 + 2, column=1)

            simple_entries.append((name_entry, x_entry, y_entry))
    except:
        messagebox.showerror("错误", "请输入正确的折线条数！")


# 主窗口
root = tk.Tk()
root.title("交互式折线图绘制工具")

# 标题与坐标轴标签
tk.Label(root, text="图表标题:").grid(row=0, column=0)
entry_title = tk.Entry(root, width=40)
entry_title.grid(row=0, column=1)

tk.Label(root, text="X轴标签:").grid(row=1, column=0)
entry_xlabel = tk.Entry(root, width=40)
entry_xlabel.grid(row=1, column=1)

tk.Label(root, text="Y轴标签:").grid(row=2, column=0)
entry_ylabel = tk.Entry(root, width=40)
entry_ylabel.grid(row=2, column=1)

# 坐标范围输入
tk.Label(root, text="X最小值:").grid(row=3, column=0)
entry_xmin = tk.Entry(root, width=10)
entry_xmin.grid(row=3, column=1)

tk.Label(root, text="X最大值:").grid(row=3, column=2)
entry_xmax = tk.Entry(root, width=10)
entry_xmax.grid(row=3, column=3)

tk.Label(root, text="Y最小值:").grid(row=4, column=0)
entry_ymin = tk.Entry(root, width=10)
entry_ymin.grid(row=4, column=1)

tk.Label(root, text="Y最大值:").grid(row=4, column=2)
entry_ymax = tk.Entry(root, width=10)
entry_ymax.grid(row=4, column=3)

# 单条折线输入
tk.Label(root, text="单条折线 X 数据:").grid(row=5, column=0)
entry_x = tk.Entry(root, width=40)
entry_x.grid(row=5, column=1)

tk.Label(root, text="单条折线 Y 数据:").grid(row=6, column=0)
entry_y = tk.Entry(root, width=40)
entry_y.grid(row=6, column=1)

btn_single = tk.Button(root, text="绘制单条折线", command=draw_single_line)
btn_single.grid(row=7, column=1, pady=5)

# 多条折线输入
tk.Label(root, text="折线条数:").grid(row=8, column=0)
entry_num = tk.Entry(root, width=10)
entry_num.grid(row=8, column=1)

btn_create = tk.Button(root, text="生成输入框", command=create_multi_entries)
btn_create.grid(row=8, column=2)

frame_multi = tk.Frame(root)
frame_multi.grid(row=9, column=0, columnspan=4, pady=10)

btn_multi = tk.Button(root, text="绘制多条折线", command=draw_multi_line)
btn_multi.grid(row=10, column=1, pady=5)

root.mainloop()
