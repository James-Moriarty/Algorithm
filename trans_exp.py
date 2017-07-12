from quene import *
import back_expression

priority = {'(' : 1, '+' : 3, '-' : 3, '*' : 5, '/' : 5}
infix_operators = '+-*/()'
def trans_exp(expression):

    st = SStack()
    exp = []

    for i in tokens(expression):
        if i not in infix_operators:
            exp.append(i)
        elif st.is_empty() or i == '(':
            st.push(i)
        elif i == ')':
            while not st.is_empty() and st.top() != '(':         
                exp.append(st.pop())
            if st.is_empty():
                raise SyntaxError('missing \'(\'.')
            st.pop()                                             #pop '('
        else:
            while (not st.is_empty() and priority[st.top()] >= priority[i]):
                exp.append(st.pop())
            st.push(i)
    while not st.is_empty():
        if st.top() == '(':
            raise SyntaxError('extra \'(\'.')
        exp.append(st.pop())
    return ' '.join(exp)

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
        
        print(exp[i:j])
        yield exp[i:j]
        
        i = j

if __name__ == '__main__':
    test1 = '(9*6+1)-90/5+1*5'
    y = (9*6+1)-90/5+1*5
    print(y)
    x = trans_exp(test1)
    print(x)
    x = ''.join(x)
    z = back_expression.back_expression(x)
    print(z)