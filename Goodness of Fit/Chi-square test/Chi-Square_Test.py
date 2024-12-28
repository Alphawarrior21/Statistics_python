import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# Step 1: Create the data (observed frequencies)
# Rows: Gender, Columns: Product Categories
data = np.array([[30, 50, 20],  # Male
                 [40, 30, 30]]) # Female

# Convert to DataFrame for better visualization
df = pd.DataFrame(data, columns=["Electronics", "Clothing", "Groceries"], index=["Male", "Female"])
print("Observed Frequency Table:")
print(df)

# Step 2: Perform Chi-Square Test
chi2, p, dof, expected = chi2_contingency(data)

print("\nChi-Square Test Results:")
print(f"Chi-Square Statistic: {chi2:.2f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of Freedom: {dof}")
print("\nExpected Frequencies Table:")
print(pd.DataFrame(expected, columns=["Electronics", "Clothing", "Groceries"], index=["Male", "Female"]))

# Step 3: Interpret Results
alpha = 0.05
if p < alpha:
    print("\nConclusion: Reject the null hypothesis (H₀). There is an association between gender and product category preference.")
else:
    print("\nConclusion: Fail to reject the null hypothesis (H₀). Gender and product category preference are independent.")
