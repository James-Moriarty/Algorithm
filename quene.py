'''
    栈的实现，采用顺序表实现，名字quene但实际为栈的实现
    由于之后的应用中
'''


class StackUnderFlow(ValueError):
    pass

class SStack():
    def __init__(self):
        self._elem = []
    
    def is_empty(self):
        return self._elem == []

    def top(self):
        if self._elem == []:
            raise StackUnderFlow('in SStack.top()')
        return self._elem[-1]

    def push(self,elem):
        self._elem.append(elem)

    def pop(self):
        if self._elem == []:
            raise StackUnderFlow('in SStack.pop()')
        return self._elem.pop()
    
#i = SStack()
#i.pop()