# Take the example of 5 coin tosses.
# What’s the probability that you flip
# exactly 3 heads in 5 coin tosses?

import matplotlib.pyplot as plt
from scipy.stats import binom
import numpy as np

# Number of trials
n = 5
# Probability of success on a single trial
p = 0.5

# Possible number of successes (0 to n)
x = np.arange(0, n + 1)

# Calculate the binomial PMF
pmf_values = binom.pmf(x, n, p)

# Create the plot
plt.figure(figsize=(8, 6))
plt.bar(x, pmf_values, color='skyblue', edgecolor='black')

# Highlight the bar for exactly 3 heads
plt.bar(3, pmf_values[3], color='orange', edgecolor='black')

# Add labels and title
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('Binomial Distribution: Probability of Heads in 5 Coin Tosses')
plt.xticks(x)

# Annotate the probability for exactly 3 heads
plt.annotate(f"P(X=3) = {pmf_values[3]:.4f}", xy=(3, pmf_values[3]), xytext=(3, pmf_values[3] + 0.05),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, ha='center')

# Show the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

