Grupo: Wilson Pombo(202602687542), Daniel Souza(202508172585), Luiz Felipe de Sousa(202603508803), André Lessa(202302233155), Ruan Assunção(202211393338)
Matéria: Lógica de Programação
Tema: Calculadora de Eficiência Energética

A Calculadora de Eficiência Energética é um projeto desenvolvido em Python para analisar o consumo de energia elétrica em edifícios.

O sistema permite cadastrar informações como área do edifício, quantidade de andares e consumo energético de cada andar. 
Com base nesses dados, é calculado um índice de eficiência energética, além da geração de recomendações para redução de consumo.

*Objetivos:
>Calcular o consumo total de energia;
>Avaliar a eficiência energética do edifício;
>Identificar andares com maior e menor consumo;
>Fornecer recomendações de melhoria.

*Como Funciona:

O programa solicita:
>Nome do edifício;
>Área total (m²);
>Quantidade de andares;
>Consumo energético de cada andar.

O consumo pode ser informado manualmente ou calculado automaticamente a partir da quantidade e tempo de uso de equipamentos como:
>Lâmpadas LED;
>TVs;
>Computadores;
>Notebooks;
>Geladeiras;
>Ar-condicionados.

Ao final, o sistema gera um relatório contendo o consumo total, índice de eficiência, classificação energética e recomendações.

Etapas:
1ª: Iniciar o programa, selecione "S" para iniciar o programa;

2ª: Nomeio o edifício. Exemplo: "Estácio";

3ª: Digite a área do edifício(m²). Ex: "400";

4ª: Digite o número de andares: Ex: "4";

5ª: Feito isso, virão as opções individuais, andar por andar. (Esse menu se repetirá baseado na quantidade de andares que você informou no programa.);

6ª: Nesse menu, você poderá selecionar se quer informar o consumo manualmente ou se deseja calcular pelos aparelhos de cada andar.
==> Caso deseje informar manualmente, você deverá informar o consumo completo de cada andar. Ex: 500 kWh;
==> Caso deseje informar baseado em cada aparelho que possue por andar, deverá informar a quantidade de cada aparelho de cada andar e a quantidade de horas por dia que esses aparelhos são utilizados.

Ao colocar todas essas informações, o programa retornará uma avaliação. Caso o consumo seja considerado bom, ele terá
Após informar o consumo para cada andar, no final é enviado um relatório de acordo com o cálculo de efiência, se o usuário tiver selecionado para digitar o consumo total por andar manualmente o cálculo usado será a soma de todos os andares, se selecionar para descrever o consumo dos andares de acordo com os aparelhos o cálculo será (potência_de_cada_aparelho*horas_por_dia * 30)/1000. No relatório é mostrado a área total do edifício, quantidade de andares, consumo total do edifício, consumo de eficiência(consumo_total/área), classificação de eficiência e separando qual dos andares tem o menor e o maior consumo.
