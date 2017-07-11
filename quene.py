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