import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

df = pd.read_csv("/content/data (1).csv")

data = df.copy()

# Replace -1 values in PortfolioOpen (these are the missing values)
data['PortfolioOpen'] = data['PortfolioOpen'].replace(-1, np.nan)

# Drop date columns (because they are strings)
drop_cols = [col for col in data.columns if data[col].dtype == 'object']
data_num = data.drop(columns=drop_cols)

# MICE Imputer
imputer = IterativeImputer(max_iter=50, random_state=0)

# Fit and transform
imputed = imputer.fit_transform(data_num)

# Convert back to DataFrame
imputed_df = pd.DataFrame(imputed, columns=data_num.columns)

# Extract last 20 imputed values
last20 = imputed_df['PortfolioOpen'].tail(20)

print("Last 20 imputed PortfolioOpen values:")
print(last20)
