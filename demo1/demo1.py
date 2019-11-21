#排序算法 2-3
import random
import time

#类 排序数组初始化 函数 1.断言函数用法2.随机数标准写法

#这个类中全是 辅助计算的函数

class SortTestHelper:
                # 生成n个参数的数组 下限L 上限R
    def __init__(self, n, rangL , rangR):
        self.n = n
        self.rangL = rangL
        self.rangR = rangR

    def generaterandomarray(self):
        #1.断言函数用法
        assert self.rangR>self.rangL
        arr = []
        for i in range(self.n):
            #随机数标准写法 生成随机数与标准差R-L取余 加上下限L
            arr.append(random.randint(1,10000)%(self.rangR-self.rangL+1)+self.rangL)
        return  arr
        '''以下是冒泡排序'''
    def selectionsort_bubblesort(self,arr):#冒泡
        for i in range(1,len(arr)):
            for j in range(0,len(arr)-i):#为什么是0 到 n-i 原因是把最大的推到最后 这里是0-18 循环不能超过数组长度
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr
        '''以下是冒泡排序反向冒泡'''
    def selectionsort_bubblesort_2(self,arr):#冒泡2
        for i in range(1,len(arr)):
            for j in range(i,len(arr)):#反推要怎么写 这里的入参2是数组长度 所以是1-19 1，19
                if arr[len(arr)-j+i-1] < arr[len(arr)-1-j+i-1]:#最后一个 和前一个比 j = 1就是19 与18比 后一个比前一个小 提到前面来 直到与0比
                    arr[len(arr)-1-j+i-1],arr[len(arr)-j+i-1] = arr[len(arr)-j+i-1],arr[len(arr)-1-j+i-1]
        return arr#之前错误的原因是因为  第二次循环没有从最末段开始

    def selectionsort(self, arr):#选择排序
        for i in range(1,len(arr)):
            minIndex = i-1
            for j in range(i,len(arr)):#为什么上面的是 len(arr)-i 下面是len(arr)
                if arr[j]< arr[minIndex]:
                    minIndex = j
            arr[i-1] , arr[minIndex] =arr[minIndex] , arr[i-1]
        return arr
    #   以下是插入排序


    def insertionsort(self,arr):
        for i in range(1,len(arr)): #从1开始到arr长度n前一位结束 也就是n-1 数组是0到n-1
            for j in range(i,0,-1):#倒叙 从i开始比较 与i-1 ,i-1 与i-2 直到
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1] = arr[j-1],arr[j]
                else:
                    break
        return arr#最初疑惑我的问题是为什么需要在比较不成功的地方跳出 ，后来想明白了因为比较不成功的部分前面是已经整理过的序列

    def insertionsort_better(self, arr):
        for i in range(1,len(arr),1):
            e = arr[i]
            for j in range(i,0,-1):
                if  arr[j-1]> e:
                    arr[j]= arr[j-1]
                else:
                    break
            arr[j] = e
        return  arr

    def issorted(self,arr):#判断传入的数组是否有序
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                return False
        return True


if __name__ == '__main__':
    a = SortTestHelper(6,100,300)
    #打印
    arr=a.generaterandomarray()
    print(arr)


    t0 = time.time()
    arr = a.insertionsort_better(arr)       #优化插入排序
    #arr = a.insertionsort(arr)              #插入排序
    #arr=a.selectionsort_bubblesort_2(arr)   #反冒泡
    t1 = time.time()


    print(arr)
    if a.issorted(arr):
        print('排序成功')
        print(t1 - t0)
    else:
        print('排序失败')

    del a ,arr