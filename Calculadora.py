def calculos():
    print(' soma (+) \n subtracao (-) \n multiplicacao (*) \n divisao (/) \n potencia (**)')

    calculadora = input('Qual conta você deseja fazer? ')
    if calculadora == 'soma' or calculadora == '+':
        resultado = n1 + n2
        print(f'a soma de {n1} e {n2} é: {resultado:.4f}')
    elif calculadora == 'subtracao'or calculadora == '-':
        resultado = n1 - n2
        print(f'a subtração de {n1} e {n2} é: {resultado:.4f}')
    elif calculadora == 'multiplicacao'or calculadora == '*':
        resultado = n1 * n2
        print(f'a multiplicacao de {n1} e {n2} é: {resultado:.4f}')
    elif calculadora == 'divisao'or calculadora == '/':
        resultado = n1 / n2
        print(f'a divisao de {n1} e {n2} é: {resultado:.4f}')
    else:
        resultado = n1 ** n2
        print(f'a potencia de {n1} e {n2} é: {resultado:.4f}')
    
    return resultado

print('Calculadora em Python')

while True:

    n1 = float(input('Qual é o primeiro numero? '))
    n2 = float(input('Qual é o segundo numero? '))

    calculos()

    denovo = input('Deseja calcular novamente? S/N \n').upper()

    if denovo == 'S':
        pass
    else:
        print('Obrigado por usar nossa calculadora :)')
        exit()
