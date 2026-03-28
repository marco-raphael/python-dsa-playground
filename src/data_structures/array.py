import ctypes


class MyArray:
    """Uma simulação de Array de baixo nível usando a biblioteca ctypes."""

    def __init__(self):
        self._n = 0  # Número real de elementos
        self._capacity = 1  # Capacidade total de memória alocada
        self._A = self._make_array(self._capacity)  # O "bloco contínuo" de memória

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('Índice fora do intervalo')
        return self._A[k]  # Acesso O(1)

    def append(self, obj):
        """Adiciona um elemento ao final, redimensionando se necessário."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)  # Estratégia de dobrar a capacidade

        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """O processo de 'instanciar outro array com novo espaço."""
        B = self._make_array(c)  # Aloca novo espaço contíguo maior
        for k in range(self._n):
            B[k] = self._A[k]  # Copia os dados do antigo para o novo (O(n))
        self._A = B  # Atualiza a referência
        self._capacity = c

    def _make_array(self, c):
        """Retorna um novo array bruto (raw) com capacidade c."""
        return (c * ctypes.py_object)()