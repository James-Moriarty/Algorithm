'''
    队列的实现，先进先出
    采用顺序表实现
    当出现益处现象时自动扩大列表的长度
'''

class QueneUnderFlow(ValueError):
    pass

class SQuene():
    def __init__(self,init_len = 8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0 
        self._num = 0
    
    def is_empty(self):
        return self._num == 0 
    
    def peek(self):                     #The subject which is in the quene at the first
        if self.is_empty():
            raise QueneUnderFlow
        return self._elems[self._head]

    def dequene(self):
        if self.is_empty():
            raise QueneUnderFlow
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enquene(self,e):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0  