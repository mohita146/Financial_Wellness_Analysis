# 📊 Financial Wellness & Spending Behavior Analysis of Gen-Z Students

A data analytics project exploring financial habits, spending patterns, and wellness indicators among Gen-Z students.  
This project uses real-world style data to analyze income, expenses, payment preferences, financial stress, and savings behavior.

---

## 🚀 Project Overview

Gen-Z students face rising education and living costs, while income remains limited.  
This project identifies:

- Major spending categories  
- Financial stress indicators  
- Trends across gender, majors, and academic years  
- Digital payment behavior  
- Key factors affecting savings  

The goal is to understand how Gen-Z manages money and what influences their financial wellness.

---

## 🧰 Tech Stack & Tools

- **Python**
- **Pandas, NumPy** — data cleaning & transformation  
- **Matplotlib, Seaborn** — visual analytics  
- **Jupyter Notebook / VS Code** — development  
- Git & GitHub — version control

---

## 📁 Project Structure

financial-wellness-genz/
│
├── data/
│ └── student_spending.csv
│
├── notebooks/
│ └── exploratory_analysis.ipynb
│
├── src/
│ └── analysis.py
│
├── images/
│ ├── spending_by_category.png
│ ├── income_distribution.png
│ ├── heatmap.png
│ ├── payment_method_pie.png
│ ├── gender_expenses.png
│ ├── year_in_school.png
│ ├── major_expenses.png
│ └── savings_distribution.png
│
├── README.md
└── requirements.txt


---

## 🔍 Key Insights

### 📌 1. **Tuition dominates total expenses**
- Tuition has a **0.96 correlation** with total expenses.
- It is the highest cost driver across all students.

### 📌 2. **All 1000 students are financially “At Risk”**
- Savings values are **negative for 100%** of the population.
- Students spend **₹3000–₹7000 more than they earn** each month.

### 📌 3. **Income does NOT influence spending**
Correlation between income and expenses is ≈ 0.  
→ Students spend the same amount regardless of income.

### 📌 4. **Mobile payments slightly dominate**
- Mobile Apps: 35%  
- Credit/Debit Cards: 34%  
- Cash: 31%

### 📌 5. **Spending by gender is nearly identical**
→ Financial pressure affects all genders equally.

### 📌 6. **Seniors spend slightly more than freshmen**
But differences remain small.

### 📌 7. **Psychology students show the highest expenses**
Followed by Engineering & Biology.

---

## 📊 Visualizations

This project includes:

- Bar chart: spending by category  
- Pie chart: payment methods  
- Histogram: income distribution  
- Scatter: income vs expenses  
- Heatmap: correlation matrix  
- Gender-wise expenses  
- Major-wise expenses  
- Year in school vs total expenses  
- Savings distribution  

*(All images stored inside `/images` folder.)*

---

## 🧮 Financial Wellness Score

Based on savings rate:

| Category | Description |
|---------|-------------|
| Excellent | Saves ≥ 30% |
| Good | Saves 15–30% |
| Needs Improvement | Saves 5–15% |
| At Risk | Saves < 5% or negative |

**Result:**  
> 100% of students fall into the **“At Risk”** category due to negative savings.

---

## 📝 How to Run This Project

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/Financial_Wellness_Analysis.git
cd Financial_Wellness_Analysis