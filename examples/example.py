print("Hello World")
#  LISTAS

print('--> LISTAS <--')
fighters = ['Bud', 'Chuck', 'Bruce']

print(fighters)
fighters[1] = 'Chuck Norris'
print('Segundo elemento de la lista:', fighters[1])

fighters.append('Goku')
print('Lista con goku al final', fighters)
print('Ultimo elemento de la lista', fighters[-1])
print('Elementos intermedios de la lista:', fighters[1:-1])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Del 2 al 6:', numbers[2:7])
print('Mayores que 4 (del 5 al final):', numbers[5:])
print('Menores que 4 (desde el princio hasta el 4):', numbers[:4])
print('Pares:', numbers[::2])  # Es lo mismo que numbers[0:-1:2] Del principio al final de 2 en 2
print('Impares:', numbers[1::2])
print('Al reves', numbers[-1::-1])

#  TUPLAS
print('--> TUPLAS <--')
players = ('Jordan', 'Bryan', 'O\'Neal')
print('Primer jugador:', players[0])
#  players[0] = 'Michael Jordan'  <-- Las tuplas no permiten reasignaciones

#  DICCIONARIOS
print('--> DICCIONARIOS <--')
fighter = {'name': 'Alberto', 'country': 'Spain'}
print('Nombre:', fighter['name'])
print('Pais:', fighter.get('country')) #  <-- Ambos metodos son lo mismo.
#  print('Victorias:', fighter['wins'])  <-- Aqui devolveria una excepcion, el proceso se para.
print('Victorias:', fighter.get('wins', 0))  #  <-- El segundo parametro (opcional) de get es el valor a devolver si no existe la clave
fighter['country'] = 'Italy'


#  OPERADOR IN
print('--> OPERADOR IN <--')
print('Detector de links:', 'http://' in 'Mira este enlace http://google.com')
print('Valores del diccionario:', fighter.values())
print('Valor en diccionario', 'Italy' in fighter.values())

#  FUNCIONES LAMBDA
print('--> FUNCIONES LAMBDA <--')
lambda_exp = lambda n, m : n**m

def exp(n, m):
    return n**m

print('Exponente con lambda:', lambda_exp(2, 3))
print('Exponente con funcion:', exp(2, 3))




