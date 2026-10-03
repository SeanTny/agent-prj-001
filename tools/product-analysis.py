import csv
from pathlib import Path

# 获取项目根目录
project_dir = Path(__file__).resolve().parent.parent

# 读取产品数据
csv_file = project_dir / "products.csv"

with csv_file.open(encoding="utf-8-sig", newline="") as file:
    products = csv.DictReader(file)

    for product in products:
        name = product["product"]
        cost = float(product["cost"])
        price = float(product["price"])

        profit = price - cost
        margin = profit / price * 100

        print(f"产品: {name}")
        print(f"毛利: ${profit:.2f}")
        print(f"毛利率: {margin:.2f}%")
        print("--------------------")
