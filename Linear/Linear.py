def BuscaLinear ():
    k = 1
    vetor = [10,2,3,4,5]
    select = int(input("numero buscado: "))
    for i in range (0, len(vetor)):
        if select == vetor[i]:
            print("O elemento esta na posição: ",(i+1))
            k =k+1
    if k ==1:
        print("Elemento não encontrado")

BuscaLinear()