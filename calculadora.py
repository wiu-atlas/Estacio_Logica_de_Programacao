#Calculadora para Análise de Eficiência Energética de Edifícios
#Desenvolvido por: Wilson

print("\nAnálise de Eficiência Energética de Edifícios")
print("         Lógica de Programação - Estácio de Sá, 2026")

def analisar_eficiencia_energetica():
    print("Insira os dados do edifício para análise:")
    

#Dados Básicos
area = float(input("\n\n1. Área total construída do edifício (m²): "))
andares = int(input("2. Número de andares: "))
ocupantes = int(input("3. Número médio de ocupantes: "))



#Iluminação
print("\n\n4. Tipo de iluminação predominante (LED, Fluorescente, Incandescente): ")
print("1 - LED")
print("2 - Fluorescente")
print("3 - Incandescente")
iluminacao = int(input("\nSelecione o tipo de iluminação (1~3): "))
if iluminacao == 1:
    tipo_iluminacao = "LED"
elif iluminacao == 2:
    tipo_iluminacao = "Fluorescente"
elif iluminacao == 3:
    tipo_iluminacao = "Incandescente"



#Ar Condicionado / Climatização
print("\n\n5. Sistema de climatização: ")
print("1 - Nenhum")
print("2 - Ar condicionado split")
print("3 - Ar condicionado central")
climatizacao = int(input("\nSelecione o sistema de climatização (1~3): "))
if climatizacao == 1:
    tipo_climatizacao = "Nenhum"
elif climatizacao == 2:
    tipo_climatizacao = "Ar condicionado split"
elif climatizacao == 3:
    tipo_climatizacao = "Ar condicionado central"



#Isolamento e Janelas
print("\n\n6. Qualidade de isolamento e janelas: ")
print("1 - Precária (janelas simples, sem isolamento)")
print("2 - Decente (janelas duplas, isolamento mínimo)")
print("3 - Boa (janelas duplas ou triplas, isolamento moderado)")
isolamento = int(input("Escolha entre as opções acima (1~3): "))



#Consumo (Atual) Médio de Energia
consumo_mensal = float(input("\n\n7. Consumo médio mensal de energia (kWh): "))