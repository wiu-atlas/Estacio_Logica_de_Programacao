from calculadora import *



#Cálculos de Eficiência Energética



#Fatores de Eficiência
fator_iluminacao = [1.8, 1.3, 1.0][iluminacao-1]  # LED, Fluorescente, Incandescente
fator_climatizacao = [0.7, 1.6, 1.0][climatizacao-1]  # Nenhum, Split, Central
fator_isolamento = [1.5, 1.2, 1.0][isolamento-1]  # Precária, Decente, Boa



#Consumo Estimado de Refêrencia (edifício médio)
consumo_referencia = area * 8.5 # kWh/m²/mês (Média no Brasil para edifícios comerciais/residenciais)



#Consumo ajustado pela eficiência
consumo_ajustado = consumo_mensal * fator_iluminacao * fator_climatizacao * fator_isolamento



#Potencial de Economia
economia_percent = max(0, (1 - consumo_ajustado / consumo_referencia) * 100)
economia_reais = consumo_mensal * 0.92 * (economia_percent / 100)  # Considerando o custo médio de R$0,92/kWh



#Classificação de Eficiência (similar ao Procel / Etiqueta Nacional)
if consumo_ajustado < consumo_referencia * 0.65:
    classificacao = "A (Excelente)"
    cor = "Verde Escuro"
elif consumo_ajustado < consumo_referencia * 0.85:
    classificacao = "B (Boa)"
    cor = "Verde Claro"
elif consumo_ajustado < consumo_referencia * 1.1:
    classificacao = "C (Média)"
    cor = "Amarelo"
elif consumo_ajustado < consumo_referencia * 1.4:
    classificacao = "D (Baixa)"
    cor = "Laranja"
else:
    classificacao = "E (Muito Baixa)"
    cor = "Vermelho"