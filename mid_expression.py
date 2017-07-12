from quene import *

priority = {'(' : 1, '+' : 3, '-' : 3, '*' : 5, '/' : 5}
infix_operators = '+-*/()'

class ESStack(SStack):
    def depth(self):
        return len(self._elem)
def mid_expression(exp):
    data = ESStack()
    op = ESStack()

    for x in tokens(exp):
        if x not in infix_operators:
            data.push(x)
        elif op.is_empty() or x == '(':
            op.push(x)
        elif x == ')':
            while not op.is_empty() and op.top() != '(':
                a1 = float(data.pop())
                b1 = float(data.pop())
                c1 = caculate(a1, b1, op.pop())
                data.push(c1)
            if op.is_empty():
                raise SyntaxError('Missing \'(\'')
            op.pop()
        else:
            while (not op.is_empty() and priority[op.top()] >= priority[x]):
                a2 = float(data.pop())
                b2 = float(data.pop())
                c2 = caculate(a2, b2, op.pop())
                data.push(c2)
            op.push(x)
    while not op.is_empty() or data.depth() != 1:
        a3 = float(data.pop())
        b3 = float(data.pop())
        c3 = caculate(a3, b3, op.pop())
        data.push(c3)
        if data.depth() == 1 and op.depth() != 0:
            raise SyntaxError('Extra operator')
    return data.pop()
            
        
def caculate(a,b,x):
    print('%s %s %s' % (b, x, a))
    if x == '+':
        c = b + a
    elif x == '-':
        c = b - a
    elif x == '/':
        if a == 0:
            raise ValueError('dividend can\' be zero')
        c = b / a
    elif x == '*':
        c = b * a
    else:
        raise SyntaxError('wrong operator')
    return c
         
def tokens(exp):
    i, longity = 0, len(exp)
    while i < longity:
        while i < longity and exp[i].isspace():
            i += 1
        if i >= longity:
            break
        if exp[i] in infix_operators:
            #print(exp[i])                       #为运算符的情况
            yield exp[i]
            i += 1
            continue

        j = i + 1

        while (j < longity and not exp[j].isspace() and exp[j] not in infix_operators):             #为运算对象的时候以多位数字时
            if ((exp[j] == 'e' or exp[j] == 'E') and j+1 < longity and exp[j + 1] == '-'):          #处理负指数
                j += 1
            j += 1
        
        #print(exp[i:j])
        yield exp[i:j]
        
        i = j

if __name__ == '__main__':
    test1 = '(9*6+1)-90/5+1*5'
    print((9*6+1)-90/5+1*5)
    result = mid_expression(test1)
    print(result)