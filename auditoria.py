import pandas as pd

# ler planilha
df = pd.read_excel("auditoria5S.xlsx")

print(df.columns)

resultados = [] # criar uma lista vazia

# percorrer cada auditoria (cada linha)
for index, linha in df.iterrows():

    area = linha["Qual é o local que está auditando?"]

    ruim = 0
    regular = 0
    bom = 0
    otimo = 0
    na = 0

    # pegar respostas das perguntas
    respostas = linha[8:30]  # começa na pergunta 1

    for resposta in respostas:
        
        if pd.isna(resposta):
            na += 1

        elif resposta == "Ruim":
            ruim += 1

        elif resposta == "Regular":
            regular += 1

        elif resposta == "Bom":
            bom += 1

        elif resposta == "Ótimo":
            otimo += 1

    resultados.append({
    "Qual é o local que está auditando?": area,
    "Ruim": ruim,
    "Regular": regular,
    "Bom": bom,
    "Ótimo": otimo,
    "NA": na
})

    print("Auditoria", index + 1)
    print("Ruim:", ruim)
    print("Regular:", regular)
    print("Bom:", bom)
    print("Ótimo:", otimo)
    print("N/A:", na)
    print("---------------------")

    df_resultado = pd.DataFrame(resultados)

    df_resultado.to_excel("resultado_auditorias.xlsx", index=False)

    print("Relatório gerado: resultado_auditorias.xlsx")