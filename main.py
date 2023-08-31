from funcoes import *

print('---------- calculadora ----------')
print('')
print('-----  Digite o número -----')
print('')
print('-----  Digite a operação desejada -----)')
print('')
print('-----  Digite o outro número e visualize o resultado da operação  -----')
print('')

num1 = int(input('_ Número: '))
op = input('_ Operação: ')
if op.isalpha() or op.isnumeric():
    op = input('Operação inválida, digite a operação novamente:')
num2 = int(input('_ Número: '))

if op == '+':
    soma(num1,num2)
    
elif op == '-':
    subtracao(num1, num2)
    
elif op == '*':
    multiplicacao(num1,num2)
    
elif op == '/':
   divisao, (num1, num2)