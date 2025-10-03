import pandas as pd
import numpy as np

START_DATE = "2030-01-01"
END_DATE = "2035-12-31"
EMPRESA = "Pousada da Ponte"

linhas_padrao = [
    ("Fixa", "Administrativa", "Aluguel"),
    ("Fixa", "Administrativa", "Energia"),
    ("Fixa", "Administrativa", "Água"),
    ("Fixa", "Administrativa", "Contabilidade"),
    ("Fixa", "Administrativa", "Internet"),
    ("Variável", "Administrativa", "Impostos"),
    ("Fixa", "Folha de Pagamento", "Salário"),
    ("Fixa", "Folha de Pagamento", "FGTS"),
    ("Fixa", "Folha de Pagamento", "INSS"),
    ("Variável", "Operacional", "Padaria"),
    ("Variável", "Operacional", "Mat. Linpeza"),
    ("Variável", "Operacional", "Manutenção"),
    ("Variável", "Folha de Pagamento", "Diária"),
    ("Variável", "CMV", "Mercadoria")
]

def gerar_valor(descricao):
    if descricao == "Aluguel":
        return 4800
    elif descricao == "Energia":
        return np.random.randint(3200, 3500)
    elif descricao == "Água":
        return np.random.randint(500, 601)
    elif descricao == "Contabilidade":
        return 400
    elif descricao == "Internet":
        return 220
    elif descricao == "Impostos":
        return np.random.randint(1500, 2000)
    elif descricao == "Salário":
        return np.random.randint(3200, 4500)
    elif descricao == "FGTS":
        return np.random.randint(320, 450)
    elif descricao == "INSS":
        return np.random.randint(320, 450)
    elif descricao == "Padaria":
        return np.random.randint(800, 1000)
    elif descricao == "Mat. Linpeza":
        return np.random.randint(200, 300)
    elif descricao == "Manutenção":
        return np.random.randint(200, 500)
    elif descricao == "Diária":
        return np.random.randint(200, 500)
    elif descricao == "Mercadoria":
        return np.random.randint(300, 500)
    else:
        return 0

datas = pd.date_range(start=START_DATE, end=END_DATE, freq='M')

linhas = []

for data in datas:
    for cat, tipo, desc in linhas_padrao:
        valor = gerar_valor(desc)
        linhas.append({
            "data": data.strftime("%Y-%m-%d"),
            "empresa": EMPRESA,
            "categoria": cat,
            "tipo": tipo,
            "descricao": desc,
            "valor": valor
        })

df = pd.DataFrame(linhas)

df.to_csv("bi-rafatrindade/mh/pousada_despesas.csv", index=False, sep=";", encoding="utf-8-sig")

print("Arquivo 'pousada_despesas.csv' gerado com sucesso!")
