"""
by Nilov Daniil "Arrays handler"
"""
N = 100 #const integer varible - size of array
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
    def quickSort(self, l, r): #this is the method of quick sort
        if l >= r:
            return
        else:
            q = rand.choice(self.a[l:r + 1])#random choise of mid between l and r
            i = l
            j = r
            while i <= j:
                while self.a[i] < q:
                    i += 1
                while self.a[j] > q:
                    j -= 1
                if i <= j:
                    self.a[i], self.a[j] = self.a[j], self.a[i]
                    i += 1
                    j -= 1
                    self.quickSort(l, j)
                    self.quickSort(i, r)#recursion in the method

"""main function(out of class) begins here"""
X = [rand.randint(0, N) for i in range(N)] #filling of array with random element
r = algorithm(X) # "r" is object of class algorithm
r.bubbleSort()
r.stoneSort()
r.selectionSort()
r.quickSort(0,N-1)
r.binSearch(8)
print(X)
