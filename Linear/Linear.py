def BuscaLinear ():
    import time
    k = 1
    vetor =[]
    tamanho = int(input("quantidade de elementos: "))
    for i in range (0, tamanho):
        print("Elemento", i+1)
        digito = int(input())
        vetor.append(digito)
    print(vetor)
    select = int(input("Numero a Ser Buscado: "))
    t1 = time.time()
    for i in range (0, len(vetor)):
        if select == vetor[i]:
            print("O elemento esta na posição: ",(i+1))
            k =k+1
    if k ==1:
        print("Elemento não encontrado")
    tempoExec = time.time() - t1
    print("Tempo de execução: {:.5f} segundos".format(tempoExec))

BuscaLinear()