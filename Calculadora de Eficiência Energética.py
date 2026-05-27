# ==========================================
# ANÁLISE SIMPLES DE EFICIÊNCIA ENERGÉTICA
# ==========================================

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


# =================
# CÓDIGO PRINCIPAL
# =================

continuar = "S"

while continuar.upper() == "S":

    print("======================")
    print("Análise de Eficiência")
    print("======================\n")

    sair = input(
        "Deseja iniciar o programa(S/N): "
    ).upper()

    if sair == "N":
        break

    edificio_nome = input(
        "Digite o nome do edifício: "
    )

    area = ler_numero_positivo(
        "Digite a área do edifício em m²: "
    )

    num_andares = ler_inteiro_positivo(
        "Digite o número de andares: "
    )

    consumos = []
    consumo_total = 0

    print(
        "\nDigite o consumo de energia "
        "de cada andar:\n"
    )

    # CONTROLE MANUAL DOS ANDARES
    i = 1

    while i <= num_andares:

        print(f"\n===== Andar {i} =====")

        # ============================
        # MENU DE OPÇÕES
        # ============================

        while True:

            print(
                "\nComo deseja informar "
                "o consumo do andar?"
            )

            print("1 - Digitar consumo manualmente")
            print("2 - Calcular pelos aparelhos")
            print("0 - Voltar")

            opcao = input(
                "Escolha a opção de "
                "informação de consumo: "
            )

            if opcao in ["0", "1", "2"]:
                opcao = int(opcao)
                break

            else:
                print("Opção inválida.\n")

        # ============================
        # VOLTAR
        # ============================

        if opcao == 0:

            print(
                "Voltando para o mesmo andar...\n"
            )

            continue

        # ============================
        # OPÇÃO 1 - MANUAL
        # ============================

        if opcao == 1:

            consumo_andar = ler_numero_positivo(
                f"Consumo do andar {i}: "
            )

        # ============================
        # OPÇÃO 2 - APARELHOS
        # ============================

        elif opcao == 2:

            consumo_andar = 0

            # ============================
            # LÂMPADAS
            # ============================

            print("\n=====================================")
            print("Os aparelhos possuem valores aproximados: ")
            print("-Lâmpada: 12W")
            print("-Ar-Condicionado(12000BTU): 1200W")
            print("-Computador(Desktop): 300W")
            print("-TV: 100W")
            print("-Notebook: 80W")
            print("-Geladeira: 150W")
            print("=====================================\n")

            qtd_lampadas = ler_inteiro_nao_negativo(
                "Quantidade de lâmpadas LED: "
            )

            if qtd_lampadas > 0:

                horas_lampadas = ler_numero_positivo(
                    "Horas por dia das lâmpadas: "
                )

                consumo_andar += consumo_energia(
                    "lampada(LED)",
                    horas_lampadas
                ) * qtd_lampadas

            # ============================
            # TVs
            # ============================

            qtd_tv = ler_inteiro_nao_negativo(
                "Quantidade de TVs: "
            )

            if qtd_tv > 0:

                horas_tv = ler_numero_positivo(
                    "Horas por dia das TVs: "
                )

                consumo_andar += consumo_energia(
                    "TV",
                    horas_tv
                ) * qtd_tv

            # ============================
            # COMPUTADORES
            # ============================

            qtd_pc = ler_inteiro_nao_negativo(
                "Quantidade de computadores: "
            )

            if qtd_pc > 0:

                horas_pc = ler_numero_positivo(
                    "Horas por dia dos computadores: "
                )

                consumo_andar += consumo_energia(
                    "computador(desktop)",
                    horas_pc
                ) * qtd_pc

            # ============================
            # Ar-Condicionado
            # ============================
            qtd_ac = ler_inteiro_positivo(
                "Quantidade de ar-condicionados: "
            )

            horas_ac = ler_numero_positivo(
                "Horas por dia dos ar-condicionados: "
            )

            consumo_andar += consumo_energia(
                "ar-condicionado(1200BTU)",
                horas_ac
            ) * qtd_ac

            # ============================
            # Notebook
            # ============================
            qtd_note = ler_inteiro_positivo(
                "Quantidade de notebooks: "
            )

            horas_note = ler_numero_positivo(
                "Horas por dia dos notebooks: "
            )

            consumo_andar += consumo_energia(
                "notebook",
                horas_note
            ) * qtd_note

            # ============================
            # geladeira
            # ============================
            qtd_gel = ler_inteiro_positivo(
                "Quantidade de geladeiras: "
            )

            horas_gel = ler_numero_positivo(
                "Horas por dia da geladeira: "
            )

            consumo_andar += consumo_energia(
                "geladeira",
                horas_gel
            ) * qtd_gel

        # ============================
        # SALVAR CONSUMO
        # ============================

        consumos.append(consumo_andar)

        consumo_total += consumo_andar

        print(
            f"Consumo do andar {i}: "
            f"{consumo_andar:.2f} kWh"
        )

        i += 1 # Avança para o próximo andar

    eficiencia = consumo_total / area

    classificacao = classificar_eficiencia(
        eficiencia
    )

    # ============================
    # RELATÓRIO
    # ============================

    print("\n=========== RELATÓRIO ===========")

    print(f"Edifício: {edificio_nome}")

    print(f"Área: {area:.2f} m²")

    print(
        f"Quantidade de andares: "
        f"{num_andares}"
    )

    print(
        f"Consumo total: "
        f"{consumo_total:.2f} kWh"
    )

    print(
        f"Índice de eficiência: "
        f"{eficiencia:.2f}"
    )

    print(
        f"Classificação: "
        f"{classificacao}"
    )

    if num_andares > 0:

        maior_consumo = max(consumos)
        menor_consumo = min(consumos)

        andar_maior = consumos.index(
            maior_consumo
        ) + 1

        andar_menor = consumos.index(
            menor_consumo
        ) + 1

        print(
            f"Andar com maior consumo: "
            f"Andar {andar_maior} "
            f"({maior_consumo:.2f} kWh)"
        )

        print(
            f"Andar com menor consumo: "
            f"Andar {andar_menor} "
            f"({menor_consumo:.2f} kWh)"
        )

    mostrar_recomendacao(classificacao)

    continuar = input(
        "\nDeseja rodar o programa novamente? (S/N): "
    )

print("\nPrograma encerrado.")