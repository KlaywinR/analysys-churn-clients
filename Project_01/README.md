# Simulação e Análise de Churn de Clientes

## Sobre o projeto

Este projeto simula um conjunto de dados de clientes de uma empresa de telecomunicações e modela o comportamento de churn (cancelamento de serviço) com base em variáveis como tempo de fidelidade, tipo de contrato, tipo de internet e valor da fatura mensal.

O objetivo é criar um dataset realista para estudos de análise de dados e modelagem preditiva.

---

## Objetivo Central

* Gerar dados sintéticos realistas de clientes
* Simular o comportamento de churn com base em regras probabilísticas
* Criar uma base pronta para análises exploratórias (EDA)
* Servir como base para projetos de Machine Learning

---

## Tecnologias utilizadas

* Python 3
* NumPy
* Pandas
* Seaborn
* Matplotlib
* Plotly

---

## Como funciona a simulação

A função `generating_data()` cria um dataset com base em distribuições estatísticas e regras de negócio:

### Variáveis geradas:

* **Id Cliente** → Identificador único
* **Fidelidade em Meses** → Tempo de permanência (1 a 66 meses)
* **Tipo de Contrato**

  * Mensal (maior risco de churn)
  * Anual
  * Dois anos (menor risco)
* **Serviço de Internet**

  * Fibra
  * Rádio
  * Sem internet
* **Fatura Mensal**

  * Baseada no tipo de contrato + ruído aleatório
* **Churn**

  * Variável alvo (0 ou 1)

---

## Lógica do churn

O churn é calculado com base em uma função logística:

* Clientes com menor fidelidade → maior chance de churn
* Contratos mensais → maior risco
* Faturas mais altas → maior risco
* Tipo de internet influencia o comportamento

A probabilidade é definida por:

* Transformação logística (sigmoid)
* Combinação linear de variáveis

---

## Modelo matemático

A probabilidade de churn é dada por uma função logística:

P(churn) = 1 / (1 + e^(z))

Onde `z` é uma combinação das variáveis do cliente.

---

##  Como executar

### 1. Instale as dependências:

```bash
pip install numpy pandas matplotlib seaborn plotly
```

### 2. Execute o script:

```bash
python churn_simulation.py
```

---

## Exemplo de saída

| Id Cliente | Fidelidade em Meses | Tipo de Contrato | Serviço de Internet | Fatura Mensal | Churn |
| ---------- | ------------------- | ---------------- | ------------------- | ------------- | ----- |
| 1          | 12                  | Mensal           | Fibra               | 89.3          | 1     |
| 2          | 45                  | Dois Anos        | Rádio               | 55.1          | 0     |

---

## Possibilidades de uso

Este dataset pode ser utilizado para:

* Análise exploratória (EDA)
* Modelos de Machine Learning (classificação)
* Previsão de churn
* Criação de dashboards
* Testes de algoritmos

---

## Melhorias futuras

* Adicionar mais variáveis (idade, região, plano)
* Criar correlações mais complexas
* Balanceamento de classes
* Exportação automática para CSV
* Integração com modelos preditivos (Random Forest, XGBoost)

---

##ANANANAN