"""
PROVA A - Fundamentos de Python para IA
Duração: 90 minutos | Valor Total: 100 pontos

Instruções:
- Preencha as funções abaixo implementando a lógica solicitada.
- Você é responsável por testar o seu próprio código. Sinta-se à vontade para 
  criar chamadas de teste no final do arquivo para garantir que a lógica funciona.
- Quando terminar, faça o commit e o push para o repositório.
"""

# ==============================================================================
# Questão 1: Manipulação de Dicionário (20 pontos)
# ==============================================================================
# Dado um texto (string), retorne um dicionário onde as chaves são as palavras 
# e os valores são o número de vezes que cada palavra aparece no texto.
texto = "python é legal python é poderoso"
def contar_frequencia(texto):
        palavras = texto.split()
        contagem = {}

        for palavra in palavras:
            if palavra in contagem:
                contagem[palavra] += 1
            else:
                contagem[palavra] = 1

        return contagem

# ==============================================================================
# Questão 2: Funções Lambda e Map (20 pontos)
# ==============================================================================
# Dada uma lista de números inteiros, utilize a função `map` em conjunto com
# uma função `lambda` para criar e retornar uma nova lista onde cada elemento
# é o quadrado do valor original.

numeros = [ 1, 2, 3, 4, 5, 6, 7]
def elevar_ao_quadrado(numeros):
    quadrada = list(map(lambda x: x ** 2, numeros))
    return quadrada




# ==============================================================================
# Questão 3: Funções Lambda e Filter (20 pontos)
# ==============================================================================
# Dada uma lista de nomes, utilize a função `filter` e uma função `lambda`
# para retornar uma lista apenas com os nomes que possuem 3 letras ou menos.

nomes = ['Joao', 'Ian', 'Diego', 'Bruna', 'Teo']
def filtrar_nomes_curtos(nomes):
        menor = list(filter(lambda x: len(x) <= 3, nomes))
        return menor

# ==============================================================================
# Questão 4: Recursão (20 pontos)
# ==============================================================================
# Crie uma função recursiva que calcule a soma de todos os números numa lista.
soma = [1, 67, 41, 9, 8]
def soma_recursiva(lista, tamanho):
        if tamanho < 0:
            return 0
        return lista[tamanho - 1] + soma_recursiva(lista, tamanho - 1)


# ==============================================================================
# Questão 5: Teoria aplicada à IA (20 pontos)
# ==============================================================================
# "Na preparação de dados para modelos de Machine Learning, é comum evitarmos
# o uso extensivo de laços `for` tradicionais em Python, dando preferência a
# abordagens funcionais (como map/filter) ou bibliotecas vetorizadas.
# Explique, com as suas palavras, por que essa prática é adotada e qual a vantagem
# das funções lambda nesse contexto."

RESPOSTA_Q5 = """
Essa prática é adotada para economizar código e deixar a resposta mais rapida, de modo que as abordagens map e filter 
facilitam a compreensão do código. A principal vantagem das lambdas 
é de não precisar definir uma função completa para fazer uma tarefa fácil...
"""

if __name__ == "__main__":
    print(contar_frequencia(texto))
    print(elevar_ao_quadrado(numeros))
    print(filtrar_nomes_curtos(nomes))
    print(soma_recursiva(soma, 5))






