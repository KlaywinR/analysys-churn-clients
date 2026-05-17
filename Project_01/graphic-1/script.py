import pandas as pd
import matplotlib.pyplot as plt

#dados
df_churn = pd.DataFrame({
    'Churn': [1, 0, 1, 1, 0, 0, 1, 0, 1, 0]
})

#tratamento de dados
churn_counts = (
    df_churn['Churn']
    .value_counts()
    .rename(index={1: 'Sim', 0: 'Não'})
)

color_map = {
    'Sim': '#6A5ACD',  
    'Não': '#BEB0B0'  
}

cores = [color_map[label] for label in churn_counts.index]

explode = [0.08 if label == 'Sim' else 0 for label in churn_counts.index]

#grafico
plt.figure(figsize=(6, 6))

plt.pie(
    churn_counts.values,
    labels=churn_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=cores,
    explode=explode,
    shadow=True
)

plt.title("Distribuição de Churn de Clientes", fontsize=16)

plt.tight_layout()
plt.show()