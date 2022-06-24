 
arq = open('registrados.txt', 'a')
print('Olá, Bem vindo a Tela de Cadastro !!')
nome_usuario = input('Digite o seu nome : ')
nome_email = input('Digite o seu Email: ')

arq.write('{}\n'.format(nome_usuario))
arq.write('{}\n'.format(nome_email))



print('Cadastro realizado com sucesso!\n')
print('Bem vindo, {}!'.format(nome_usuario))
arq.close() 