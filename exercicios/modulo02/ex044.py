print('{:=^30}'.format(' LOJAS '))
#print(f'{" LOJAS DO SHOKI ":=^30}')
produto = float(input('Digite o preço do produto: R$'))
pagamento = str(input('FORMAS DE PAGAMENTO'
                      '\n[ 1 ] À vista dinheiro/cheque'
                      '\n[ 2 ] À vista no Cartão'
                      '\n[ 3 ] 2x no cartão'
                      '\n[ 4 ] 3x ou mais no cartão.'
                      '\nEscolha a condição de pagamento 1, 2, 3 ou 4: ')).strip().upper()
print('\033[4m=-=-= Condições de pagamento: =-=-=\033[m')
if pagamento == '1':
    total = produto - (produto * 10 / 100)
    print('À vista (Dinheiro/Cheque) (15%): - \033[4;32mR${:.2f}\033[m'.format(total))
elif pagamento == '2':
    total = produto - (produto * 5 / 100)
    print('À vista (Cartão) (5%): - - - - - - \033[4;32mR${:.2f}\033[m'.format(total))
elif pagamento == '3':
    total = produto / 2
    print('Em até 2x no cartão: - - - - - - - \033[4;32mR${:.2f}\033[m'.format(total))
elif pagamento == '4':
    total = produto + (produto * 20 / 100)
    parce = int(input('Quantas parcelas? '))
    totparc = total / parce
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parce, totparc))
    print('3x ou mais no cartão:- - - - - - - \033[4;32mR${:.2f}\033[m'.format(total))