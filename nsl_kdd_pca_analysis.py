import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, chi2

# Load data from the text file 
data = pd.read_csv('KDDTrain+.txt')
    
# Missing Value Handling
data.fillna(data.mean(), inplace=True)

# Check for duplicate records
duplicate_records = data[data.duplicated(keep='first')]

if not duplicate_records.empty:
    print("Duplicate records found. Sample duplicates:")
    print(duplicate_records.head())
    
    data = data.drop_duplicates(keep='first')
else:
    print("No duplicate records found.")

# Categorical Data Encoding 
data = pd.get_dummies(data, columns=['protocol_type'], drop_first=True)

# Data preprocessing: Standardize numeric features
numeric_features = data.select_dtypes(include=['float64', 'int64'])
scaler = StandardScaler()
data[numeric_features.columns] = scaler.fit_transform(numeric_features)

num_features_to_select = 10

# Identify features and labels
X = data.drop('class', axis=1)
y = data['class']

# Apply feature selection
feature_selector = SelectKBest(score_func=chi2, k=num_features_to_select)
selected_features = feature_selector.fit_transform(X, y)

# Retrieve the indices of the selected features
selected_feature_indices = feature_selector.get_support(indices=True)

# Create a DataFrame with the selected features
selected_features_df = X.iloc[:, selected_feature_indices]

# Update the 'data' DataFrame with the selected features
data = pd.concat([selected_features_df, data['class']], axis=1)

# Feature Engineering: Create a new feature 'failed_login_attempts'
data['failed_login_attempts'] = data['num_failed_logins'] + data['root_shell'] + data['su_attempted']

# Check the distribution of the new feature
plt.figure(figsize=(8, 6))
sns.histplot(data['failed_login_attempts'], bins=10, kde=True)
plt.title("Distribution of 'failed_login_attempts'")
plt.xlabel("Number of Failed Login Attempts")
plt.ylabel("Frequency")
plt.show()

# Create a scatter plot between 'failed_login_attempts' and 'duration'
plt.figure(figsize=(8, 6))
plt.scatter(data['failed_login_attempts'], data['duration'], alpha=0.5)
plt.xlabel("Failed Login Attempts")
plt.ylabel("Duration")
plt.title("Relationship Between Failed Login Attempts and Duration")
plt.show()

# Save the scatter plot as an image
plt.savefig("scatter_plot.png")

# Show the plot
plt.show()

# Display the number of rows and columns
print("Number of rows and columns:", data.shape)

# Display data types of each column
print("Data types:", data.dtypes)

# Display the first few rows of the dataset
print(data.head())

# Summary statistics for numeric columns
print(data.describe())

# Unique values in a specific column 
unique_protocols = data['protocol_type'].unique()
print("Unique protocols:", unique_protocols)

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values:", missing_values)

# Class distribution for the 'class' column
class_distribution = data['class'].value_counts()
print("Class distribution:\n", class_distribution)

# Histogram of a numeric feature
plt.figure(figsize=(8, 6))
sns.histplot(data['duration'], bins=20, kde=True)
plt.title("Distribution of 'duration'")
plt.xlabel("Duration")
plt.ylabel("Frequency")
plt.show()

# Further EDA: Pair Plot
sns.pairplot(data, hue='class', plot_kws={'alpha': 0.5})

# Correlation Analysis: Heatmap
correlation_matrix = data.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
