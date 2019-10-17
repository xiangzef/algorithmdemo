#排序算法 2-3
import random
#类 排序数组初始化 函数 1.断言函数用法2.随机数标准写法
class SortTestHelper:

    def __init__(self, n, rangL , rangR):
        self.n = n
        self.rangL = rangL
        self.rangR = rangR

    def generaterandomarray(self):
        #1.断言函数用法
        assert self.rangR>self.rangL
        arr = []
        for i in range(self.n):
            #随机数标准写法
            arr.append(random.randint(1,10000)%(self.rangR-self.rangL+1)+self.rangL)

        return  arr


if __name__ == '__main__':
    a = SortTestHelper(20,100,300)
    print(a.generaterandomarray())
