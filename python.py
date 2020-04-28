"""
Программа Нилова Даниила Лабораторная работа "Обработка массивов" 
"""
import random
N = 100
import random
def qSort ( A ): #Функция быстрой сортировки(вне класса получилось некрасиво, просто в Питоне ООП и рекурсия не очень хотят дружить)
    if len(A) <= 1: return A # (1)
    X = random.choice(A) # (2)
    B1 = [ b for b in A if b < X ] # (3)
    BX = [ b for b in A if b == X ] # (4)
    B2 = [ b for b in A if b > X ] # (5)
    return qSort(B1)+BX+qSort(B2) # (6)
def binSearch (lst, x): #Функция бинарного поиска
	lst.sort()
	p = 0
	r = len(lst) - 1
	answer = None
	while p <= r:
		q = (p + r) // 2
		if lst[q] == x:
			answer = q
			break
		elif lst[q] > x:
			r = q - 1
		elif lst[q] < x:
			p = q + 1

	return answer

class quadSorts(object): #Класс методов квадратичных сортировок
    def __init__(self,a):
        self.a = a
    def bubbleSort(self): #метод класса сортировки пузырьком
      for i in range(N-1):
        for j in range(N-2, i-1, - 1):
            if self.a[j] > self.a[j + 1]:
                self.a[j], self.a[j + 1] = self.a[j + 1], self.a[j]
    def stoneSort(self): #метод класса сортировки камнем
      for i in range(N - 1):
         for j in range(N - i - 1):
             if self.a[j] > self.a[j + 1]:
                 self.a[j], a[j + 1] = self.a[j + 1], self.a[j]
    def selectionSort(self): #метод класса сортировки выбором
        i = 0
        while i < N - 1:
            m = i
            j = i + 1
            while j < N:
                if self.a[j] < self.a[m]:
                    m = j
                j += 1
            self.a[i], self.a[m] = self.a[m], self.a[i]
            i += 1


X = [random.randint(0, N) for i in range(N)]
alg = quadSorts(X)
X = qSort(X)
print(X)
