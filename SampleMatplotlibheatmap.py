# Description:  Matplotlib Heatmap for Order Date and number of Product sales
# Version: 1.0
# Last Modified Date: 2026-09-23
# Created By: Hit

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Read Data
df = pd.read_csv("C:\Python\SalesData.csv")
#Set the Data Format
df["Order_Date"] = pd.to_datetime(df["Order_Date"], format="%d/%m/%Y")
df["Product_Name"] = df["Product_Name"].astype(str)

df_order_date = sorted(df["Order_Date"].unique())

print (df_order_date)

# Create summary table
heatmap_data = df.pivot_table(
    index="Order_Date",
    columns="Product_Name",
    values="Order_Quantity",
    aggfunc="sum",
    fill_value=0
)

heatmap_data = heatmap_data.reindex(df_order_date)
# Format Y-axis dates as DD/MM/YYYY
heatmap_data.index = heatmap_data.index.strftime("%d/%m/%Y")

# Create heatmap
plt.figure(figsize=(8, 4))

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=",",
    cmap="YlOrRd",
    linewidths=0.5
)

#Set chart Labels
plt.title("Sales Heatmap Order Date and Sold Product Quantity")
plt.xlabel("Product")
plt.ylabel("Order Date")

plt.tight_layout()
plt.show()

