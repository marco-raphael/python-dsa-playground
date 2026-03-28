from src.data_structures.array import MyArray
import pytest


def test_array_append_e_acesso():
    arr = MyArray()
    arr.append(10)
    arr.append(20)
    arr.append(30)

    assert len(arr) == 3
    assert arr[0] == 10
    assert arr[1] == 20
    assert arr[2] == 30


def test_array_redimensionamento_automatico():
    arr = MyArray()
    # A capacidade inicial é 1, vamos forçar redimensionamentos
    for i in range(10):
        arr.append(i)

    assert len(arr) == 10
    assert arr[9] == 9
    # Verifica se a capacidade cresceu (deve ser 16 se dobrou: 1->2->4->8->16)
    assert arr._capacity == 16


def test_array_indice_invalido():
    arr = MyArray()
    arr.append("Python")

    # Testa se levanta o erro correto ao acessar índice inexistente
    with pytest.raises(IndexError):
        _ = arr[1]

    with pytest.raises(IndexError):
        _ = arr[-1]


def test_array_heterogeneo():
    #(referências/ponteiros)
    arr = MyArray()
    arr.append(100)  # Int
    arr.append("DSA")  # String
    arr.append([1, 2, 3])  # List

    assert arr[0] == 100
    assert arr[1] == "DSA"
    assert isinstance(arr[2], list)