import numpy as np
from scipy.stats import norm, chi2

# Dane
weights = [57.5, 62.5, 67.5, 72.5, 77.5, 82.5, 87.5]
observed = [7, 11, 22, 35, 23, 8, 4]
total = sum(observed)
mean = 72
std_dev = 7
alpha = 0.01

# Wyznaczanie granic przedziałów
intervals = [(55, 60), (60, 65), (65, 70), (70, 75), (75, 80), (80, 85), (85, 90)]
expected = []

# Obliczanie oczekiwanych liczności
for (low, high) in intervals:
    p = norm.cdf(high, mean, std_dev) - norm.cdf(low, mean, std_dev)
    expected.append(p * total)

# Obliczanie statystyki chi-kwadrat
chi_square = sum((o - e) ** 2 / e for o, e in zip(observed, expected))

# Stopnie swobody i wartość krytyczna
df = len(intervals) - 1 - 2
critical_value = chi2.ppf(1 - alpha, df)

print(chi_square, '|', critical_value)
