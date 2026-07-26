import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("employee_data.csv")
print("--------INFORMATION--------")
print("First 5 Rows of the DataFrame:")
print(df.head())
print("Last 5 Rows of the DataFrame:")
print(df.tail())
print("DataFrame Information:")
print(df.info())
print("DataFrame Description:")
print(df.describe())
print("DataFrame Shape:")
print(df.shape)
print("DataFrame Columns:")
print(df.columns)
print("\n\n\n")

df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
df=df.drop_duplicates()
df["Joining_Date"]=pd.to_datetime(df["Joining_Date"],errors='coerce')
#found invalid_date so replaced with a valid date
df.loc[df["Joining_Date"].isna(), "Joining_Date"] = pd.Timestamp("2022-08-15")
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)


df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 30, 45, 100],
    labels=["Young", "Adult", "Senior"],
    right=True
)
df["Salary_Category"]=pd.qcut(
    df["Salary"],
    q=3,
    labels=["Low", "Medium", "High"]
)
df["Experience_Level"]=pd.cut(df["Experience"],
    bins=[0,3,7,20],
    labels=["Junior", "Mid-level", "Senior"],
    right=True
)
print(df)



print("\n\n")
print("Average Salary by Department:")
print(df.groupby("Department")["Salary"].mean())
print("\nEmployees in each Department:")
print(df["Department"].value_counts())
print("\nAverage age of employees in each Department:")
print(df.groupby("Department")["Age"].mean())
print("\nAverage experience of employees in each Department:")
print(df.groupby("Department")["Experience"].mean())
print("\nNumber of male and female employees:")
print(df["Gender"].value_counts())
print("\nHighest Paid Employee")
print(df.loc[df["Salary"].idxmax()])#idxmax() returns index of max value
print("\nLowest Paid Employee")
print(df.loc[df["Salary"].idxmin()])#idxmin() returns index of min value
print("\n\n")


print("\nAverage Salary by Department-Pivot Table")
pivot_salary=pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="mean"
)
print(pivot_salary)

print("\nAverage Salary by Department and Gender")
pivot_gender=pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)
print(pivot_gender)

print("\nCounting employees by Department and Gender")
cross=pd.crosstab(
    df["Department"],df["Gender"]
)
print(cross)
print("\n\n")


print("\nCorrelation Matrix")
print(df.corr(numeric_only=True))
print("\nCorrelation between Experience and Salary")
print(df["Experience"].corr(df["Salary"]))
print("\nCorrelation between Age and Salary")
print(df["Age"].corr(df["Salary"]))
print("\n\n")


#GRAPHS
  #Graph-1 :Employees by Department
count=df["Department"].value_counts()
plt.style.use("ggplot")
plt.figure(figsize=(8,5))
plt.bar(count.index,count.values,color=["red","green","blue","orange"],edgecolor="black")
plt.title("Employees by Department",fontsize=16,fontweight="bold")
plt.xlabel("Department")
plt.ylabel("Employee count")
plt.grid(axis="y")
for i,value in enumerate(count.values):
    plt.text(i,value,str(value),ha="center")
plt.tight_layout()
plt.show()

   #Graph-2:Gender Distribution
count=df["Gender"].value_counts()
plt.figure(figsize=(8,5))
plt.pie(count.values,labels=count.index,colors=["red","green"],autopct="%1.1f%%",startangle=90,explode=[0,0.2],shadow=True)
plt.title("Gender Distribution",fontweight="bold",fontsize=16)
plt.tight_layout()
plt.show()

   #Graph-3:Salary Distribution
data=df["Salary"].dropna()
plt.figure(figsize=(8,5))
plt.style.use("ggplot")
plt.hist(data,bins=5,color="#ff65dd",edgecolor="black",alpha=0.8)
plt.title("Slaary Distribution",fontweight="bold")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.grid(axis="y")
avg_salary=data.mean()
plt.axvline(avg_salary,color="red",linestyle="--",linewidth=2,label="Average Salary")
plt.legend()
plt.tight_layout()
plt.show()
print("Average Salary",avg_salary)
    
    #Graph-4:Experience vs Salary
df=df.dropna(subset=["Experience","Salary"])
plt.style.use("ggplot")
plt.figure(figsize=(8,5))
plt.scatter(df["Experience"],df["Salary"],color="green",marker="s",s=100,alpha=0.8,edgecolor="black")
z=np.polyfit(df["Experience"],df["Salary"],1)
p=np.poly1d(z)
plt.plot(
    df["Experience"],
    p(df["Experience"]),
    color="red",
    linewidth=2,
    label="Trend line"
)
plt.title("Experience vs Salary",fontweight="bold")
plt.xlabel("Experience(Years)")
plt.ylabel("Salary")
plt.annotate("Text",xy=(5,40000),xytext=(4,42000),arrowprops=dict(arrowstyle="->"))
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
print("No strong relationship is observed between experience nad salary")


     #Graph-5:Average Salary by Department
avg_salary=df.groupby("Department")["Salary"].mean()
plt.style.use("ggplot")
plt.figure(figsize=(8,5))
plt.bar(avg_salary.index,avg_salary.values,edgecolor="black",colors=["red","blue","green","orange"])
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.grid(axis="y")
for i,value in enumerate(avg_salary.values):
    plt.text(i,value,f"{value:0f}",ha="center")
high=avg_salary.idxmax()
print(f"Department with Highest Salary:{high} , Highest Salary:{avg_salary.max()}")
plt.tight_layout()
plt.show()
print(f"The {high} department has the highest average salary (₹{avg_salary.max():.2f}).")