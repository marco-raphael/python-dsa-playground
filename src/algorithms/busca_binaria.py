def busca_binaria(lista: list, alvo: int) -> int:
    baixa = 0
    alta = len(lista) -1

    while baixa <= alta:
        meio = (baixa + alta) // 2
        chute = lista[meio]
        if chute == alvo:
            return meio
        if chute > alvo:
            alta = meio - 1
        else:
            baixa = meio + 1
    return -1

