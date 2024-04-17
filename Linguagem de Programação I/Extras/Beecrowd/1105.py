while True:
    try:
        B, N = [int(x) for x in input().strip().split(' ')]

        saldos = [int(x) for x in input().strip().split(' ')]
        saldos.insert(0, 0)

        for _ in range(N):
            devedor, credor, valor = [int(x) for x in input().strip().split(' ')]

            saldos[devedor] -= valor
            saldos[credor] += valor
        
        possivel = True
        for saldo in saldos:
            if(saldo < 0):
                possivel = False
                break
        
        print('S' if possivel else 'N')
    except EOFError:
        break