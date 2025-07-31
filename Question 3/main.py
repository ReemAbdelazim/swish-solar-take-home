"""
FastAPI app that generates and returns a PNG line plot
of synthetic daily sales data for multiple products.
"""

import io
import random

from fastapi import FastAPI, Response
import pandas as pd
import matplotlib.pyplot as plt


app = FastAPI()

def generate_sales_data():
    """
    Generate synthetic daily sales data for 4 products over a 6-month period.

    Returns:
        pd.DataFrame: A DataFrame with columns ['date', 'product', 'quantity'].
                        Each row represents one day's sales for one product.
    """
    date_range = pd.date_range(start="2024-01-01", periods=180, freq="D")
    products = ["A", "B", "C", "D"]
    data = {
        "date": [d for d in date_range for _ in products],
        "product": products * len(date_range),
        "quantity": [random.randint(5, 50) for _ in range(len(products) * len(date_range))]
    }
    return pd.DataFrame(data)

@app.get("/sales/trend")
def get_sales_trend():
    """
    Endpoint that returns a PNG line plot showing daily sales trends per product.

    The function generates synthetic sales data, pivots it to get quantity per product per day,
    plots a time series with one line per product, and returns the chart as a PNG image.

    Returns:
        fastapi.Response: A PNG image of the sales trend line chart.
    """
    df = generate_sales_data()

    pivot_df = df.pivot_table(index="date", columns="product", values="quantity", aggfunc="sum")

    plt.figure(figsize=(10, 6))
    for product in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[product], label=f"Product {product}")

    plt.title("Daily Sales Quantity per Product")
    plt.xlabel("Date")
    plt.ylabel("Quantity Sold")
    plt.legend()
    plt.tight_layout()

    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    plt.close()
    img_bytes.seek(0)

    return Response(content=img_bytes.read(), media_type="image/png")
