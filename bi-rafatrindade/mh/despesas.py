import pandas as pd
import numpy as np

START_DATE = "2030-01-01"
END_DATE = "2032-12-31"
EMPRESA = "Pousada da Ponte"

linhas_padrao = [
    ("Fixa", "Administrativa", "Contabilidade"),
    ("Fixa", "Administrativa", "Advocacia"),
    ("Fixa", "Administrativa", "Sistemas"),
    ("Fixa", "Administrativa", "Impostos"),
    ("Fixa", "Folha de Pagamento", "Salário"),
    ("Fixa", "Folha de Pagamento", "FGTS"),
    ("Fixa", "Folha de Pagamento", "INSS"),
    ("Variável", "Folha de Pagamento", "Diária"),
    ("Variável", "Operacional", "Combustível"),
    ("Variável", "Operacional", "Aluguel Carro"),
    ("Variável", "Operacional", "Manutenção"),
    ("Variável", "CMV", "Mercadoria")
]

def gerar_valor(descricao):
    if descricao == "Contabilidade":
        return 400
    elif descricao == "Advocacia":
        return 500
    elif descricao == "Sistemas":
        return 55
    elif descricao == "Impostos":
        return np.random.randint(1800, 3000)
    elif descricao == "Salário":
        return np.random.randint(2000, 3500)
    elif descricao == "FGTS":
        return np.random.randint(150, 250)
    elif descricao == "INSS":
        return np.random.randint(150, 250)
    elif descricao == "Diária":
        return np.random.randint(100, 500)
    elif descricao == "Combustível":
        return np.random.randint(1200, 2000)
    elif descricao == "Aluguel Carro":
        return 1500
    elif descricao == "Manutenção":
        return np.random.randint(200, 1000)
    elif descricao == "Mercadoria":
        return np.random.randint(10000, 14000)
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

df.to_csv("bi-rafatrindade/mh/mh_despesa.csv", index=False, sep=";", encoding="utf-8-sig")

print("Arquivo 'mh_despesa.csv' gerado com sucesso!")
