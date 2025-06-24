import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# STEP 1: Load the dataset
df = pd.read_csv(r"C:\Users\user\PycharmProjects\Customer Churn Prediction & Analysis for Orange Telecom\churn-bigml-80.csv")

# STEP 2: Convert categorical columns to numeric
df['International plan'] = df['International plan'].map({'Yes': 1, 'No': 0})
df['Voice mail plan'] = df['Voice mail plan'].map({'Yes': 1, 'No': 0})
df['Churn'] = df['Churn'].astype(int)

# STEP 3: Drop unneeded columns (State, Area code can be dropped for ML)
X = df.drop(['Churn', 'State', 'Area code'], axis=1)
y = df['Churn']

# STEP 4: Split and train a model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# STEP 5: Predict churn on the full dataset
df['Churn_Prediction'] = model.predict(X)

# STEP 6: Export to CSV for Power BI
output_path = r"C:\Users\user\PycharmProjects\Customer Churn Prediction & Analysis for Orange Telecom\churn_with_predictions.csv"
df.to_csv(output_path, index=False)

print(f"CSV file successfully saved at: {output_path}")
