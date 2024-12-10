# If I toss a coin 20 times, what’s the
# probability of getting exactly 10 heads?

import matplotlib.pyplot as plt
from scipy.stats import binom
import numpy as np

#no. of trials
n=20
#exactly 10 heads(success count)
k=10
#probabilty of having 1 head(successs event) in a single single trial
p=0.5

#P(X=10)
p=binom.pmf(10,20,0.5)

print(p*100)

#To shoe the binomial distribution lets take the distribution of trials
x=np.arange(0,10+1)

p_binomDistribution=binom.pmf(x,n,p)

# Create the plot
plt.figure(figsize=(12, 6))
plt.bar(x, p_binomDistribution, color='skyblue', edgecolor='black')

# Highlight the bar for exactly 10 heads
plt.bar(10, p_binomDistribution[10], color='orange', edgecolor='black')

# Add labels and title
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('Binomial Distribution: Probability of Heads in 20 Coin Tosses')
plt.xticks(np.arange(0, n + 1, 2))  # Show ticks every 2 units for clarity

# Annotate the probability for exactly 10 heads
plt.annotate(f"P(X=10) = {p_binomDistribution[10]:.4f}", xy=(10, p_binomDistribution[10]), xytext=(10, p_binomDistribution[10] + 0.02),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, ha='center')

# Show the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


