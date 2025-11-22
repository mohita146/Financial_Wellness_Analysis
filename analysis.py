import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
import os

# Create 'images' folder automatically if not exists
# Ensure 'images' is a real folder
if not os.path.exists("images"):
    os.mkdir("images")

# Helper function to save plots
def save_fig(name):
    path = f"images/{name}.png"
    plt.savefig(path, dpi=300, bbox_inches='tight')
    print(f"Saved: {path}")



# Load data
df = pd.read_csv("data/student_spending.csv.csv")

# Show the first few rows
print(df.head())
print(df.info())

# -----------------------------
# Data Cleaning

# Drop unwanted index column
df = df.drop(columns=["Unnamed: 0"])

# Check duplicates
print("\nDuplicates:", df.duplicated().sum())

# Statistical summary
print("\nSummary statistics:")
print(df.describe(include="all"))

print("\nColumn names:")
print(df.columns)

# List of expense columns
expense_cols = ['tuition', 'housing', 'food', 'transportation', 
                'books_supplies', 'entertainment', 'personal_care',
                'technology', 'health_wellness', 'miscellaneous']

# Total expenses
df["total_expenses"] = df[expense_cols].sum(axis=1)

# Total income
df["total_income"] = df["monthly_income"] + df["financial_aid"]

# Savings
df["savings"] = df["total_income"] - df["total_expenses"]

print("\nSample of income/expense/savings:")
print(df[["monthly_income", "financial_aid", "total_expenses", "total_income", "savings"]].head())

# -----------------------------
# Financial Wellness Score

# Avoid divide-by-zero
df['savings_rate'] = df['savings'] / df['total_income']

# Define categories
def wellness_label(rate):
    if rate >= 0.30:
        return "Excellent"
    elif rate >= 0.15:
        return "Good"
    elif rate >= 0.05:
        return "Needs Improvement"
    else:
        return "At Risk"

df['financial_wellness'] = df['savings_rate'].apply(wellness_label)

print("\nFinancial Wellness distribution:")
print(df['financial_wellness'].value_counts())


# Category-wise total expenses (bar chart)
expense_sums = df[expense_cols].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
sns.barplot(x=expense_sums.values, y=expense_sums.index, palette="viridis")
plt.title("Total Spending by Category")
plt.xlabel("Total Amount Spent")
plt.ylabel("Category")
plt.tight_layout()
plt.show()
save_fig("total_spending_by_category")


#pai chart - payment method
plt.figure(figsize=(6,6))
df['preferred_payment_method'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Preferred Payment Method")
plt.ylabel("")
plt.show()
save_fig("preferred_payment_method")


#histogram - monthly income
plt.figure(figsize=(8,5))
sns.histplot(df['monthly_income'], kde=True, bins=20)
plt.title("Monthly Income Distribution")
plt.xlabel("Income")
plt.tight_layout()
plt.show()
save_fig("income_distribution")


#scatter plot - income vs total expenses
plt.figure(figsize=(7,5))
sns.scatterplot(x=df['total_income'], y=df['total_expenses'])
plt.title("Income vs Total Expenses")
plt.xlabel("Total Income")
plt.ylabel("Total Expenses")
plt.tight_layout()
plt.show()
save_fig("income_vs_expenses")


#heatmap - corrilation
numeric_df = df.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(12,8))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
save_fig("correlation_heatmap")


#gender based spending analysis
plt.figure(figsize=(10,5))
sns.barplot(data=df, x="gender", y="total_expenses")
plt.title("Total Expenses by Gender")
plt.tight_layout()
plt.show()
save_fig("expenses_by_gender")


#spending by year in scholl 
plt.figure(figsize=(10,5))
sns.boxplot(data=df, x="year_in_school", y="total_expenses")
plt.title("Expense Distribution by Year in School")
plt.tight_layout()
plt.show()
save_fig("expenses_by_year")


#spending by major 
plt.figure(figsize=(12,6))
sns.boxplot(data=df, x="major", y="total_expenses")
plt.title("Total Expenses by Major")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
save_fig("expenses_by_major")


#savings distribution 
plt.figure(figsize=(8,5))
sns.histplot(df['savings'], bins=20, kde=True)
plt.title("Savings Distribution")
plt.tight_layout()
plt.show()
save_fig("savings_distribution")
