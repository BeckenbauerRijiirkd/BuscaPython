def BuscaBinaria():
    import time
    
    vetor =[]
    tamanho = int(input("quantidade de elementos: "))
    for i in range (0, tamanho):
        print("Elemento", i+1)
        digito = int(input())
        vetor.append(digito)
    print(vetor)
    select = int(input("Numero a Ser Buscado: "))

    inicio = 0

    fim = (len(vetor)-1)
    t1 = time.time()
    while inicio <= fim:
        meio = ((inicio+fim)//2)
        if select == vetor[meio]:
            print("Elemento encontrado na posição: ", (meio+1))
            break
        if select < vetor[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    tempoExec = time.time() - t1
    print("Tempo de execução: {:.5f} segundos".format(tempoExec))

        
        
BuscaBinaria()