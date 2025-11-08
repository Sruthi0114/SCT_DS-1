import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv('population_data.csv')

# ---- Histogram for Age (Continuous) ----
plt.figure(figsize=(8,4))
plt.hist(df['Age'], bins=6, color='pink', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# ---- Bar Chart for Gender (Categorical) ----
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(gender_counts.index, gender_counts.values, color=['lightcoral','lightgreen'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# ---- Bar Chart for Department (Categorical) ----
dept_counts = df['Department'].value_counts()
plt.figure(figsize=(8,4))
plt.bar(dept_counts.index, dept_counts.values, color='mediumpurple')
plt.title('Department Distribution')
plt.xlabel('Department')
plt.ylabel('Count')
plt.show()
