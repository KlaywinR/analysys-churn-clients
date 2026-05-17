import numpy as np 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display


def generating_data(num_clients = 200):
    
    np.random.seed(42)
    
    fidelidade_meses = np.random.randint(1,67, size = num_clients)
    tipo_contrato_opts = ['Mensal', 'Anual', 'Dois Anos']
    contratos_probs = [0.6,0.25, 0.15]
    tipo_contrato = np.random.choice(tipo_contrato_opts, size = num_clients, p = contratos_probs)
    serviço_net_opts = ['Fibra', 'Radio', "Nao"]
    internet_probs = [0.55,0.35,0.1]
    serviço_net = np.random.choice (serviço_net_opts, size = num_clients, p = internet_probs)
    
    
    fatura_b = {
        'Mensal': np.random.normal(60,20),
        'Anual': np.random.normal(70,25),
        'Dois Anos': np.random.normal(80,30),
    }
     
    fatura_mensal = [fatura_b[c] + fidelidade_meses[i] * 0.2 + np.random.normal(0,50) for i, c in enumerate(tipo_contrato)]
    fatura_mensal = np.clip(fatura_mensal, 20,120)
    
    prob_churn_log = -2.5 #tendencia de nao cancelar 
    prob_churn_log += -0.5 * fidelidade_meses
    prob_churn_log += [3.0 if c == 'Mensal' else -1.5 if c == 'Anual' else -2.5 for c in tipo_contrato]
    prob_churn_log += [0.8 if s == 'Fibra' else -0.5 for s in serviço_net]
    prob_churn_log += 0.03 * fatura_mensal
    
    
    prob_churn = 1 / (1 + np.exp(prob_churn_log))
    
    churn  = (np.random.rand(num_clients) < prob_churn).astype(int)
    
    
    df = pd.DataFrame ({
        'Id Cliente': range(1,num_clients +1),
        "Fidelidade em Meses": fidelidade_meses,
        "tipo de contrato": tipo_contrato,
        'serviço  de inteernt': serviço_net,
        'Fatura Mensal': fatura_mensal,
        "Churn": churn
    })
    
    return df

if __name__ == "__main__":
    df = generating_data()
    print("Dados gerados:")
    print(df.head(10))
    # Para salvar em CSV: df.to_csv('dados_churn.csv', index=False)