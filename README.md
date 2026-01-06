# 交互式折线图绘制工具

一个基于 **Python Tkinter + Matplotlib** 的图形化小工具，支持用户通过界面输入数据并绘制折线图。  
适合快速可视化实验数据、性能曲线或其他需要折线展示的场景。

---

## ✨ 功能特性
- **单条折线模式**：输入一组 X/Y 数据即可绘制。
- **多条折线模式**：支持多条折线，用户可自定义名称、数据，自动生成图例。
- **灵活的数据输入**：兼容多种分隔符：
  - 英文逗号 `,`
  - 中文逗号 `，`
  - 空格
  - 换行符
- **自定义图表信息**：
  - 标题
  - X/Y 坐标轴标签
  - 可选的坐标范围限制（不输入则默认自动范围）
- **中文支持**：标题、坐标轴标签、图例均可输入中文，避免乱码。
- **图表美化**：自动添加网格、图例，支持多种线型和颜色。

---

## 🖥️ 使用方法
1. 启动程序后，在界面中输入：
   - 图表标题、X/Y 坐标轴标签
   - 数据（单条或多条折线）
   - 可选的坐标范围
2. 点击按钮绘制折线图，图表会弹出显示。
3. 多条折线模式下，先输入折线条数并生成输入框，再填写每条折线的数据。

---

## 📦 打包为可执行文件
使用 [PyInstaller](https://pyinstaller.org/) 打包：
```bash
pyinstaller --onefile --windowed line_chart_app.py
```

# Interactive Line Chart Drawing Tool

A graphical tool based on **Python Tkinter + Matplotlib** that allows users to input data through a user interface and generate line charts.  
It is suitable for quickly visualizing experimental data, performance curves, or any scenarios that require line chart representation.

---

## ✨ Features
- **Single Line Mode**: Input one set of X/Y data to draw a line chart.
- **Multi-Line Mode**: Support multiple lines; users can customize names and data, with legends generated automatically.
- **Flexible Data Input**: Compatible with multiple delimiters:
  - English comma `,`
  - Chinese comma `，`
  - Space
  - Newline
- **Customizable Chart Information**:
  - Title
  - X/Y axis labels
  - Optional axis range limits (leave blank for automatic range)
- **Chinese Support**: Titles, axis labels, and legends can include Chinese characters without encoding issues.
- **Chart Beautification**: Automatic grid and legend, with support for multiple line styles and colors.

---

## 🖥️ Usage
1. Launch the program and enter:
   - Chart title, X/Y axis labels
   - Data (single or multiple lines)
   - Optional axis ranges
2. Click the button to draw the line chart; the chart will pop up.
3. In multi-line mode, first enter the number of lines and generate input fields, then fill in the data for each line.

---

## 📦 Packaging as Executable
Use [PyInstaller](https://pyinstaller.org/) to package:
```bash
pyinstaller --onefile --windowed line_chart_app.py
```
