import numpy as np
import scipy.stats as stats

def confidence_interval(p, n, confidence=0.95):
    # Calculate standard error
    se = np.sqrt((p * (1 - p)) / n)
    # Calculate Z-score for the confidence level
    z = stats.norm.ppf((1 + confidence) / 2)
    # Calculate confidence interval
    return p - z * se, p + z * se

# Data for Class 0
precision_class0 = 0.99
recall_class0 = 1.00
f1_score_class0 = 1.00
n_class0 = 117492

# Data for Class 1
precision_class1 = 0.89
recall_class1 = 0.59
f1_score_class1 = 0.71
n_class1 = 1437

# Calculate confidence intervals
ci_precision_class0 = confidence_interval(precision_class0, n_class0)
ci_recall_class0 = confidence_interval(recall_class0, n_class0)
ci_f1_score_class0 = confidence_interval(f1_score_class0, n_class0)

ci_precision_class1 = confidence_interval(precision_class1, n_class1)
ci_recall_class1 = confidence_interval(recall_class1, n_class1)
ci_f1_score_class1 = confidence_interval(f1_score_class1, n_class1)

# Print results
print(f"Class 0 Precision CI: {ci_precision_class0}")
print(f"Class 0 Recall CI: {ci_recall_class0}")
print(f"Class 0 F1-Score CI: {ci_f1_score_class0}")

print(f"Class 1 Precision CI: {ci_precision_class1}")
print(f"Class 1 Recall CI: {ci_recall_class1}")
print(f"Class 1 F1-Score CI: {ci_f1_score_class1}")
