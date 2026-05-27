# ================= FUNÇÕES PRINCIPAIS =================

def ler_numero_positivo(mensagem):

    while True:

        try:
            valor = float(input(mensagem))

            if valor > 0:
                return valor

            else:
                print("Digite um valor maior que 0.")

        except ValueError:
            print("Digite apenas números.")


def ler_inteiro_positivo(mensagem):

    while True:

        try:
            valor = int(input(mensagem))

            if valor > 0:
                return valor

            else:
                print("Digite um número inteiro maior que 0.")

        except ValueError:
            print("Digite apenas números inteiros válidos.")


# Permite valor 0
def ler_inteiro_nao_negativo(mensagem):

    while True:

        try:
            valor = int(input(mensagem))

            if valor >= 0:
                return valor

            else:
                print("Digite um número maior ou igual a 0.")

        except ValueError:
            print("Digite apenas números inteiros válidos.")


def consumo_energia(aparelho, horas_por_dia):

    potencias = {
        "lampada(LED)": 12,
        "ar-condicionado(1200BTU)": 1200,
        "computador(desktop)": 300,
        "TV": 100,
        "notebook": 80,
        "geladeira": 150
    }

    if aparelho not in potencias:

        print("Aparelho não encontrado.")
        return 0

    potencia = potencias[aparelho]

    consumo = (
        potencia * horas_por_dia * 30
    ) / 1000

    return consumo


def classificar_eficiencia(indice):

    if indice < 20:
        return "Muito Eficiente"

    elif indice < 40:
        return "Eficiente"

    elif indice < 60:
        return "Regular"

    else:
        return "Ineficiente"


def mostrar_recomendacao(classificacao):

    print("\nRecomendações:")

    if classificacao == "Muito Eficiente":

        print(
            "- Parabéns! O edifício apresenta ótimo desempenho energético."
        )

    elif classificacao == "Eficiente":

        print("- Manter manutenção preventiva dos sistemas.")
        print("- Continuar utilizando lâmpadas LED.")

    elif classificacao == "Regular":

        print("- Avaliar o uso de iluminação LED.")
        print("- Verificar isolamento térmico.")
        print("- Reduzir desperdícios de energia.")

    else:

        print("- Trocar lâmpadas comuns por LED.")
        print("- Revisar o uso de ar-condicionado.")
        print("- Melhorar isolamento térmico.")
        print("- Fazer inspeção dos equipamentos elétricos.")