numb1 = 0
numb2 = 0
resultado = 0
op = ''

while True:
    numb1 = float(input('Primeiro número: '))  # Ler o primeiro número em ponto flutuante
    op = input('Digite a operação matemática (+, -, *, /) ou "sair" para encerrar: ')
    
    # Verificar condição para sair do loop
    if op.lower() == 'sair':
        print("Saindo da calculadora.")
        break
    
    numb2 = float(input('Segundo número: '))
    
    # Realizar a operação com base no operador fornecido
    if op == '+':
        resultado = numb1 + numb2
    elif op == '-':
        resultado = numb1 - numb2
    elif op == '/':
        if numb2 != 0:
            resultado = numb1 / numb2
        else:
            print('Erro: Divisão por zero!')
            continue  # Pular a iteração atual e voltar ao início
    elif op == '*':
        resultado = numb1 * numb2
    else:
        print('Operação não reconhecida!')
        continue  # Pular a iteração atual e voltar ao início

    # Mostrar o resultado
    print(f'{numb1} {op} {numb2} = {resultado}')