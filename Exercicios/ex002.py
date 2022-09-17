# Eu posso realizar a 'formatação' do print usando o '.format()', neste caso eu posso escrever o print completo e onde eu quero que o programa chame o dado que foi capturado pelo input eu abro e fecho chaves no local '{}' e no final da String, quando eu fechar as aspas eu coloco '.format(variável)' desse modo o nome caputador pelo input vai ser inserido no local que eu defini as chaves.

nome = input('Por favor, digite seu nome: \n')
print ('Olá {} seja muito bem vindo(a) ao curso de Python do Curso em Vídeo!'.format(nome))
