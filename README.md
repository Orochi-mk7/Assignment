
## Introduction

This README explains the step-by-step process of analyzing the NSL-KDD dataset using Python. The code provided in this repository performs various data preprocessing, feature selection, and exploratory data analysis (EDA) tasks.

## Code Overview

1 Loading the Dataset

I start by loading the NSL-KDD dataset from the 'KDDTrain+.txt' text file using the Pandas library. This dataset contains information about network traffic for intrusion detection.

2 Handling Missing Values

I handle missing values in the dataset by replacing them with the mean of the respective columns. This ensures that the data is complete and ready for analysis.

3 Checking for Duplicate Records

Duplicate records can affect the quality of analysis. I check for duplicate records in the dataset and either retain or remove them, ensuring data integrity.

 4 Categorical Data Encoding

Categorical data, such as 'protocol_type,' is encoded into numerical format using one-hot encoding. This step is essential for machine learning algorithms to work with categorical features.

5 Standardizing Numeric Features

I standardize numeric features by scaling them to have a mean of 0 and a standard deviation of 1. This step ensures that all features contribute equally to subsequent analyses.

6 Feature Selection

I use the chi-squared (χ²) method to perform feature selection and select the top 10 most relevant features. This step reduces dimensionality and focuses on the most important aspects of the data.

7 Feature Engineering

I create a new feature called 'failed_login_attempts' by combining relevant features: 'num_failed_logins,' 'root_shell,' and 'su_attempted.' This new feature provides additional information for analysis.

8 Data Visualization

I create two types of data visualizations:

 A histogram of the 'failed_login_attempts' feature to understand its distribution.
 A scatter plot showing the relationship between 'failed_login_attempts' and 'duration.'

9 Summary Statistics

I display summary statistics for numeric columns, providing insights into the data's central tendencies and distributions.

10 Unique Values and Missing Values

I check for unique values in the 'protocol_type' column and report them. Additionally, I check for missing values and display the count of missing values in each column.

11 Class Distribution

I analyze the class distribution of the 'class' column, which is crucial for understanding the balance between normal and intrusion records.

12 Additional EDA

I create a pair plot to visualize relationships between features, and a correlation heatmap to understand feature correlations.
