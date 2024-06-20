import numpy as np 
# Criando um array Numpy a partir de uma lista 
array = np.array([1,2,3,4,5])
#imprimindo o array
print("\nArray Inicial: ",array)

#Acessando um elemento especifico do array 
elemento= array[2] #Acessa o 3° elemento
print("\nAcessou o elemento: ",elemento)

#Array bidimensional
array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\nArray bidimensional: ",array_2d)

#Acessando um elemento específico de um array bidimensional
elemento_2d = array_2d[1,2] #acessa o elemento na linha1, coluna2
print("\nO elemento é: ",elemento_2d)

#Soma de arrays 
array_1 = np.array([1,2,3])
array_2 = np.array([4,5,6])
soma = array_1 + array_2
#Realiza a soma linha --> coluna
print(f"\nA soma é: {soma}")

#Multiplicação de arrays: 
multiplicacao = array_1 * 2
# ou (multiplicacao = array_1 * array_2)
print(f"\nMultiplicação: {multiplicacao}")

#Divisão:
divisao =  array_1/array_2
print("\nA divisão é: ",divisao)

#Calculando a Média:
array = np.array([1,2,3,4,5])
media = np.mean(array)
print("\nA média é: ",media)

# Calculando a soma dos elementos de um array
soma = np.sum(array)
print("\nA Soma dos elementos é: ",soma)

# Calculando o desvio padrão de um array
desvio_padrao = np.std(array)
print("\nO Desvio Padrao: ",desvio_padrao)


# Selecionando elementos com índice específico
array = np.array([1, 2, 3, 4, 5])

selecao_indices = array[1:4]  # Seleciona elementos do índice 1 ao 3 (exclusivo)
print("\nIndicies: ",selecao_indices)

# Selecionando elementos com base em uma condição
array = np.array([1, 4, 2, 5, 3])

selecao_condicao = array[array > 3]  # Seleciona elementos maiores que 3
print("\nelementos selecionados: ",selecao_condicao)


# Transpondo um array (trocando linhas e colunas)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

transposta = array_2d.T  # Transpõe o array
print("\nTransposta: \n", transposta)


# Concatenando arrays horizontalmente (linhas)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

concatenacao_h = np.hstack((array1, array2))
print("\nconcatenação X: \n",concatenacao_h)

# Concatenando arrays verticalmente (colunas)
concatenacao_v = np.vstack((array1, array2))
print("\nconcatenação Y: \n",concatenacao_v)
