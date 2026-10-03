from pathlib import Path

from mcp.server import MCPServer

mcp = MCPServer("Product Demo")


@mcp.tool()
def get_product_count() -> int:
    """Return the number of products in products.csv."""
    csv_file = Path(__file__).resolve().parent.parent / "products.csv"

    with csv_file.open(encoding="utf-8-sig") as file:
        lines = file.readlines()

    # First line is the CSV header.
    return max(0, len(lines) - 1)

@mcp.tool()
def get_product(product_name: str) -> str:
    """Get product information from products.csv."""
    csv_file = Path(__file__).resolve().parent.parent / "products.csv"

    with csv_file.open(encoding="utf-8-sig", newline="") as file:
        products = __import__("csv").DictReader(file)

        for product in products:
            if product["product"].lower() == product_name.lower():
                return (
                    f"产品: {product['product']}\n"
                    f"成本: ${float(product['cost']):.2f}\n"
                    f"售价: ${float(product['price']):.2f}\n"
                    f"搜索量: {int(product['search_volume']):,}"
                )

    return f"没有找到产品: {product_name}"

@mcp.resource("product://catalog")
def get_product_catalog() -> str:
    """Return the product catalog from products.csv."""
    csv_file = Path(__file__).resolve().parent.parent / "products.csv"

    return csv_file.read_text(encoding="utf-8-sig")

@mcp.prompt()
def analyze_product(product_name: str) -> str:
    """Create a prompt for analyzing a product."""
    return (
        f"请分析产品 {product_name}。\n"
        f"请关注成本、售价、搜索量，并说明这些数据对产品分析的意义。"
    )

if __name__ == "__main__":
    mcp.run()
