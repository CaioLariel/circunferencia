from ast import Break


print('vamos fazer circunferência')
inicio = int(input('''qual função vc gostaria de fazer?
[1]saber o comprimento da circunferência
[2]saber o diâmetro/raio
            
'''))
if inicio == 1:
    a = int(input('''vc tem o valor do raio ou diâmetro?
            [1]raio
            [2]diâmetro
            '''))
    if a == 1:
        b = float(input('qual valor do raio?:'))
        comprimento = 6.28 * b
        print('o valor do comprimento é  {:.2f}'.format(comprimento))

    elif a == 2:
        d = float(input('qual valor do diâmetro ?:'))
        conta = 6.28 * (d / 2)
        print('o valor do comprimento é {:.2f}'.format(conta))

if inicio == 2:
    a = float(input('qual valor do comprimento?:'))
    r = a / 6.18
    t = (a / 6.18) * 2
    print('o valor do raio é {:.2f}'.format(r))
    print('o valor do diâmetro é {:.2f}'.format(t))

a = (input("fim, aperte enter para fechar."))
Break