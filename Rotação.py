import math

def rotacionar_objeto(ponto_referencia, ponto_objeto, angulo_graus):

    x_referencia, y_referencia = ponto_referencia
    x_objeto, y_objeto = ponto_objeto

    angulo_radianos = math.radians(angulo_graus)

    x_novo = x_referencia + (x_objeto - x_referencia) * math.cos(angulo_radianos) \
             - (y_objeto - y_referencia) * math.sin(angulo_radianos)
    y_novo = y_referencia + (x_objeto - x_referencia) * math.sin(angulo_radianos) \
             + (y_objeto - y_referencia) * math.cos(angulo_radianos)

    return (x_novo, y_novo)

ponto_referencia = tuple(map(float, input("Digite as coordenadas do ponto de referência (x, y): ").split(',')))
ponto_objeto = tuple(map(float, input("Digite as coordenadas do objeto (x, y): ").split(',')))

angulo_graus = float(input("Digite o ângulo de rotação (em graus): "))

nova_posicao_objeto = rotacionar_objeto(ponto_referencia, ponto_objeto, angulo_graus)

print("Nova posição do objeto após rotação:", nova_posicao_objeto)

input("Pressione Enter para sair.")
