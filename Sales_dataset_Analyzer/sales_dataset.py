import pandas as pd
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
df =pd.read_csv('sales_data.csv')

print("data overview:")
print(df.head())
print(df['Order Date'])



#data cleaning , check for missing values
print("\n Missing Data check")
print(df.isnull().sum()) #give the total null values in columns
#
# # #Data Pre processing
df['Order Date']=pd.to_datetime(df['Order Date'], errors ='coerce')
#df['Order Date']=df['Order Date'].pd.to_strftime('%y-%m-%d')

df['Total sales']= df['Units Sold'] * df['Unit Price']
df1=df.to_csv('sales_data_new.csv')

#group by order id and calculate total sales per customer
customer_sales=df.groupby('Order ID')['Total sales'].sum().reset_index()
print("\n Total sales by customer:")
print(customer_sales)

#group by order id and calculate total sales per customer
region_sales=df.groupby('Region')['Total sales'].sum().reset_index()
print("\n Total sales by region:")
print(region_sales)

#find most popular product(item type) by quantity sold
product_sales=df.groupby('Item Type')['Total sales'].sum()
print(product_sales)
most_popular_product=product_sales.idxmax()
print("Most popular product is: ",most_popular_product)

#Data Visualization
plt.figure(figsize=(10,10))
plt.plot(region_sales['Region'], region_sales['Total sales'], color='g')
plt.title('total sales by region')
plt.xlabel('Region')
plt.ylabel('Total sales')
plt.show()

#now Creating a 3d plot


