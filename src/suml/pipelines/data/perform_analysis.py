import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def perform_analysis(data):
    # Load and inspect data
    if "ID" in data.columns:
        data = data.drop(columns=["ID"])

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
    data.hist(bins=50, figsize=(16, 12))
    plt.show()

    # Correlation matrix for numeric columns
    numeric_data = data.select_dtypes(include=["number"])
    correlation_matrix = numeric_data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.show()

    return data
