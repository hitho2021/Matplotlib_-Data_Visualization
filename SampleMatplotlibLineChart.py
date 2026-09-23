# Description: Matplotlib Line Chart for sales by date
# Version: 1.0
# Last Modified Date: 2026-09-22
# Created By: Hit
import pandas as pd
import matplotlib.pyplot as plt

#Read Data
df = pd.read_csv("C:\Python\SalesData.csv")
#Set the String to DateTime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

#Create New Field to sum of the Sales by Date
pdf=df.groupby(['Order_Date']).Sub_Total.sum().reset_index(name ='Total_Sales')

sdf= pdf.sort_values(by=['Order_Date'],ascending=True)

x = sdf[['Order_Date']]
y = sdf[['Total_Sales']]


plt.plot(x,y)

#Set the Axis Label
plt.xlabel('Date')
plt.ylabel('Total Sales')
#Set the Chart Name
plt.title('Line chart for sales by date')

#Format X-axis and Y-axis 
y_max = sdf["Total_Sales"].max()
plt.ylim(bottom=0, top=y_max * 1.1)

# Display date only (DD/MM/YYYY)
import matplotlib.dates as mdates
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))

plt.show()

