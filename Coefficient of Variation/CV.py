import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import variation

# Generate sample data
np.random.seed(0)
data = np.random.normal(loc=50, scale=10, size=1000)  # Normal distribution

# Calculate mean, standard deviation, and CV
mean = np.mean(data)
std_dev = np.std(data)
cv = variation(data) * 100  # CV as a percentage
# calc_cv=(std_dev/mean)*100
# print(calc_cv)

# Plotting the distribution
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')

# Annotate mean, standard deviation, and CV
plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean:.2f}')
plt.axvline(mean + std_dev, color='green', linestyle='dashed', linewidth=2, label=f'Mean + 1 SD: {mean + std_dev:.2f}')
plt.axvline(mean - std_dev, color='green', linestyle='dashed', linewidth=2, label=f'Mean - 1 SD: {mean - std_dev:.2f}')
plt.text(mean + std_dev + 1, plt.ylim()[1] * 0.9, f'CV: {cv:.2f}%', color='black')

# Labels and title
plt.title('Distribution with Coefficient of Variation')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Show plot
plt.show()
