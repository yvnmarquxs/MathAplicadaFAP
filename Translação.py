def transladar_objeto(x, y, direcao, distancia):

    if direcao == 'cima':
        y += distancia
    elif direcao == 'baixo':
        y -= distancia
    elif direcao == 'esquerda':
        x -= distancia
    elif direcao == 'direita':
        x += distancia

    return (x, y)

x_inicial, y_inicial = map(int, input("Digite as coordenadas iniciais (x, y): ").split(','))

direcao = input("Digite a direção ('cima', 'baixo', 'esquerda', 'direita'): ")
distancia = int(input("Digite a distância: "))

nova_posicao = transladar_objeto(x_inicial, y_inicial, direcao, distancia)

print("Nova posição do objeto:", nova_posicao)

input("Pressione Enter para sair.")