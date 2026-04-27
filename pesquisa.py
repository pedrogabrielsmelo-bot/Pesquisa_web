# Programa de Pesquisa de Opinião - TudoWeb

# Contadores para respostas
qtd_excelente = 0
qtd_ruim = 0

# Estrutura de repetição FOR para 10 entrevistados
for i in range(1, 11):
    print(f"\nEntrevistado {i}")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Digite sua opinião (1/2/3): "))

    # Estrutura de decisão para verificar opinião
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1

# Exibição dos resultados finais
print("\nRESULTADOS DA PESQUISA")
print(f"Quantidade de respostas EXCELENTE: {qtd_excelente}")
print(f"Quantidade de respostas RUIM: {qtd_ruim}")
