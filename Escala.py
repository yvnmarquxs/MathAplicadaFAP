def escalar_objeto(ponto_referencia, ponto_objeto, fator_escala):

    x_referencia, y_referencia = ponto_referencia
    x_objeto, y_objeto = ponto_objeto

    x_novo = x_referencia + (x_objeto - x_referencia) * fator_escala
    y_novo = y_referencia + (y_objeto - y_referencia) * fator_escala

    return (x_novo, y_novo)

ponto_referencia = tuple(map(float, input("Digite as coordenadas do ponto de referência (x, y): ").split(',')))
ponto_objeto = tuple(map(float, input("Digite as coordenadas do objeto (x, y): ").split(',')))

#(exemplo, 2 para escalar para o dobro do tamanho)
fator_escala = float(input("Digite o fator de escala: "))

nova_posicao_objeto = escalar_objeto(ponto_referencia, ponto_objeto, fator_escala)

print("Nova posição do objeto após a escala:", nova_posicao_objeto)

input("Pressione Enter para sair.")
