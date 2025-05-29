import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import minmax_normalization
import matplotlib.pyplot as plt

# 1. Macierz decyzyjna (Koszty, Zyski, Czas, Ryzyko) 
decision_matrix = np.array([
    [5000, 30000, 24, 7],   # Alternatywa A
    [7000, 35000, 30, 5],   # Alternatywa B
    [6000, 28000, 20, 8],   # Alternatywa C
    [5500, 40000, 36, 6],   # Alternatywa D
])

# 2. Wektor wag
weights = np.array([0.3, 0.4, 0.2, 0.1])  # Koszty, Zyski, Czas, Ryzyko

# 3. Kryteria maksymalizowane i minimalizowane 
criteria_types = np.array([-1, 1, -1, -1])

# 4. Normalizacja danych
norm_matrix = np.zeros_like(decision_matrix, dtype=float)
for j in range(decision_matrix.shape[1]):
    norm_matrix[:, j] = minmax_normalization(decision_matrix[:, j], criteria_types[j])

# 5.  Uruchomienie TOPSIS
topsis = TOPSIS()
topsis_scores = topsis(norm_matrix, weights, criteria_types)

# 6. Uruchomienie SPOTIS 
bounds = np.array([
    [5000, 7000],    # Koszty
    [28000, 40000],  # Zyski
    [20, 36],        # Czas
    [5, 8],          # Ryzyko
])
spotis = SPOTIS(bounds)
spotis_scores = spotis(decision_matrix, weights, criteria_types)

# 7. Wyniki
alternatives = ['A', 'B', 'C', 'D']
results_df = pd.DataFrame({
    'Alternatywa': alternatives,
    'TOPSIS': topsis_scores,
    'SPOTIS': spotis_scores
})
results_df['RANK_TOPSIS'] = results_df['TOPSIS'].rank(ascending=False).astype(int)
results_df['RANK_SPOTIS'] = results_df['SPOTIS'].rank(ascending=True).astype(int)

print("=== WYNIKI ===")
print(results_df)

# Wykres słupkowy rankingów
fig, ax = plt.subplots(figsize=(8, 5))
bar_width = 0.35
index = np.arange(len(alternatives))

bars1 = ax.bar(index, results_df['RANK_TOPSIS'], bar_width, label='TOPSIS')
bars2 = ax.bar(index + bar_width, results_df['RANK_SPOTIS'], bar_width, label='SPOTIS')

ax.set_xlabel('Alternatywa')
ax.set_ylabel('Miejsce w rankingu')
ax.set_title('Porównanie rankingów TOPSIS i SPOTIS')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(alternatives)
ax.legend()
ax.invert_yaxis()

plt.tight_layout()
plt.show()
