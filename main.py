#This calculator program was made by Andre Luiz de Carvalho Oliveira, also known has ALCN!







def normal_calculator():
    interation = ['+', '-', '/', 'x', '*']
    interation2 = ['sim','quero','y','s','yes']
    number1, number2 = float, float

    def contin():
        question2 = input('\nDeseja continuar? \n Digite no seu idioma: ')
        if question2.lower() in interation2:
            interations()
        else:
            exit()

    def apresentation():
        question = input(
            '\nOlá, sou a calculadora! \n Como posso ajudar? \n + : Adição \n - : Subtração \n x : Multiplicação \n / : Divisão \n Digite sua resposta de acordo com o SÍMBOLO CORRESPONDENTE: ')
        return question

    def addition(x, y):
        return x + y

    def subtration(x, y):
        return x - y

    def mutiple(x,y):
        return x*y

    def division(x,y):
        return x/y

    def type():
        a = float(input('\nDigite o 1º Número: '))
        b = float(input('\nDigite o 2º Número: '))
        return [a,b]

    def interations():
        # Firts interaction
        answer = apresentation()

        # Security measure to prevent error
        while answer not in interation:
            print('\n RESPOSTA ERRADA! FAÇA DE NOVO: ')
            answer = apresentation()

        # Where the shit get's done
        if answer.lower() == '+':
            numbers = type()
            number1 = numbers[0]
            number2 = numbers[1]
            soma = addition(number1, number2)
            print(f'\nO resultado da soma entre {number1:.2f} e {number2:.2f} é: ', str(soma))
            contin()


        elif answer.lower() == '-':
            numbers = type()
            number1 = numbers[0]
            number2 = numbers[1]
            sub = subtration(number1, number2)
            print(f'\nO resultado da subtração entre {number1:.2f} e {number2:.2f} é: ', str(sub))
            contin()

        elif answer.lower() == '*':
            numbers = type()
            number1 = numbers[0]
            number2 = numbers[1]
            sub = mutiple(number1, number2)
            print(f'\nO resultado da multiplicação entre {number1:.2f} e {number2:.2f} é: ', str(sub))
            contin()

        elif answer.lower() == '/':
            numbers = type()
            number1 = numbers[0]
            number2 = numbers[1]
            sub = division(number1, number2)
            print(f'\nO resultado da divisão entre {number1:.2f} e {number2:.2f} é: ', str(sub))
            contin()

    interations()


normal_calculator()