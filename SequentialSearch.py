#Fonte: https://github.com/kelvins/Algoritmos-e-Estruturas-de-Dados/blob/main/src/python/busca_sequencial.py

class SequentialSearch:
    def __init__(self):
        self.comparisons = 0
    def getComparisons(self):
        return self.comparisons
    def sequential_search(self, value, array):
        for i in range(0, len(array)):
            self.comparisons += 1
            if array[i] == value:
                return i
        return -1