# ==========================================
# ANÁLISE SIMPLES DE EFICIÊNCIA ENERGÉTICA
# ==========================================



import Function_Calc_Eficiencia



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

    area = Function_Calc_Eficiencia.ler_numero_positivo(
        "Digite a área do edifício em m²: "
    )

    num_andares = Function_Calc_Eficiencia.ler_inteiro_positivo(
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

    # Voltar ao início
    voltar_inicio = False

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

            if i > 1:
                i -= 1 # Volta para o andar anterior
                print("Voltando ao início...\n")
            else:
                print("Você já está no início.\n")

            continue



        # ============================
        # OPÇÃO 1 - MANUAL
        # ============================

        if opcao == 1:

            consumo_andar = Function_Calc_Eficiencia.ler_numero_positivo(
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

            qtd_lampadas = Function_Calc_Eficiencia.ler_inteiro_nao_negativo(
                "Quantidade de lâmpadas LED: "
            )

            if qtd_lampadas > 0:

                horas_lampadas = Function_Calc_Eficiencia.ler_numero_positivo(
                    "Horas por dia das lâmpadas: "
                )

                consumo_andar += Function_Calc_Eficiencia.consumo_energia(
                    "lampada(LED)",
                    horas_lampadas
                ) * qtd_lampadas



            # ============================
            # TVs
            # ============================

            qtd_tv = Function_Calc_Eficiencia.ler_inteiro_nao_negativo(
                "Quantidade de TVs: "
            )

            if qtd_tv > 0:

                horas_tv = Function_Calc_Eficiencia.ler_numero_positivo(
                    "Horas por dia das TVs: "
                )

                consumo_andar += Function_Calc_Eficiencia.consumo_energia(
                    "TV",
                    horas_tv
                ) * qtd_tv



            # ============================
            # COMPUTADORES
            # ============================

            qtd_pc = Function_Calc_Eficiencia.ler_inteiro_nao_negativo(
                "Quantidade de computadores: "
            )

            if qtd_pc > 0:

                horas_pc = Function_Calc_Eficiencia.ler_numero_positivo(
                    "Horas por dia dos computadores: "
                )

                consumo_andar += Function_Calc_Eficiencia.consumo_energia(
                    "computador(desktop)",
                    horas_pc
                ) * qtd_pc



            # ============================
            # Ar-Condicionado
            # ============================
            qtd_ac = Function_Calc_Eficiencia.ler_inteiro_nao_negativo(
                "Quantidade de ar-condicionados: "
            )

            if qtd_ac > 0:
                horas_ac = Function_Calc_Eficiencia.ler_numero_positivo(
                    "Horas por dia dos ar-condicionados: "
                )

                consumo_andar += Function_Calc_Eficiencia.consumo_energia(
                    "ar-condicionado(1200BTU)",
                    horas_ac
                ) * qtd_ac



            # ============================
            # Notebook
            # ============================
            qtd_note = Function_Calc_Eficiencia.ler_inteiro_nao_negativo(
                "Quantidade de notebooks: "
            )

            if qtd_note > 0:
                horas_note = Function_Calc_Eficiencia.ler_numero_positivo(
                    "Horas por dia dos notebooks: "
                )

                consumo_andar += Function_Calc_Eficiencia.consumo_energia(
                    "notebook",
                    horas_note
                ) * qtd_note



            # ============================
            # geladeira
            # ============================
            qtd_gel = Function_Calc_Eficiencia.ler_inteiro_nao_negativo(
                "Quantidade de geladeiras: "
            )

            if qtd_gel > 0:
                horas_gel = Function_Calc_Eficiencia.ler_numero_positivo(
                    "Horas por dia da geladeira: "
                )

                consumo_andar += Function_Calc_Eficiencia.consumo_energia(
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

    if voltar_inicio:
        continue

    eficiencia = consumo_total / area

    classificacao = Function_Calc_Eficiencia.classificar_eficiencia(
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

    Function_Calc_Eficiencia.mostrar_recomendacao(classificacao)

    continuar = input(
        "\nDeseja rodar o programa novamente? (S/N): "
    )

print("\nPrograma encerrado.")