#排序算法 2-3
import random

class SortTestHelper:

    def __init__(self, n, rangL , rangR):
        self.n = n
        self.rangL = rangL
        self.rangR = rangR

    def generaterandomarray(self):
        assert self.rangR>self.rangL
        arr = []
        for i in range(self.n):
            arr.append(random.randint(1,10000)%(self.rangR-self.rangL+1)+self.rangL)

        return  arr


if __name__ == '__main__':
    a = SortTestHelper(20,100,300)
    print(a.generaterandomarray())
