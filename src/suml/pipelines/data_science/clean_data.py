import pandas as pd
from sklearn.preprocessing import LabelEncoder

def clean_data(data):
    # Drop columns with all NaN values
    data = data.dropna(axis=1, how='all')
    
    # Drop rows with any NaN values
    data = data.dropna(axis=0, how='any')

    # Convert 'TARGET' to numeric, replacing errors with NaN
    data['TARGET'] = pd.to_numeric(data['TARGET'], errors='coerce')

    # Drop rows where 'TARGET' is NaN
    data = data.dropna(subset=['TARGET'])

    # Check and handle infinite values
    data.replace([float('inf'), float('-inf')], float('nan'), inplace=True)

    # Drop rows with any NaN values (including those created by inf replacements)
    data = data.dropna(axis=0, how='any')

    # Initialize LabelEncoder
    label_encoder = LabelEncoder()

    # # Iterate over columns with 'object' type and encode them
    # for column in data.select_dtypes(include=['object']).columns:
    #     data[column] = label_encoder.fit_transform(data[column])

    return data
