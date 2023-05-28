#Fonte: https://github.com/kelvins/Algoritmos-e-Estruturas-de-Dados/blob/main/src/python/busca_binaria.py

class BinarySearch:
    def __init__(self):
        self.comparisons = 0
    def getComparisons(self):
        return self.comparisons
    def search(self, valor, vetor, esquerda, direita):
        meio = int((esquerda + direita) / 2)
        if esquerda <= direita:
            self.comparisons += 1
            if valor > vetor[meio]:
                esquerda = meio + 1
                return self.search(valor, vetor, esquerda, direita)
            elif valor < vetor[meio]:
                direita = meio - 1
                return self.search(valor, vetor, esquerda, direita)
            return meio
        return -1