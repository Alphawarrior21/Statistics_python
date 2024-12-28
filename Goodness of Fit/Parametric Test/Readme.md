# Parametric and non-parametric tests

### **Parametric Tests**
Parametric tests rely on specific assumptions about the data, such as normality, homogeneity of variance, linearity, and independence.

#### **Key Assumptions:**
1. **Normality**: Data follows a normal distribution.
   - **Example**: Suppose you’re analyzing the heights of adult men in Denmark. Heights tend to follow a bell-shaped, normal distribution. A parametric test like a **t-test** or **ANOVA** would be appropriate to compare the mean heights of two groups (e.g., Danish men vs. Swedish men) if the data is normally distributed.

2. **Homogeneity of Variances**: The variances across groups are similar.
   - **Example**: If you’re comparing test scores of students from three different schools, and you assume that the variability in scores is roughly the same across all schools, you can use ANOVA.

3. **Linearity**: There’s a straight-line relationship between variables.
   - **Example**: When studying the relationship between study hours and exam scores, if the scores increase linearly with hours studied, a parametric test like a **Pearson correlation** or **linear regression** is appropriate.

4. **Independence**: Observations are independent of each other.
   - **Example**: If you’re testing the effect of a new workout routine on weight loss, each participant’s weight loss is independent of others.

---

### **Non-Parametric Tests**
Non-parametric tests don’t assume any specific distribution for the data. These are ideal for situations where the data doesn’t meet the parametric assumptions.

#### **Examples When Assumptions Are Violated:**
1. **Data isn’t normally distributed**:
   - **Example**: If you’re analyzing income levels, which are often skewed (a few people earn very high incomes), a non-parametric test like the **Mann-Whitney U test** or **Kruskal-Wallis test** is better.

2. **Heterogeneity of variances**:
   - **Example**: If you’re comparing customer satisfaction ratings (measured on a 1–10 scale) across three companies, but the variability of responses differs greatly between companies, a non-parametric test like the Kruskal-Wallis test is more appropriate.

3. **Non-linear relationships**:
   - **Example**: Suppose you’re studying the relationship between age and reaction time. Reaction time might decrease until middle age, then increase again in older age (U-shaped relationship). A non-parametric correlation like **Spearman’s rank correlation** is suitable.

4. **Dependent/paired data**:
   - **Example**: If you’re analyzing the effectiveness of a meditation program by measuring participants’ stress levels before and after the program, use a non-parametric test like the **Wilcoxon signed-rank test** if normality isn’t met.


### **Summary with Real-Life Choices:**

| **Situation**                                     | **Parametric Test**      | **Non-Parametric Test**      |
|---------------------------------------------------|--------------------------|------------------------------|
| Comparing average heights of two groups          | t-test                   | Mann-Whitney U test          |
| Comparing customer satisfaction across companies | ANOVA                    | Kruskal-Wallis test          |
| Relationship between study hours and exam scores | Pearson correlation      | Spearman’s rank correlation  |
| Before-and-after blood pressure measurements     | Paired t-test            | Wilcoxon signed-rank test    |

# t-test

The **t-test** is a statistical method used to compare the means of two groups. It helps determine if observed differences between the groups are statistically significant or due to random chance.

---

### **Key Points:**
1. **Purpose**: Test the null hypothesis \( H_0 \) that the means of the two groups are equal.
   - Example: Are the average test scores of two classes significantly different?

2. **Assumptions**:
   - **Normality**: Data should follow a normal distribution.
   - **Equal Variances**: The variability in both groups should be similar.
   - **Random Assignment**: Observations should be randomly assigned to groups.

---

### **Types of t-tests and Applications:**

1. **Simple t-test (One-sample t-test)**:
   - **What it does**: Compares the mean of a single sample to a known population mean.
   - **Example**: 
     - Suppose the average IQ of the population is 100.
     - A researcher measures the IQ of 30 students in a class and wants to test if their average IQ differs significantly from 100.

   **Hypotheses**:
   - Null hypothesis (\( H_0 \)): The sample mean = 100.
   - Alternative hypothesis (\( H_A \)): The sample mean ≠ 100.

---

2. **Independent Sample t-test**:
   - **What it does**: Compares the means of two independent groups.
   - **Example**:
     - A company wants to test if a new training method improves employee productivity.
     - Group 1 uses the current method; Group 2 uses the new method.
     - The company compares the average productivity scores of the two groups.

   **Hypotheses**:
   - Null hypothesis (\( H_0 \)): The means of the two groups are equal.
   - Alternative hypothesis (\( H_A \)): The means of the two groups are not equal.

---

3. **Paired Sample t-test (Dependent t-test)**:
   - **What it does**: Compares two measurements from the same group or individual at different times.
   - **Example**:
     - A fitness trainer measures participants’ body weight before and after a 6-week program.
     - The trainer compares the mean weight before and after the program.

   **Hypotheses**:
   - Null hypothesis (\( H_0 \)): The mean difference = 0 (no change in weight).
   - Alternative hypothesis (\( H_A \)): The mean difference ≠ 0 (significant weight change).

---

### **How t-tests Work:**
- The t-test calculates a **t-statistic** based on the difference between group means, the variance within groups, and the sample size.
- This t-statistic is compared to a critical value from the **t-distribution** to determine if the null hypothesis can be rejected.

---

### **Real-World Example Summary**:

| **Type of t-test**            | **Scenario**                                                                 |
|-------------------------------|-------------------------------------------------------------------------------|
| **Simple t-test**              | Testing if the average height of Danish men differs from the population mean. |
| **Independent Sample t-test** | Comparing the average exam scores of public vs. private school students.      |
| **Paired Sample t-test**       | Measuring cholesterol levels before and after a diet intervention.            |

# One-sample t-test

The **one-sample t-test** is used to compare the mean of a single sample to a known or hypothesized population mean. This test checks if the observed sample mean differs significantly from the reference mean.

---

### **Key Points:**
1. **Purpose**: Test the null hypothesis \( H_0 \) that the sample mean is equal to the population mean.
   - Example: Does the average weight of chocolate bars produced by a factory differ from the claimed weight of 50 grams?

2. **Assumptions**:
   - Data is normally distributed.
   - The population mean is known or hypothesized.
   - The sample is randomly selected.

---

### **Steps Involved:**
1. **State the hypotheses**:
   - Null hypothesis (\( H_0 \)): The sample mean = the population mean.
   - Alternative hypothesis (\( H_A \)): The sample mean ≠ the population mean.

2. **Collect data**:
   - Measure the sample (e.g., weights of chocolate bars or health perception scores).

3. **Calculate the t-statistic**:
   - Formula:  
     \[
     t = \frac{\bar{x} - \mu}{\frac{s}{\sqrt{n}}}
     \]
     Where:
     - \( \bar{x} \): Sample mean
     - \( \mu \): Population mean (reference mean)
     - \( s \): Sample standard deviation
     - \( n \): Sample size

4. **Compare with critical t-value**:
   - Use a t-distribution table or software to find the critical value for a given significance level (\( \alpha \), usually 0.05).
   - If \( |t| > \text{critical value} \), reject \( H_0 \).

---

### **Real-World Examples:**

#### **Example 1: Chocolate Bar Weights**
- **Scenario**: A chocolate bar manufacturer claims its bars weigh 50 grams on average.  
- **Test**: You take a random sample of 30 bars, weigh them, and calculate the sample mean (\( \bar{x} \)) and standard deviation (\( s \)).  
- **Objective**: Determine if the sample mean weight differs significantly from 50 grams.  

**Hypotheses**:
- \( H_0 \): The mean weight = 50 grams.
- \( H_A \): The mean weight ≠ 50 grams.

---

#### **Example 2: Health Perception of Managers**
- **Scenario**: You want to see if the health perception of Canadian managers differs from the general population, which has a health perception score of 75 on average.  
- **Test**: You survey 50 managers and calculate their average health perception score (\( \bar{x} \)) and standard deviation (\( s \)).  
- **Objective**: Determine if Canadian managers' perception of health significantly differs from 75.  

**Hypotheses**:
- \( H_0 \): The mean perception score = 75.
- \( H_A \): The mean perception score ≠ 75.

---

### **Results Interpretation:**

1. If the calculated \( t \)-statistic falls within the critical range, **fail to reject \( H_0 \)**:
   - Example: "There is no significant difference between the sample mean and the population mean."
   
2. If the calculated \( t \)-statistic exceeds the critical range, **reject \( H_0 \)**:
   - Example: "The sample mean is significantly different from the population mean."

---

### **Summary Table**:

| **Scenario**                                          | **Population Mean (\( \mu \))** | **Sample Mean (\( \bar{x} \))** | **Objective**                                                       |
|-------------------------------------------------------|----------------------------------|---------------------------------|---------------------------------------------------------------------|
| Chocolate bar weights                                 | 50 grams                        | Calculated from 30 bars         | Test if the sample mean differs from the claimed weight.            |
| Health perception of Canadian managers               | 75                              | Calculated from 50 managers     | Check if managers' perception differs from that of the population.  |

### t-test for independent samples

Compares the means of two independent groups or samples, to know if there is a significant
difference between these means.

For a pharmaceutical company, you want to see if a
drug XY helps you lose weight or not. This is done
by giving 20 people the medicine and 20 people a
placebo.

For a screw factory you want to find out if two
production lines produce screws of the same weight.
To test this, you weigh 50 screws from one machine
and 50 screws from the other machine and compare
them..


# Paired samples t-Test

Used to test/survey the same group or sample at two points in time.

You want to check whether a new drug increases memory performance. You test the
memory performance of 40 people before and after they take the medicine.

Researchers collect monthly temperature data from a weather station for the years 2010
and 2020. They want to determine if there is a statistically significant difference in the
average monthly temperatures between these two years.

## Components of a t-test

1. Formulate the hypothesis to be tested

Null Hypothesis (H0): There is no significant difference between the means of the two related
groups.

Alternative Hypothesis (H1): There is a significant difference between the means of the two
related groups.

2. Collect data from each pair of related observations.

3. Calculate descriptive statistics, i.e. the mean and standard deviation.

4. Use the formula to calculate the t-statistic.

5. Based on the calculated t-statistic, determine the critical value from a t-distribution table or use statistical software to find the p-value.

6. Make a Decision: Reject or retain the null hypothesis


# Calculate t-test

To calculate the t-value, we need two values:

The difference of the means (difference between the groups)

The standard deviation from the mean (difference within the groups)

This value is called the standard error.

t = Difference between mean
values

Standard deviation from the
mean

x̄1 = mean of sample 1

x̄2 = mean of sample 2

s1 = standard deviation of
sample 1

s2 = standard deviation of
sample 2

n1 = number of cases in sample
1

n2 = number of cases in sample
2

x̄ = mean of the
sample

μ = reference value

s = standard deviation

n = number of cases

t-value for the one sample
t-test

x̄d = mean of the difference

0 = reference value

s = standard deviation

n = number of cases


# The t-value and the null hypothesis

We now want to use the t-test to find out whether we reject the null hypothesis or not.

The t-value has a corresponding p-value, which represents the probability that what is observed
could be produced by random data. The lower the p-value, the more confident we can be that
the difference is not produced by chance and is indeed a reliable difference between the means
of the two groups.

To decide on the null hypothesis, we can use the t-value in two ways –

Read the critical t-value from a table, or

Calculate the p-value with the help of the t-value.

If t-value > t-critical 🡪 reject H0 🡪 Two means are so different

If p-value < level of significance 🡪 reject H0 🡪 Two means are not equal