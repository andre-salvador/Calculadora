print('Calculadora em Python')

while True:

    print(' inteiro \n quebrados')
    estilo = input('Você quer realizar contas em qual estilo de numero? ')

    if estilo == 'inteiro':
        n1 = int(input('Qual é o primeiro numero? '))
        n2 = int(input('Qual é o segundo numero? '))

        print('soma \n subtracao \n multiplicacao \n divisao \n potencia')

        calculadora = input('Qual conta você deseja fazer? ')
        if calculadora == 'soma':
            soma = n1 + n2
            print(f'a soma de {n1} e {n2} é: {soma}')
        elif calculadora == 'subtracao':
            subtracao = n1 - n2
            print(f'a subtração de {n1} e {n2} é: {subitracao}')
        elif calculadora == 'multiplicacao':
            multiplicacao = n1 * n2
            print(f'a multiplicacao de {n1} e {n2} é: {multiplicacao}')
        elif calculadora == 'divisao':
            divisao = n1 / n2
            print(f'a divisao de {n1} e {n2} é: {divisao}')
        else:
            potencia = n1 ** n2
            print(f'a potencia de {n1} e {n2} é: {potencia}')

    elif estilo == 'quebrados':
        n1 = float(input('Qual é o primeiro numero? '))
        n2 = float(input('Qual é o segundo numero? '))

        print(' soma \n subtracao \n multiplicacao \n divisao \n potencia')

        calculadora = input('Qual conta você deseja fazer? ')

        if calculadora == 'soma':
            soma = n1 + n2
            print(f'a soma de {n1} e {n2} é: {soma}')
        elif calculadora == 'subtracao':
            subtracao = n1 - n2
            print(f'a subtração de {n1} e {n2} é: {subitracao}')
        elif calculadora == 'multiplicacao':
            multiplicacao = n1 * n2
            print(f'a multiplicacao de {n1} e {n2} é: {multiplicacao}')
        elif calculadora == 'divisao':
            divisao = n1 / n2
            print(f'a divisao de {n1} e {n2} é: {divisao}')
        else:
            potencia = n1 ** n2
            print(f'a potencia de {n1} e {n2} é: {potencia}')
    else:
        print('Escolha entre os numeros inteiros ou quebrados... \n')

    denovo = input('Deseja calcular novamente? S/N \n').upper()

    if denovo == 'S':
        pass
    else:
        print('Obrigado por usar nossa calculadora :)')
        exit()
