import quene

class ESSstack(quene.SStack):
    def depth(self):
        return len(self._elem)
def back_expression(exp):
    operators = '+-*/'
    st = ESSstack()
    exp = exp.split()
    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue
        if st.depth() < 2:
            raise SyntaxError('short of operand(s).')
        a = st.pop()
        b = st.pop()

        if x == '+':
            c = b + a
        if x == '-':
            c = b - a
        if x == '*':
            c = b * a
        if x == '/':
            if a == '0':
                raise SyntaxError('dividend can\' be zero')
            c = b / a
        st.push(c)
    if st.depth() == 1:
        return st.pop()
    raise SyntaxError('extra operand(s)')

if __name__ == '__main__':
    exp = '3 5 - 6 17 4 * + * 3 /'
    '''
        the mid_expression is '(3 - 5) * (6 + 17 * 4) / 3 =  -49.3333333333333
    '''
    result = back_expression(exp)
    print('the result of %s is %s' % (exp,result))