# Description: Matplotlib Pie Chart for sales by products
# Version: 1.0
# Last Modified Date: 2026-09-23
# Created By: Hit
import pandas as pd
import matplotlib.pyplot as plt

#Read Data
df = pd.read_csv("C:\Python\SalesData.csv")
#Set the String to DateTime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Product_Name"] = df["Product_Name"].astype(str)

#Create New Field to sum of the Sales by Product and percentage in all Sales
pdf=df.groupby(['Product_Name']).Sub_Total.sum().reset_index(name ='Total_Sales')
pdf['percentage'] = (pdf['Total_Sales'] / pdf['Total_Sales'].sum()) * 100

#Sort the data for Display Purpose
sdf= pdf.sort_values(by=['Product_Name'],ascending=True)

labels = sdf[['Product_Name']]
values = sdf[['percentage']]

sdf.groupby(['Product_Name']).sum().plot( kind='pie', y='Total_Sales', autopct='%1.0f%%', shadow=True)

#Set chart Labels
plt.title('Pie chart for sales by product category')

plt.show()
