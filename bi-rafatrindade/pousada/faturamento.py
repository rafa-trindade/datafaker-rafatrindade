import pandas as pd
import numpy as np
import requests
from datetime import datetime

####################
# API FERIADOS - https://api.invertexto.com/api-feriados
###################
START_DATE = "2030-01-01"
END_DATE = "2032-12-22"
EMPRESA = "Pousada da Ponte"
UF = "GO"
API_KEY = "22137|SRHoo5bWW93micFMAvCc5fq8d60utocr"

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

def get_feriados(year, uf="GO"):
    url = f"https://api.invertexto.com/v1/holidays/{year}?token={API_KEY}&state={uf}"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        return {f["date"]: f["name"] for f in data}
    else:
        print(f"Erro ao buscar feriados {year}: {resp.text}")
        return {}

# Coletar feriados
feriados = {}
for ano in range(2030, 2036):
    feriados.update(get_feriados(ano, UF))

# Lista de datas
datas = pd.date_range(start=START_DATE, end=END_DATE, freq="D")

linhas = []
for data in datas:
    for servico in ["Hospedagem", "Frigobar"]:
        empresa = EMPRESA
        cmv = 0 if servico == "Hospedagem" else 1
        
        data_str = data.strftime("%Y-%m-%d")
        eh_feriado = 1 if data_str in feriados else 0
        nome_feriado = feriados[data_str] if eh_feriado else "-"
        evento = 0

        # ==========================
        # Obs: FERIDADO ou FDS
        # ==========================
        if eh_feriado:
            obs = "FERIADO"
        elif data.weekday() >= 4:  # sexta=4, sábado=5, domingo=6
            obs = "FDS"
        else:
            obs = "-"

        # ==========================
        # Valor base
        # ==========================
        if servico == "Hospedagem":
            if eh_feriado:
                valor_base = np.random.randint(50, 120) * 10
            else:
                valor_base = np.random.randint(30, 100) * 10

            qtd_hospedes = valor_base // 75

        else:  # Frigobar
            if eh_feriado:
                valor_base = np.random.randint(30, 70) * 10
            else:
                valor_base = np.random.randint(10, 50)
            qtd_hospedes = 0

        # ==========================
        # Aplicar multiplicador mensal
        # ==========================
        peso = mes_peso.get(data.month, 1.0)
        valor = int(valor_base * peso)

        linhas.append({
            "data": data_str,
            "empresa": empresa,
            "servico": servico,
            "cmv": cmv,
            "feriado": eh_feriado,
            "evento": evento,
            "obs": obs,
            "Tipo": nome_feriado,
            "qtd_hospedes": qtd_hospedes,
            "valor": valor
        })

df = pd.DataFrame(linhas)

df.to_csv("bi-rafatrindade/pousada/pousada_faturamento.csv", index=False, sep=";", encoding="utf-8-sig")

print("Arquivo 'pousada_faturamento.csv' gerado com sucesso!")
