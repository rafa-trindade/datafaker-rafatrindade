import pandas as pd
import numpy as np
from datetime import datetime

START_DATE = "2030-01-01"
END_DATE = "2032-12-22"
EMPRESA = "MH Refeições"

mes_peso = {
    1: 1.2,
    2: 1.3,
    3: 1.0,
    4: 1.1,
    5: 1.1,
    6: 1.2,
    7: 1.4,
    8: 1.3,
    9: 1.3,
    10: 1.2,
    11: 1.1,
    12: 1.3
}

def fds(data):
    return data.weekday() >= 5

datas = pd.date_range(start=START_DATE, end=END_DATE, freq="D")

linhas = []
for data in datas:
    for servico in ["Grupo Tamburi", "Vantage", "Rondon R/R", "Elisa Agro"]:
        empresa = EMPRESA
        cmv = 1
        data_str = data.strftime("%Y-%m-%d")

        if servico == "Grupo Tamburi":
            if fds:
                valor_base = np.random.randint(20, 30) * 22
            else:
                valor_base = np.random.randint(40, 60) * 22

        elif servico == "Vantage":
            if fds:
                valor_base = np.random.randint(4, 6) * 25
            else:
                valor_base = np.random.randint(6, 8) * 25

        elif servico == "Rondon R/R":
            if fds:
                valor_base = np.random.randint(0, 2) * 20
            else:
                valor_base = np.random.randint(4, 8) * 20

        elif servico == "Elisa Agro":
            if fds:
                valor_base = np.random.randint(10, 20) * 20
            else:
                valor_base = np.random.randint(20, 40) * 20    

        peso = mes_peso.get(data.month, 1.0)
        valor = int(valor_base * peso)

        linhas.append({
            "data": data_str,
            "empresa": empresa,
            "servico": servico,
            "cmv": cmv,
            "valor": valor
        })

df = pd.DataFrame(linhas)

df.to_csv("bi-rafatrindade/mh/mh_faturamento.csv", index=False, sep=";", encoding="utf-8-sig")

print("Arquivo 'mh_faturamento.csv' gerado com sucesso!")
