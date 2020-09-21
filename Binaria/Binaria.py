def BuscaBinaria():
    select = int(input("Numero: "))
    vetor = [1,2,3,4,5,6,7,8,9,10]
    inicio = 0
    meio = ((len(vetor))//2)

    fim = vetor[(len(vetor)-1)]
    print(meio)
    
    while inicio <= fim:
        if select == vetor[meio]:
            print("Elemento encontrado")
        

BuscaBinaria()