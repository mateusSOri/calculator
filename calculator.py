numb1 = 0
numb2 = 0
result = 0
op = ''

while True:
    numb1 = float(input('First number: '))  # Read the first number as a float
    op = input('Enter the mathematical operation (+, -, *, /) or "exit" to quit: ')
    
    # Check condition to exit the loop
    if op.lower() == 'exit':
        print("Exiting the calculator.")
        break
    
    numb2 = float(input('Second number: '))
    
    # Perform the operation based on the operator provided
    if op == '+':
        result = numb1 + numb2
    elif op == '-':
        result = numb1 - numb2
    elif op == '/':
        if numb2 != 0:
            result = numb1 / numb2
        else:
            print('Error: Division by zero!')
            continue  # Skip this iteration and restart the loop
    elif op == '*':
        result = numb1 * numb2
    else:
        print('Unrecognized operation!')
        continue  # Skip this iteration and restart the loop

    # Show the result
    print(f'{numb1} {op} {numb2} = {result}')