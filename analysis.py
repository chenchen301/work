from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(ROOT / "data.csv")

print("=== FXI 数据 ===")
print(df.to_string(index=False))

print("\n=== 各主题数量 ===")
summary = df["topic"].value_counts()
print(summary)

print("\n=== FXI 结构与功能 ===")
print(df[df["topic"].isin(["Structure", "Function"])]
      [["topic", "indicator", "value", "unit"]]
      .to_string(index=False))

summary.to_csv(OUT / "topic_summary.csv", header=["count"])

summary.plot(kind="bar", title="FXI资料各主题数量")
plt.xlabel("主题")
plt.ylabel("条目数")
plt.tight_layout()
plt.savefig(OUT / "topic_summary.png", dpi=150)
plt.close()

print("\n结果已保存到 output/")
