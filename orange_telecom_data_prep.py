import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv(r"C:\Users\user\PycharmProjects\Customer Churn Prediction & Analysis for Orange Telecom\churn-bigml-80.csv")

df['International plan'] = df['International plan'].map({'Yes': 1, 'No': 0})
df['Voice mail plan'] = df['Voice mail plan'].map({'Yes': 1, 'No': 0})
df['Churn'] = df['Churn'].astype(int)

X = df.drop(['Churn', 'State', 'Area code'], axis=1)
y = df['Churn']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


df['Churn_Prediction'] = model.predict(X)

output_path = r"C:\Users\user\PycharmProjects\Customer Churn Prediction & Analysis for Orange Telecom\churn_with_predictions.csv"
df.to_csv(output_path, index=False)

print(f"CSV file successfully saved at: {output_path}")
