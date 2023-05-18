from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}' )
if idade == 18:
    print('Voce tem que se Alistar IMEDIATAMENTE! ')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda Faltam {saldo} para o Alistamente! ')
    ano = atual + saldo
    print(f'Seu Alistamento será em {ano}!')
elif idade > 18:
    saldo = idade - 18
    print(f'Voce deveria ter se alistado há {saldo} anos! ')
    ano = atual - saldo
    print(f'Seu Alistmento foi em {ano}! ')

