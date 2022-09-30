frase = 'Curso em Vídeo Python'
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase)) #Conta a quantidade de caracteres na frase
print(frase.count('o')) #Vai contar quantas vezes aparece a letra 'o' minúsculo
print(frase.count('O')) #Vai contar quantas vezes aparece a letra 'O' maiúsculo
print(frase.upper().count('O')) 
print(frase.count('o',0,13)) #Conta a quantidade de vezes que a letra 'o' aparece, mas com fatiamento junto
print(frase.find('deo')) #Encontra onde começa o termo 'deo'
print(frase.find('Android')) 
print('Curso' in frase) #Retorna um boolean, se existe ou não aquela palavra na variável, neste caso TRUE
print(frase.replace('Python', 'Android')) #Aqui substitui a primeira palavra pela segunda, mas apenas no print, não muda a string
print(frase)
frase = frase.replace('Python', 'Android') #Agora consigo alterar minha frase usando o replace e ela foi alterada de fato, não apenas no print, mas na variável.
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase = '   Aprenda Python  '
print(len(frase))
print(len(frase.strip())) #Conta quantos caracteres existem na frase, excluindo os espaços antes e depois da frase
print(frase.strip()) #Remove os espaços excedentes antes e depois da String
print(frase.rstrip())
print(frase.lstrip())
frase = 'Curso em Vídeo Python'
print(frase.split()) #Separa as palavras da string em uma lista
dividido = frase.split()
print('-'.join(dividido)) #Junta as strings de uma lista separados eles por um hífen '-'
print(dividido[2])
print(dividido[2][1])
print(frase)

print(''' O que é Lorem Ipsum?
Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e 
de impressos, e vem sendo utilizado desde o século XVI, quando um impressor 
desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de 
modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também 
ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. 
Se popularizou na década de 60, quando a Letraset lançou decalques contendo 
passagens de Lorem Ipsum, e mais recentemente quando passou a ser integrado a 
softwares de editoração eletrônica como Aldus PageMaker.''') 
#Usando três aspas no começo e fechando com três aspas no final um texto bem grande com quebra de linha pode ser impresso normalmente
