# If I toss a coin 20 times, what’s the
# probability of getting of getting 2 or
# fewer heads?

import matplotlib.pyplot as plt
from scipy.stats import binom
import numpy as np

#no. of trials
n=20

#k -> success -> K<=2
x=np.arange(0,n+1)

p=0.5

pmf_values=binom.pmf(x,n,p)

# Calculate the cumulative probability for 2 or fewer heads
cumulative_probability = binom.cdf(2, n, p)

# Create the plot
plt.figure(figsize=(12, 6))
plt.bar(x, pmf_values, color='skyblue', edgecolor='black')

# Highlight the bars for 0, 1, and 2 heads
plt.bar(x[:3], pmf_values[:3], color='orange', edgecolor='black')

# Add labels and title
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('Binomial Distribution: Probability of 2 or Fewer Heads in 20 Coin Tosses')
plt.xticks(np.arange(0, n + 1, 2))  # Show ticks every 2 units for clarity

# Annotate the cumulative probability for 2 or fewer heads
plt.annotate(f"P(X ≤ 2) = {cumulative_probability:.4f}", xy=(2, pmf_values[2]), xytext=(5, pmf_values[2] + 0.02),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, ha='center')

# Show the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
