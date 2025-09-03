import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("players_22.csv")

#Top 20 overall
top_20_overall = df.sort_values(by = ['overall'], ascending = False).head(20)
print(top_20_overall[['short_name', 'overall', 'club_name', 'age']])
sns.set_style("darkgrid")
plt.figure(figsize = (12, 8))
barplot = sns.barplot(x = top_20_overall['overall'], y = top_20_overall['short_name'], palette = 'rocket')
barplot.bar_label(barplot.containers[0], fmt='%.2f')
plt.title("Top 20 Melhores Jogadores no FIFA 22", fontsize = 14)
plt.xlabel("Overall", fontsize = 12)
plt.ylabel("Jogador", fontsize = 12)
plt.tight_layout()
plt.show()

print("-=" * 40)

#15 Maiores Jovens Promessas
menor_21 = df[df['age'] <= 21]
maiores_potenciais = menor_21.sort_values(by = ['potential'], ascending = False).head(15)
print(maiores_potenciais[['short_name', 'age', 'club_name', 'overall', 'potential']])
sns.set_style("whitegrid")
plt.figure(figsize = (12, 8))
barplot = sns.barplot(x = maiores_potenciais['potential'], y = maiores_potenciais['short_name'], palette = 'mako')
barplot.bar_label(barplot.containers[0], fmt='%.2f')
plt.title("Top 15 Maiores Jovens Promessas FIFA 22", fontsize = 14)
plt.xlabel("Overall Máximo", fontsize = 12)
plt.ylabel("Jogador", fontsize = 12)
plt.tight_layout()
plt.show()

#Bons e baratos (20)
maior_zero = df[df['value_eur'] > 0 ].copy()
bons_e_baratos = maior_zero[
    (maior_zero['overall'] >= 80) &
    (maior_zero['age'] <= 30)
].copy()
bons_e_baratos['custo_beneficio'] = bons_e_baratos['overall'] / (bons_e_baratos['value_eur'] / 1000000)
top20_bom_barato = bons_e_baratos.sort_values(by = ['custo_beneficio'], ascending = False).head(20)
print(top20_bom_barato[['short_name', 'age', 'club_name', 'overall', 'potential']])
sns.set_style("ticks")
plt.figure(figsize = (12, 8))
barplot = sns.barplot(x = top20_bom_barato['custo_beneficio'], y = top20_bom_barato['short_name'], palette = 'viridis')
barplot.bar_label(barplot.containers[0], fmt='%.2f')
plt.title("Bom e Barato", fontsize = 14)
plt.xlabel("Custo-Benefício", fontsize = 12)
plt.ylabel("Jogador", fontsize = 12)
plt.tight_layout()
plt.show()
