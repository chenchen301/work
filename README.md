# FXI（凝血因子XI）数据分析项目

## 1. 项目简介
本项目以凝血因子 XI（Factor XI，FXI）为主题。
项目使用 Python、Pandas、Matplotlib 和 Jupyter Notebook。
数据来自整理后的教学数据，不是患者临床数据。
项目用于学习数据处理、统计和可视化。
同时用于练习 Git 的版本管理方法。

## 2. 学习目标
- 了解 FXI 的基本结构。
- 了解 FXI 的基本功能。
- 认识 FXI 缺乏的相关概念。
- 了解 FXI 研究的主要方向。
- 学习读取 CSV 文件。
- 学习使用 Pandas 处理数据。
- 学习进行简单的数据统计。
- 学习使用 Matplotlib 绘图。
- 学习使用 Jupyter Notebook。
- 学习使用 Git 管理项目。

## 3. 项目结构
```text
work/
├── README.md
├── analysis.ipynb
├── analysis.py
├── data.csv
├── requirements.txt
└── .gitignore
```

## 4. 文件说明
README.md 用来介绍项目。
analysis.ipynb 用来展示 Jupyter 分析过程。
analysis.py 用来执行完整的数据分析。
data.csv 保存 FXI 教学数据。
requirements.txt 保存 Python 依赖。
.gitignore 用来排除不需要提交的文件。

## 5. 环境要求
建议使用 Python 3.10 或更高版本。
项目可以在常见的 Windows、macOS 和 Linux 环境中运行。
运行前需要安装 Python。
还需要安装项目所使用的第三方库。

## 6. 环境安装
打开终端并进入项目目录。
然后运行下面的命令：

```bash
pip install -r requirements.txt
```

安装完成后即可运行分析程序。
如果使用 Jupyter，也需要保证 jupyter 已经正确安装。

## 7. 运行 Python 程序
在项目目录运行：

```bash
python analysis.py
```

程序首先读取 data.csv。
然后显示完整的 FXI 数据。
接着统计四个主题的条目数量。
程序还会显示结构和功能相关信息。
最后生成分析结果文件。

## 8. 使用 Jupyter Notebook
运行：

```bash
jupyter notebook
```

打开 analysis.ipynb。
按照从上到下的顺序运行代码单元。
Notebook 会显示原始数据。
之后会显示主题统计结果。
还会显示结构和功能信息。
最后使用柱状图进行简单可视化。

## 9. 数据主题
本项目的数据分成四个主题。
第一个主题是 Structure。
第二个主题是 Function。
第三个主题是 Disease。
第四个主题是 Research。

Structure 主要描述 FXI 的结构信息。
Function 主要描述 FXI 的凝血功能。
Disease 主要描述 FXI 缺乏相关内容。
Research 主要描述 FXI 的研究方向。

## 10. FXI 基本知识
FXI 是凝血系统中的一种蛋白质。
FXI 在血浆中主要以同源二聚体形式存在。
人类经典 FXI 蛋白由 625 个氨基酸组成。
每个亚基包含四个 Apple 结构域。
每个亚基还包含一个丝氨酸蛋白酶结构域。
FXI 被激活后形成 FXIa。
FXIa 可以激活凝血因子 IX。
因此 FXI 参与凝血过程。

## 11. FXI 缺乏
FXI 缺乏是一种罕见的出血性疾病。
历史上也称为血友病 C。
Rosenthal 综合征也是相关名称。
患者的出血表现存在较大的个体差异。
部分患者可能在手术或创伤后出现出血。
实验室检查中 aPTT 可能延长。
但是不能只根据单项实验室指标判断个体实际情况。

## 12. FXI 与研究
FXI 是目前凝血研究中的一个重要对象。
研究人员关注 FXI 与血栓形成之间的关系。
FXI 和 FXIa 也是药物研究的潜在靶点。
相关研究会同时关注抗血栓作用和出血风险。
本项目只介绍基本概念。
本项目不涉及药物剂量或治疗建议。

## 13. 数据分析方法
程序使用 Pandas 读取 CSV 文件。
使用 value_counts() 统计不同主题。
使用布尔筛选提取结构和功能数据。
使用 groupby() 对主题进行分组。
使用 size() 统计每组数据数量。
使用 Matplotlib 绘制柱状图。
图像保存到 output 文件夹。
统计结果也保存到 output 文件夹。

## 14. 可复现性
项目使用固定的 data.csv。
分析程序不会从网络下载数据。
因此运行时不需要访问外部数据库。
只要安装相同的依赖即可重新运行。
Python 程序和 Notebook 使用相同的数据来源。
这使项目具有较好的可复现性。

## 15. Git 版本管理
项目使用 Git 保存不同版本。
常见操作如下：

```bash
git init
git add .
git commit -m "Initial FXI analysis project"
```

创建版本标签：

```bash
git tag -a v1.0.0 -m "FXI analysis version 1.0.0"
```

上传主分支：

```bash
git push origin main
```

上传标签：

```bash
git push origin v1.0.0
```

## 16. 项目结果
运行程序后可以看到四个 FXI 数据主题。
可以比较不同主题的条目数量。
可以查看 FXI 的结构与功能资料。
还可以通过柱状图直观观察数据。
这些结果主要用于练习数据分析方法。

## 17. 注意事项
data.csv 是教学整理数据。
它不是临床数据库。
其中的数据不能代表真实患者。
项目中的医学内容只用于学习。
不能根据本项目进行疾病诊断。
不能根据本项目制定治疗方案。

## 18. 参考资料
1. NCBI Gene: F11 coagulation factor XI。
2. UniProt: Coagulation factor XI, P03951。
3. Factor XI deficiency 相关医学综述。
4. FXI/FXIa 抑制剂相关研究资料。

## 19. 项目总结
本项目将 FXI 知识与 Python 数据分析结合。
通过 CSV 文件保存结构化数据。
通过 Pandas 完成数据读取和统计。
通过 Matplotlib 完成简单可视化。
通过 Jupyter Notebook 展示分析结果。
通过 Git 完成项目版本管理。
整个项目可以在本地重新运行。

## 20. 许可证
本项目仅用于学习和课程作业。
不用于医学诊断或临床决策。
