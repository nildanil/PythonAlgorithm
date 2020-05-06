"""
by Nilov Daniil "Arrays handler"
"""
N = 15000 #const integer varible - size of array
import random as rand
class algorithm(object): #make class Algorithm to ease the use of algorithms of sorts and binary search
    def __init__(self, a):#initialize the atrubute of class, it's the list, that we want to handle
        self.a = a
    def bubbleSort(self): #this is the method of bubble
      for i in range(N-1):
        for j in range(N-2, i-1, - 1):
            if self.a[j] > self.a[j + 1]:
                self.a[j], self.a[j + 1] = self.a[j + 1], self.a[j]
    def stoneSort(self): #this is the method of stone
      for i in range(N - 1):
         for j in range(N - i - 1):
             if self.a[j] > self.a[j + 1]:
                 self.a[j], self.a[j + 1] = self.a[j + 1], self.a[j]
    def selectionSort(self): #this is the method of selection
        for i in range(N - 1):
            nMin = i
            for j in range(i + 1, N):
             if self.a[j] < self.a[nMin]:
                nMin = j
             if i != nMin:
                 self.a[i], self.a[nMin] = self.a[nMin], self.a[i]

    def binSearch(self, x):  #function of binary search(it takes one argument "x")
        self.a.sort()#array must be sorted
        p = 0
        r = len(self.a) - 1
        answer = None
        while p <= r:
            q = (p + r) // 2
            if self.a[q] == x:
                answer = q
                break
            elif self.a[q] > x:
                r = q - 1
            elif self.a[q] < x:
                p = q + 1
        return answer

    def quickSort(self, nStart, nEnd):
        if nStart >= nEnd: return
        L = nStart;
        R = nEnd
        X = self.a[(L + R) // 2]
        while L <= R:
            while self.a[L] < X: L += 1  
            while self.a[R] > X: R -= 1
            if L <= R:
                self.a[L], self.a[R] = self.a[R], self.a[L]
                L += 1;
                R -= 1
        self.quickSort( nStart, R) 
        self.quickSort( L, nEnd)

"""main function(out of class) begins here"""
X = [rand.randint(0, N) for i in range(N)] #filling of array with random element
r = algorithm(X) # "r" is object of class algorithm
r.quickSort(0,N-1)
print(X)
