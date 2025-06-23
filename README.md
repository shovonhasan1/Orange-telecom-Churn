# Orange Telecom Churn Prediction – Retention Through Data

**“Because saving a customer costs less than earning a new one.”**

This project focuses on predicting customer churn using Orange Telecom's customer data. Through end-to-end data cleaning, feature engineering, modeling, and visualization, the goal was to empower telecom marketers and data teams to make smarter retention decisions.

---

## Project Objective

To analyze customer data and **predict churn probability** using supervised machine learning.  
The final deliverable includes both a **Python-based churn prediction model** and a **Power BI dashboard** highlighting key patterns, at-risk customer segments, and business insights.

---

## Project Structure

orange-telecom-churn/
├── churn_model.py ← Python script for model building
├── Orange_Telecom_Churn.xlsx ← Original dataset
├── Churn_Predictions.xlsx ← Output with churn probabilities
├── churn_dashboard.pbix ← Power BI dashboard file
├── requirements.txt ← Package list
└── README.md ← This file


---

## 🧪 What Was Done (Step-by-Step Breakdown)

### 1. **Data Cleaning**
- Loaded Excel dataset using `pandas`
- Removed duplicate rows
- Stripped whitespace from column headers
- Converted target column `Churn` from Yes/No to 1/0
- Handled missing values (e.g., filled or dropped)

### 2. **Feature Engineering**
- Selected relevant features for training:
  - Usage metrics: Call minutes, international plan, number of complaints
  - Account features: Contract type, tenure, payment method
  - Demographics: State, age group
- Encoded categorical variables using **OneHotEncoding**
- Split the dataset into:
  - **X**: Feature set
  - **y**: Churn (target variable)

### 3. **Model Building**
- Built a `Pipeline` using:
  - `ColumnTransformer` for preprocessing
  - `LogisticRegression` for classification (later expanded to include `RandomForest` or `DecisionTree` if needed)
- Fit the model on full dataset
- Evaluated model performance (accuracy, precision, recall — depending on version)

### 4. **Churn Prediction Output**
- Predicted churn probability for each customer
- Appended it as a new column: `churn_prob`
- Exported final results to Excel:
  - `Row_Level` sheet: full customer dataset with predicted churn
  - `Summary` sheet: churn rate by state or segment

### 5. **Power BI Dashboard**
- Imported prediction results into Power BI
- Created visualizations:
  - KPI cards: Churn rate, average tenure
  - Bar charts: Churn rate by contract type, state
  - Funnel chart: Customer base → At-risk → Churned
  - Donut chart: Churn vs retention
  - Map visualizations for geographic churn distribution

---

## Sample Insights Found

- Customers with international plans had **3x higher churn rates**
- Short-tenure customers (<6 months) were the **most likely to churn**
- Certain states had unusually high churn percentages — highlighting regional gaps
- Monthly contract customers churned more than annual contract holders

---

## Tools & Libraries Used

| Tool / Library      | Purpose                           |
|---------------------|-----------------------------------|
| Python (3.10+)      | Data manipulation & modeling      |
| `pandas`            | Data handling                     |
| `scikit-learn`      | Preprocessing & ML model pipeline |
| `openpyxl`, `xlsxwriter` | Excel output for Power BI       |
| Power BI            | Visualization and dashboards      |

---

## Why This Matters

Churn directly affects a telecom company’s bottom line. Identifying high-risk customers allows companies to:
- Intervene early with targeted offers
- Improve customer service for vulnerable segments
- Retain loyal customers and improve overall CLV (Customer Lifetime Value)

This project demonstrates the **real-world application** of data science for marketing, strategy, and product teams.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your_username/orange-telecom-churn.git
cd orange-telecom-churn

Create a virtual environment:

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
Install required libraries:

bash
Copy
Edit
pip install -r requirements.txt
Run the model script:

bash
Copy
Edit
python churn_model.py
