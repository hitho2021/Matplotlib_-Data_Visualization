# Description:  Matplotlib Linear Regression
# Version: 1.0
# Last Modified Date: 2026-09-23
# Created By: Hit
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import date

#Read Data
df = pd.read_csv("C:\Python\SalesData.csv")

#Set the Data Format
df["Order_Date"] = pd.to_datetime(df["Order_Date"], format="%d/%m/%Y")

# Keep one record per order
df = df.groupby("Order_ID", as_index=False).agg({ "Order_Date": "first", "Total_Amount": "first" })

# Calculate average order amount for each date (regression only)
daily_avg = df.groupby("Order_Date", as_index=False)["Total_Amount"].mean()
# Sort daily averages by date
daily_avg = daily_avg.sort_values("Order_Date")
#Use the sanple data will get the same result, but it show seperate the predict and scatter dataset
#daily_avg = df

# Convert dates to numbers for regression
x = daily_avg["Order_Date"].map(lambda d: d.toordinal()).to_frame()
y = daily_avg[["Total_Amount"]]

model = LinearRegression()
model.fit(x,y)
linear_regressor = LinearRegression()
linear_regressor.fit(x,y)
Y_pred = linear_regressor.predict(x)



plt.scatter(df["Order_Date"],df["Total_Amount"])
plt.plot(daily_avg["Order_Date"], Y_pred, color='red')
plt.xlabel("Order Date")
plt.ylabel("Total Amount")

#Format X-axis and Y-axis 
y_max = max(df["Total_Amount"].max(), Y_pred.max())
plt.ylim(bottom=0, top=y_max * 1.1)

# Display date only (DD/MM/YYYY)
import matplotlib.dates as mdates
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))


plt.show()


