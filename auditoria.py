import pandas as pd

dados = pd.read_excel("Auditoria.xlsx")

print(dados)

ruim = 0
regular = 0
bom = 0
otimo = 0
na = 0

for coluna in dados.columns:
    
    for resposta in dados[coluna]:
        
        if resposta == "Ruim":
            ruim += 1
            
        elif resposta == "Regular":
            regular += 1
            
        elif resposta == "Bom":
            bom += 1
            
        elif resposta == "Ótimo":
            otimo += 1
            
        elif resposta == "NA":
            na += 1

print("Resultado da Auditoria")
print("Ruim:", ruim)
print("Regular:", regular)
print("Bom:", bom)
print("Ótimo:", otimo)
print("NA:", na)





































# print("Sistema de Avaliação Auditoria 5S")

# respostas = [
# "Regular",
# "Bom",
# "Otimo",
# "N/A",
# ]

# Ruim = 0
# Regular = 0
# Bom = 0
# Otimo = 0
# NA = 0

# for resposta in respostas:

#     if resposta == "Ruim":
#         Ruim = Ruim + 1

#     elif resposta == "Regular":
#         Regular = Regular + 1

#     elif resposta == "Bom":
#         Bom = Bom + 1

#     elif resposta == "Otimo":
#         Otimo = Otimo + 1

#     elif resposta == "N/A":
#         NA = NA + 1

# print("Resultado da Auditoria")
# print("Ruim: ", Ruim)
# print("Regular: ", Regular)
# print("Bom: ", Bom)
# print("NA: ", NA)



