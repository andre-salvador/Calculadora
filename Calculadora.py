def calculos():
    print(' soma (+) \n subtracao (-) \n multiplicacao (*) \n divisao (/) \n potencia (**)')

    calculadora = input('Qual conta você deseja fazer? ')
    if calculadora == 'soma' or calculadora == '+':
        resultado = n1 + n2
        print(f'a soma de {n1} e {n2} é: {resultado}')
    elif calculadora == 'subtracao'or calculadora == '-':
        resultado = n1 - n2
        print(f'a subtração de {n1} e {n2} é: {resultado}')
    elif calculadora == 'multiplicacao'or calculadora == '*':
        resultado = n1 * n2
        print(f'a multiplicacao de {n1} e {n2} é: {resultado}')
    elif calculadora == 'divisao'or calculadora == '/':
        resultado = n1 / n2
        print(f'a divisao de {n1} e {n2} é: {resultado}')
    else:
        resultado = n1 ** n2
        print(f'a potencia de {n1} e {n2} é: {resultado}')
    
    return resultado

print('Calculadora em Python')

while True:

    print(' inteiro \n quebrados')
    estilo = input('Você quer realizar contas em qual estilo de numero? ')
    n1 = int(input('Qual é o primeiro numero? '))
    n2 = int(input('Qual é o segundo numero? '))


    if estilo == 'inteiro'or estilo == 'int':
        calculos()

    elif estilo == 'quebrados'or estilo == 'float':
        calculos()

    denovo = input('Deseja calcular novamente? S/N \n').upper()

    if denovo == 'S':
        pass
    else:
        print('Obrigado por usar nossa calculadora :)')
        exit()
