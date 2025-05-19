from ferramentas.data import *
from time import sleep

while True:
     resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do sistema'])
     if resposta == 1:
          menu_cadastros()
     elif resposta == 2:
          menu_adicionar()
     elif resposta == 3:
          título('Saindo do sistema... Até logo!')
          break
     else:
          print('\033[31mERRO! Digite uma opção válida!\033[m')
     sleep(1.5)