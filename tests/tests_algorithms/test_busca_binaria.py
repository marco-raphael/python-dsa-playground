from src.algorithms.busca_binaria import busca_binaria

def test_busca_binaria_sucesso():
    minha_lista = [1, 3, 5, 7, 9]
    assert busca_binaria(minha_lista, 3) == 1
    assert busca_binaria(minha_lista, 7) == 3

def test_busca_binaria_nao_encontrado():
    minha_lista = [1, 3, 5, 7, 9]
    assert busca_binaria(minha_lista, -1) == -1