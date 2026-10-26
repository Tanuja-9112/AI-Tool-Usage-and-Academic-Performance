import statistics
from collections import Counter
from scipy.stats import pearsonr, linregress, ttest_ind
import matplotlib.pyplot as plt

# Data of 15 students
ai_hours = [1, 2, 3, 2, 4, 5, 3, 6, 4, 5, 2, 3, 6, 4, 5]
marks = [55, 60, 65, 62, 70, 78, 68, 85, 72, 80, 61, 67, 88, 74, 82]

# 1. Mean
print("Mean AI Usage:", round(statistics.mean(ai_hours), 2))

# 2. Median
print("Median AI Usage:", statistics.median(ai_hours))

# 3. Standard Deviation
print("Standard Deviation:", round(statistics.stdev(ai_hours), 2))

# 4. Frequency Distribution
frequency = Counter(ai_hours)

print("\nFrequency Distribution:")
for hour in sorted(frequency):
    print(hour, "hours:", frequency[hour], "students")

# 5. Correlation
r, p = pearsonr(ai_hours, marks)
print("\nCorrelation:", round(r, 3))

# 6. Regression
slope, intercept, r_value, p_value, std_err = linregress(
    ai_hours, marks
)

print("Regression Equation: Marks =",
      round(slope, 2), "* AI Hours +", round(intercept, 2))

# Predict marks for 4 hours of AI usage
predicted = slope * 4 + intercept
print("Predicted Marks for 4 Hours:", round(predicted, 2))

# 7. Hypothesis Testing
low_usage = [
    marks[i] for i in range(len(ai_hours))
    if ai_hours[i] <= 3
]

high_usage = [
    marks[i] for i in range(len(ai_hours))
    if ai_hours[i] > 3
]

t_stat, p_value = ttest_ind(
    low_usage, high_usage, equal_var=False
)

print("\nHypothesis Testing")
print("T-statistic:", round(t_stat, 3))
print("P-value:", round(p_value, 4))

if p_value < 0.05:
    print("Significant difference in average marks.")
else:
    print("No significant difference in average marks.")

# 8. Bar Graph
hours = sorted(frequency.keys())
student_count = [frequency[h] for h in hours]

plt.figure(figsize=(8, 5))
plt.bar(hours, student_count, edgecolor="black")

plt.title("AI Tool Usage Among Students")
plt.xlabel("AI Usage Hours Per Day")
plt.ylabel("Number of Students")
plt.xticks(hours)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()