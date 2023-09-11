#Instruções
#Crie um tipo abstrato de dado (TAD) para manipular números complexos na
#linguagem Python. O método deve:
#- calcular três números complexos;
#- realizar todas as operações básicas;
#- e imprimir as propriedades real e img do números

if __name__ =='__main__':
    a = 1 + 2j
    b = complex(3,4)
    c = complex(4,1)

    print('primeiro numero complexo: ', a)
    print('segundo numero complexo: ', b)
    print('terceiro numero complexo: ', c)

    print('tipo do primeiro numero complexo ',type(a))
    print('tipo do segundo numero complexo ',type(b))
    print('tipo do terceiro numero complexo ',type(c))

    print('parte real do primeiro numero complexo ', a.real)
    print('parte imaginaria do primeiro numero complexo ', a.imag)
    print('parte real do segundo numero complexo ', b.real)
    print('parte imaginaria do segundo numero complexo ', b.imag)
    print('parte real do terceiro numero complexo ', c.real)
    print('parte imaginaria do terceiro numero complexo ', c.imag)

    print('soma de dos numeros complexos 1 e 2' ,a + b)
    print('subtração de dos numeros complexos 1 e 2' , a - b)
    print('multiplicação dos numeros complexos 1 e 2' , a * b)
    print('divisao dos numeros complexos 1 e 2' , a / b)

    print('soma de dos numeros complexos 1 e 3' ,a + c)
    print('subtração de dos numeros complexos 1 e 3' , a - c)
    print('multiplicação dos numeros complexos 1 e 3' , a * c)
    print('divisao dos numeros complexos 1 e 3' , a / c)
    
    print('fim do teste dos numeros complexo')
