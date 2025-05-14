# Função que calcula a soma entre vetores 
def somar_vetores(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]

# Função que calcula a subtração entre vetores 
def subtrair_vetores(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]

# Função que calcula a multiplicação por escala entre vetores 
def multiplicar_por_escalar(v, escalar):
    return [v[i] * escalar for i in range(len(v))]

# Função que calcula o produto interno entre vetores 
def produto_interno(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

# Função que calcula o produto vetorial entre vetores 
def produto_vetorial(v1, v2):
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

# Função que calcula o produto misto entre vetores 
def produto_misto(v1, v2, v3):
    return (
        v1[0] * (v2[1] * v3[2] - v2[2] * v3[1]) -
        v1[1] * (v2[0] * v3[2] - v2[2] * v3[0]) +
        v1[2] * (v2[0] * v3[1] - v2[1] * v3[0])
    )