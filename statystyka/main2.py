import numpy as np
from scipy.stats import chi2

# Dane
observed = np.array([
    [170, 85, 5],
    [20, 25, 15],
    [10, 10, 60]
])
row_totals = observed.sum(axis=1)
col_totals = observed.sum(axis=0)
total = observed.sum()

# Obliczanie oczekiwanych liczności
expected = np.outer(row_totals, col_totals) / total

# Obliczanie statystyki chi-kwadrat
chi_square = ((observed - expected) ** 2 / expected).sum()

# Stopnie swobody
df = (observed.shape[0] - 1) * (observed.shape[1] - 1)

# Wartość krytyczna
alpha = 0.01
critical_value = chi2.ppf(1 - alpha, df)

# Współczynnik C-Pearsona
C = np.sqrt(chi_square / (chi_square + total))

# Współczynnik V-Cramera
V = np.sqrt(chi_square / (total * min(observed.shape[0] - 1, observed.shape[1] - 1)))

print(chi_square, '|', critical_value, '|',C, '|', V)
