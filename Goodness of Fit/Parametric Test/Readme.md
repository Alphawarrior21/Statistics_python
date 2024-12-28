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

