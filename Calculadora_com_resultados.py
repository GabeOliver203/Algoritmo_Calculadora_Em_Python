resultados = []

def soma(numero1, numero2):
    return numero1 + numero2

def subtrai(numero1, numero2):
    return numero1 - numero2

def multiplica(numero1, numero2):
    return numero1 * numero2

def divide(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        return "Não é possível dividir por zero."

while True:
    print('Menu de opções')
    print('1 - Soma')
    print('2 - Subtrai')
    print('3 - Multiplica')
    print('4 - Divide')
    print('5 - Sair')

    opt = input('Escolha uma opção: ')

    if opt == '5':
        print('Saindo do programa...')
        break

    if opt.isdigit():
        opt = int(opt)

        if opt >= 1 and opt <= 4:
            numero1 = float(input('Insira o primeiro número: '))
            numero2 = float(input('Insira o segundo número: '))

            if opt == 1:
                resultado = soma(numero1, numero2)
            elif opt == 2:
                resultado = subtrai(numero1, numero2)
            elif opt == 3:
                resultado = multiplica(numero1, numero2)
            elif opt == 4:
                resultado = divide(numero1, numero2)

            print('Resultado:', resultado)

            resultados.append(resultado)
            historico = input('Deseja mostrar os resultados até o momento? [S]sim // [N]não ')
            historico = historico.upper()

            if historico == 'S':
                print("Resultados até o momento:", resultados)
            elif historico == 'N':
                continue
            else:
                print("Opção inválida. Por favor, digite 'S' para sim ou 'N' para não.")
        else:
            print('Opção inválida. Digite uma opção válida.')
    else:
        print('Opção inválida. Digite uma opção válida.')