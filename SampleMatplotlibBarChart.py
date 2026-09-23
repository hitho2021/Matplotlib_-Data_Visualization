# Description:  Matplotlib Bar Chart for sales by products
# Version: 1.0
# Last Modified Date: 2026-09-22
# Created By: Hit

import pandas as pd
import matplotlib.pyplot as plt

#Read Data
df = pd.read_csv("C:\Python\SalesData.csv")
#Set the Data Format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Product_Name"] = df["Product_Name"].astype(str)

#Create New Field to sum of the Sales by Product
pdf=df.groupby(['Product_Name']).Sub_Total.sum().reset_index(name ='Total_Sales')

#Sort the data for Display Purpose
sdf= pdf.sort_values(by=['Product_Name'],ascending=True)

sdf.plot.bar(x='Product_Name',y='Total_Sales', rot=1)

#Set chart Labels
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.title('Bar chart for sales by product')

plt.show()

