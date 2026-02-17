print ('Bem vindo ao assistente virtual da ComercialOn\n')

#print ('\nPara melhor ajudar a atender suas necessidades preciso que você nos informe até quanto está disposto a pagar')

produto = input('Nos informe o produto que você deseja\n')

print ('Pronto, para melhor te atender, vamos fazer o comparativo de preço e marca\n')

marca_01 = input('Digite a marca: ')
preco_01 = float(input('Digite o preço: '))

marca_02 = input('Digite a marca: ')
preco_02 = float(input('Digite o preço: '))

marca_03 = input('Digite a marca: ')
preco_03 = float(input('Digite o preço: '))

if preco_01 > preco_02 and preco_02 > preco_03:
    print (f'O melhor custo benefício no momento para o/a {produto} para você é {preco_03}')

elif preco_02 < preco_01 and preco_01 < preco_03:
    print (f'O melhor custo benefício no momento para o/a {produto} para você é {preco_02}')

elif preco_01 < preco_02 and preco_02 < preco_03:
    print (f'O melhor custo benefício no momento para o/a {produto} para você é {preco_01}')