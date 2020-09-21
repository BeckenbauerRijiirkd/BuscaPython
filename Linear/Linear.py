def BuscaLinear ():
    k = 1
    vetor = [10,2,3,4,5]
    selecionado = int(input("numero buscado: "))
    for i in range (0, len(vetor)):
        if selecionado == vetor[i]:
            print("O elemento esta na posição: ",(i+1))
            k =k+1
    if k ==1:
        print("Elemento não encontrado")

BuscaLinear()