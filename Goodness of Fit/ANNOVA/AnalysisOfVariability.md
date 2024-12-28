# Analysis of variance (ANNOVA)

An analysis of variance (ANOVA) tests whether statistically significant differences exist between
more than two samples. For this purpose, the means and variances of the respective groups are
compared with each other. In contrast to the t-test, which tests whether there is a difference
between two samples, the ANOVA tests whether there is a difference between more than two
groups.

There are different types of analysis of variance, the most common are the one-way and
two-way analysis of variance.

## Why not calculate multiple t-tests?

ANOVA is used when there are more than two groups. Of course, it would also be a possibility
to calculate a t-test for each combination of the groups. The problem here, however, is that
every hypothesis test has some degree of error. This probability of error is usually set at 5%, so
that, from a purely statistical point of view, every 20th test gives a wrong result

If, for example, 20 groups are compared in which there is actually no difference, one of the tests
will show a significant difference purely due to the sampling.


## Difference between one-way and two-way ANOVA

The one-way analysis of variance only checks whether an independent variable has an
influence on a metric dependent variable. However, if two factors, i.e. two independent
variables, are considered, a two-way analysis of variance must be used.

### One-factor ANOVA

Does a person's place of residence (independent variable) influence his or her salary
(dependent variable)?

### Two-factors ANOVA

Does a person's place of residence (1st independent variable) and gender (2nd independent
variable) affect his or her salary (dependent variable)?