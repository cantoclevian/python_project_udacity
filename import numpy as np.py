import numpy as np
import scipy.stats as stats

def confidence_interval(metric, n, confidence=0.95):
    se = np.sqrt((metric * (1 - metric)) / n)
    z = stats.norm.ppf((1 + confidence) / 2)
    return metric - z * se, metric + z * se

# Example for Class 0 Precision
precision_class0 = 0.99
n_class0 = 117492
ci_class0_precision = confidence_interval(precision_class0, n_class0)

print(f"Confidence Interval for Class 0 Precision: {ci_class0_precision}")