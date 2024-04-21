def main():
    while True:
        try:
            x_fiddlesticks, y_fiddlesticks, x_inimigo, y_inimigo, velocidade_inimigo, raio_conjuracao, raio_voo = map(float, input().split())

            deltaX = x_fiddlesticks - x_inimigo
            deltaY = y_fiddlesticks - y_inimigo
            distanciaInicial = ((deltaX ** 2) + (deltaY ** 2)) ** 0.5
            tempo_conjuracao = 1.5
            distanciaFinal = distanciaInicial + (velocidade_inimigo * tempo_conjuracao)
            alcance_maximo = raio_conjuracao + raio_voo

            if (distanciaFinal <= alcance_maximo):
                print("Y")
            else:
                print("N")
        except EOFError:
            break

main()