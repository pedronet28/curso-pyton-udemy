# ilustracion de el manejo de numeros y operandos con python

num1 = 3
num2 = 7
num3 = 2.5

print(num1 + num2 + num3)
print(num3 - num1 - num2)
print((num1 + num3)* num2) # se respeta la prioriodad de los parentesis!!
print(num1+num2 * num3)  # se respeta la prioridad de los segnos!!

# incremento en python es diferente a java y a otros lenguajes similares 
# incremento de una variable en python
num1 +=1
num2 +=2
num3 +=2.5
print(f'valor num1 = {num1}')
print(f'valor num2 = {num2}')
print(f'valor num3 = {num3}')

# Caso especial de multiplicacion en pyton
# cuando tenemos un caso de doble 2**3 asterico(signo de multiplicaion) 
# el primer número(lado izquierdo) se multiplica asi mismo 
# la cantidad de veces qui indique 
# el número del lado derecho veamos!

num4 = 8**3
print(f'nel valor de num4 = {num4}')
