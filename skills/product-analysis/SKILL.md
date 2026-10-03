---
name: product-analysis
description: 分析产品数据，包括成本、售价、毛利和毛利率。
---

# 产品分析

当任务要求分析 products.csv 中的产品时：


1. 读取项目中的 `products.csv`。
2. 使用项目中的 `product-demo` MCP Server 获取和查询产品数据。
3. 优先使用 MCP Server 提供的工具，不要直接运行 `tools/product-analysis.py`。
4. 根据 MCP 返回的数据进行分析。
5. 使用 Python 工具输出的毛利和毛利率。
6. 对计算结果进行解释。
7. 不要自己猜测计算结果。
8. 如果数据缺失，要明确说明。
