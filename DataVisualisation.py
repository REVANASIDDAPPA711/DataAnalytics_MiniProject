import pandas as pd
df=pd.read_csv("AgriCrops.csv")
print(df)
import matplotlib.pyplot as plt
import seaborn as sns

# Set up visualization style
sns.set_theme(style="whitegrid")

# Plot distributions for numeric columns
numeric_columns = [
    "Total_Cost_per_q",
    "Wholesale_Price_per_q",
    "Retail_Price_per_q",
    "Middle_Man_Price_per_q",
    "Profit_Wholesale",
    "Profit_Retail",
    "Profit_Middle_Man",
    "Market_Access_Index",
    "Transportation_Cost",
]
# Box plots for profits by crop
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(x="Crop", y="Profit_Retail", data=df, palette="Set3", ax=ax)
ax.set_title("Profit Retail by Crop")
ax.set_ylabel("Profit (Retail)")
plt.xticks(rotation=45)
plt.show()

# Scatter plot: Market Access Index vs. Total Profitability Score
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    x="Market_Access_Index",
    y="Total_Profitability_Score",
    hue="Farmer_Category",
    data=df,
    palette="deep",
    ax=ax,
)
ax.set_title("Market Access Index vs. Total Profitability Score")
ax.set_xlabel("Market Access Index")
ax.set_ylabel("Total Profitability Score")
plt.show()

# Profitability Analysis
sns.boxplot(data=df, x='Farmer_Category', y='Profit_Wholesale')
plt.title("Wholesale Profit by Farmer Category")
plt.show()

sns.boxplot(data=df, x='Farmer_Category', y='Profit_Retail')
plt.title("Retail Profit by Farmer Category")
plt.show()

# State-wise Analysis
state_profit = df.groupby('State')['Profit_Wholesale'].mean().sort_values()
state_profit.plot(kind='barh', color='skyblue', figsize=(10, 6))
plt.title("State-wise Average Wholesale Profit")
plt.xlabel("Average Profit")
plt.ylabel("State")
plt.show()

# Transportation Cost vs Profitability
sns.scatterplot(data=df, x='Transportation_Cost', y='Total_Profitability_Score', hue='Farmer_Category')
plt.title("Transportation Cost vs Total Profitability Score")
plt.show()

# Market Access Index by State
sns.boxplot(data=df, x='State', y='Market_Access_Index')
plt.title("Market Access Index by State")
plt.xticks(rotation=45)
plt.show()

# Recommended Actions
sns.countplot(data=df, y='Recommended_Action', palette='viridis')
plt.title("Frequency of Recommended Actions")
plt.xlabel("Count")
plt.ylabel("Action")
plt.show()
