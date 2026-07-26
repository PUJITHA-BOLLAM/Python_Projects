import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("ECommerce_Sales_Dataset.xlsx",sheet_name="ECommerceData")
#Data information
'''print(df.head(5))
print(df.shape)
print(df.info())
print(df.dtypes)

#Data Cleaning
print(df.isnull().sum())
print(df.duplicated().sum())
df=df.drop_duplicates()
df["Price"]=df["Price"].fillna(df["Price"].mean())
df["Discount"]=df["Discount"].fillna(df["Discount"].mean())
df["Profit"]=df["Profit"].fillna(df["Profit"].mean())
print(df.isnull().sum())
df["Order_Date"]=pd.to_datetime(df["Order_Date"],errors="coerce")
print(df["Order_Date"].isnull().sum())
df=df.dropna(subset=["Order_Date"])
print(df.info())

#Exploratory Data Analysis

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df.shape[0]
average = total_sales / total_orders

print("====== SALES OVERVIEW ======")
print(f"Total Sales         : ₹{total_sales:.2f}")
print(f"Total Profit        : ₹{total_profit:.2f}")
print(f"Total Orders        : {total_orders}")
print(f"Average Order Value : ₹{average:.2f}")

#Category wise Total Sales
sale=df.groupby("Category")["Sales"].sum()
sale=sale.sort_values(ascending=False)
print(sale)
print("Best Selling Category:",sale.idxmax())
print("Best Selling Category's Total Sales:",sale.max())

#Region wise Sales
region_sale=df.groupby("Region")["Sales"].sum()
region_sale=region_sale.sort_values(ascending=False)
print(region_sale)
print("Best-performing Region:",region_sale.idxmax())
print("Total sales of that region:",region_sale.max())

#Best selling products
product_sale=df.groupby("Product")["Sales"].sum()
product_sale=product_sale.sort_values(ascending=False)
print("=====Top-5 Products=====")
print(product_sale.head(5))
print("Best Selling product:",product_sale.idxmax())
print("Sales of best selling product:",product_sale.max())
'''

#VISUALIZATION
#Graph-1 Sales by Category
sale=df.groupby("Category")["Sales"].sum()
sale=sale.sort_values(ascending=False)
plt.style.use("ggplot")
fig,ax=plt.subplots(2,3,figsize=(18,10))

ax[0,0].bar(sale.index,sale.values,color=["red","green","blue","orange"],edgecolor='black')
ax[0,0].set_title("Sales by Category")
ax[0,0].set_xlabel("Category")
ax[0,0].set_ylabel("Sales")
ax[0,0].grid(axis="y")
for i,value in enumerate(sale.values):
    ax[0,0].text(i,value,f"{value:0f}",ha="center")

  #Graph-2 :Monthly Sales Trend
df["Month_Number"]=df["Order_Date"].dt.month
df["Order_Month"]=df["Order_Date"].dt.month_name()
month_sales=(
  df.groupby(["Month_Number","Order_Month"])["Sales"]
  .sum()
  .reset_index()
  .sort_values("Month_Number")
)
ax[0,1].plot(month_sales["Order_Month"],month_sales["Sales"],marker="o",linestyle="--",linewidth=3)
ax[0,1].set_title("Monthly Sales Trend")
ax[0,1].set_xlabel("Month")
ax[0,1].set_ylabel("Sales")
ax[0,1].grid(axis="y")
for i,value in enumerate(month_sales["Sales"]):
    ax[0,1].text(i,value,f"{value:.0f}",ha="center")


    #Graph-3:Profit by Region
profit=df.groupby("Region")["Profit"].sum()
profit=profit.sort_values(ascending=True)
ax[0,2].barh(profit.index,profit.values,edgecolor="black",color=["green","red","blue","orange"])
ax[0,2].set_title("Profit by Region")
ax[0,2].set_xlabel("Profit")
ax[0,2].set_ylabel("Region")
ax[0,2].grid(axis="x")
for i,value in enumerate(profit.values):
   ax[0,2].text(i,value,f"{value:.0f}",va="center")


    #Graph-4 :Payment Method Distribution
payment=df["Payment_Method"].value_counts()
ax[1,0].pie(payment.values,labels=payment.index,autopct="%1.1f%%",startangle=90,explode=explode)
explode=[]
for method in payment.index:
    if method == payment.idxmax():
        explode.append(0.2)
    else:
        explode.append(0)
ax[1,0].set_title("Payment Method Distribution",fontweight="bold")



   #Graph-5:Top Selling Products
product_sales=df.groupby("Product")["Sales"].sum()
product_sales=product_sales.sort_values(ascending=True)
ax[1,1].barh(product_sales.index,product_sales.values,edgecolor="black")
for i,value in enumerate(product_sales.values):
    ax[1,1].text(value,i,f"{value:.0f}",va="center")
ax[1,1].set_title("Top Selling Products")
ax[1,1].set_xlabel("Sales")
ax[1,1].set_ylabel("Product")
ax[1,1].grid(axis="x")


   #Graph-6:Sales vs Profit
ax[1,2].scatter(df["Sales"],df["Profit"],marker="o",s=80,alpha=0.7)
ax[1,2].grid(True)
ax[1,2].set_title("Sales vs Profit",fontweight="bold")
ax[1,2].set_xlabel("Sales")
ax[1,2].set_ylabel("Profit")

plt.tight_layout()
plt.show()

#Business Insights
print(f"Highest Sales Category : {sale.idxmax()}")
print(f"Highest Sales Month : {month_sales.loc[month_sales['Sales'].idxmax(),'Order_Month']}")
print(f"Highest Profit Region : {profit.idxmax()}")

best_payment = payment.idxmax()
print(
    f"Business Insight: {best_payment} is the most preferred payment method "
    f"with {payment.max()} orders."
)

best_product=product_sales.idxmax()
print(
    f"Business Insight: {best_product} is the most sold product "
    f"with {product_sales.max()} sales."
)

k=df["Sales"].corr(df["Profit"])
print(f"Correlation Coefficient:{k:.2f}")
if(k>0 and k<=1):
    print("As Sales increase - Profits also increases")
elif(k==0):
    print("No Relationship between Sales and profits ")
else:
    print("As Sales increase ,profit decreases")


