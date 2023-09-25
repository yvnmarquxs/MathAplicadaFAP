def refletir_objeto(ponto, eixo):

    x, y = ponto

    if eixo == 'x':
        return (x, -y)
    elif eixo == 'y':
        return (-x, y)
    else:
        print("Eixo inválido. Escolha 'x' para reflexão no eixo x ou 'y' para reflexão no eixo y.")
        return ponto


ponto = tuple(map(float, input("Digite as coordenadas do ponto (x, y): ").split(',')))

eixo_reflexao = input("Digite o eixo de reflexão ('x' ou 'y'): ")

nova_posicao_ponto = refletir_objeto(ponto, eixo_reflexao)

print("Nova posição do ponto após a reflexão:", nova_posicao_ponto)

input("Pressione Enter para sair.")
