# Funções auxiliares
from time import sleep
from operacoes import *

def ler_vetor(dimensao, nome='vetor'):
    while True:
        try:
            entrada = input(f"\nDigite as coordenadas do {nome} separadas por espaço: ").strip().split()
            if len(entrada) != dimensao:
                print(f"  >> Erro: Digite exatamente {dimensao} valores.")
                continue
            vetor = [float(x) for x in entrada]
            return vetor
        except ValueError:
            print("  >> Erro: Certifique-se de digitar apenas números.")

def exibir_resultado(vetor_resultado):
    print("\nResultado:")
    print("  ->", vetor_resultado)

while True:
    # Início do programa
    print('\n' + '=' * 50)
    print(f"{'CALCULADORA DE VETORES':^50}")
    print('=' * 50)

    # Tipos de vetores
    print('\nSelecione o tipo de vetor:')
    print('  [ B ] Bidimensional (2D)')
    print('  [ T ] Tridimensional (3D)')

    # Escolha do tipo de vetor
    while True:
        tipo = input('\nDigite o tipo do vetor (B ou T): ').strip().upper()
        if tipo in ['B', 'T']:
            break
        elif tipo.isdigit():
            print('  >> Entrada inválida: use apenas [ B ] ou [ T ].')
        else:
            print('  >> Tipo inválido. Tente novamente.')

    # Menu de operações
    sleep(0.2)
    print('\n' + '-' * 50)
    print(f"{'OPERAÇÕES DISPONÍVEIS':^50}")
    print('-' * 50)
    print('  [ 1 ] Adição')
    print('  [ 2 ] Subtração')
    print('  [ 3 ] Produto por Escalar')
    print('  [ 4 ] Produto Interno (Escalar)')
    print('  [ 5 ] Produto Vetorial (somente 3D)')
    print('  [ 6 ] Produto Misto (somente 3D)')
    print('  [ 0 ] Sair da Calculadora')

    # Escolha da operação
    while True:
        entrada = input('\nInforme o número da operação desejada (0 a 6): ').strip()
        if entrada.isdigit():
            operacao = int(entrada)
            if 0 <= operacao <= 6:
                if tipo == 'B' and operacao in [5, 6]:
                    print("  >> Erro: Esta operação está disponível apenas para vetores 3D.")
                    continue
                break
            else:
                print('  >> Número fora do intervalo. Digite de 0 a 6.')
        else:
            print('  >> Entrada inválida. Digite apenas um número.')

    # Define a dimensão com base no tipo escolhido
    dim = 2 if tipo == 'B' else 3

    # Executa a operação escolhida
    if operacao == 1:
        v1 = ler_vetor(dim, 'vetor A')
        v2 = ler_vetor(dim, 'vetor B')
        resultado = somar_vetores(v1, v2)
        exibir_resultado(resultado)

    elif operacao == 2:
        v1 = ler_vetor(dim, 'vetor A')
        v2 = ler_vetor(dim, 'vetor B')
        resultado = subtrair_vetores(v1, v2)
        exibir_resultado(resultado)

    elif operacao == 3:
        v = ler_vetor(dim, 'vetor')
        while True:
            try:
                escalar = float(input("Digite o valor do escalar: "))
                break
            except ValueError:
                print("  >> Entrada inválida. Digite um número real.")
        resultado = multiplicar_por_escalar(v, escalar)
        exibir_resultado(resultado)

    elif operacao == 4:
        v1 = ler_vetor(dim, 'vetor A')
        v2 = ler_vetor(dim, 'vetor B')
        if len(v1) != len(v2):
            print("  >> Erro: Vetores com dimensões diferentes.")
        else:
            resultado = produto_interno(v1, v2)
            print("\nProduto Interno (Escalar):", resultado)

    elif operacao == 5:
        v1 = ler_vetor(3, 'vetor A')
        v2 = ler_vetor(3, 'vetor B')
        resultado = produto_vetorial(v1, v2)
        print("\nProduto Vetorial:", resultado)

    elif operacao == 6:
        print("\nProduto Misto (Somente para vetores 3D):")

        # Coletando os vetores A, B e C para o produto misto
        v1 = ler_vetor(3, 'vetor A')
        v2 = ler_vetor(3, 'vetor B')
        v3 = ler_vetor(3, 'vetor C')

        resultado = produto_misto(v1, v2, v3)

        if resultado == 0:
            print(f'O produto misto entre os vetores A, B e C é: {resultado:.0f}')
            print(f'Os vetores são complanares (estão no mesmo plano).')
        else:
            print(f'O produto misto entre os vetores A, B e C é: {resultado:.0f} unidades de volume.')

    elif operacao == 0:
        print('\n' + '=' * 50)
        print(f"{'FIM DO PROGRAMA':^50}")
        print('=' * 50 + '\n')
        break

    else:
        print('Operação inválida! Escolha outra opção [0 a 6]')