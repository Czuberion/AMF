import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder

def perform_analysis(data):
    # Load and inspect data
    if 'ID' in data.columns:
        data = data.drop(columns=['ID'])
    
    # Inspect the data
    print(data)
    print(data.head())
    print(data.info())
    print(data.describe())

    # Check for missing values
    print(data.isnull().sum())
    sns.heatmap(data.isnull(), cbar=False)
    plt.show()

    # Plot histograms
    data.hist(bins=50, figsize=(16, 8))
    plt.show()

    # Correlation matrix for numeric columns
    numeric_data = data.select_dtypes(include=['number'])
    correlation_matrix = numeric_data.corr()
    plt.figure(figsize=(16, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.show()

   

    return data
