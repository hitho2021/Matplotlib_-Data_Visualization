# Description:  Matplotlib Scatter for Product and Order quantity
# Version: 1.0
# Last Modified Date: 2026-09-23
# Created By: Hit

import pandas as pd
import matplotlib.pyplot as plt

#Read Data
df = pd.read_csv("C:\Python\SalesData.csv")
#Set the Data Format
df["Product_Name"] = df["Product_Name"].astype(str)


#x = df[['Product_ID']]
x = df["Product_Name"]
y = df[['Order_Quantity']]


plt.scatter(x,y)

#Set chart Labels
plt.xlabel('Product')
plt.ylabel('Quantity in Order')
plt.title('Scatter for Product and Order quantity')

plt.show()

