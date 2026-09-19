# FXI（凝血因子XI）数据分析项目

## 项目简介
本项目以凝血因子 XI（Factor XI，FXI）为主题，使用 Python、Pandas、Matplotlib 和 Jupyter Notebook 对整理后的教学数据进行分析。

## 学习目标
- 了解 FXI 的基本结构与功能。
- 使用 Pandas 读取和统计 CSV 数据。
- 使用 Matplotlib 进行可视化。
- 使用 Jupyter Notebook 展示结果。
- 使用 Git 进行版本管理。

## 项目结构
```text
work/
├── README.md
├── analysis.ipynb
├── analysis.py
├── data.csv
├── requirements.txt
└── .gitignore
```

## 环境安装
建议 Python 3.10 或更高版本。
```bash
pip install -r requirements.txt
```

## 运行
```bash
python analysis.py
jupyter notebook
```
打开 analysis.ipynb 后依次运行代码单元。

## 科学背景
FXI 是血浆中的凝血因子，以同源二聚体形式存在。人类经典 FXI 蛋白由 625 个氨基酸组成，每个亚基包含四个 Apple 结构域和一个丝氨酸蛋白酶结构域。FXI 被激活后形成 FXIa，可激活凝血因子 IX，从而参与凝血过程。

FXI 缺乏是一种罕见的出血性疾病，历史上也称为血友病 C 或 Rosenthal 综合征。出血表现存在个体差异，不能仅凭 FXI 水平判断实际出血风险。

FXI 也是抗血栓研究关注的靶点之一。相关研究正在探索 FXI/FXIa 抑制与血栓预防、正常止血之间的关系。

> data.csv 为课程作业使用的教学整理数据，不代表真实患者数据，也不能用于临床诊断。

## 可复现性
项目不依赖网络数据。安装 requirements.txt 中的依赖后，直接运行 analysis.py 或 analysis.ipynb 即可重复分析流程。

## Git 版本管理
```bash
git init
git add .
git commit -m "Initial FXI analysis project"
git tag -a v1.0.0 -m "FXI analysis version 1.0.0"
git push origin main
git push origin v1.0.0
```

## 参考资料
1. NCBI Gene: F11 coagulation factor XI。
2. UniProt: Coagulation factor XI, P03951。
3. Factor XI deficiency 相关综述。
4. FXI/FXIa 抑制剂相关研究。

## 许可证
本项目仅用于学习和课程作业，不用于医学诊断或临床决策。
