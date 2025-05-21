#Formatação com o método format

a = 'A'
b = 'B'
c = 1.1

formato = f'a={2} b={0} c={1:.2f}'.format(a, b, c) # se a chave não tiver o index ela vai depender da ordem a b c, 0 1 e 2
#Se eu adicionar o indice de b na posicao da primeira chave o valor de b vai ser mostrado nela sem importar com a ordem

#Dentro de format temos os parametros, se eum parametro for noemado, todos os próximos devem ser nomeados também
#e no lugar do indice podemos colocar o nome ao inves de numero
print(formato)