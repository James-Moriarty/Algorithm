'''
    KMP算法python实现
    通用算法为朴素算法，即从第一个字母进行匹配，若出现不匹配，则将模式串向后移动一个位置，从第一个开始匹配
    朴素算法程序(simple_match())
    用于字符串查找，朴素算法的复杂度取决于目标串与模式串，复杂度太高
    因此采用KMP算法，基本思想为找到失配位之前的最长公共前后缀来减少匹配的次数
'''

def simple_match(m,n):          #m为模式串，n为目标串
    m1, n1 = len(m), len(n)
    i, j = 0, 0
    if m1 > n1:
        print('Wrong Input\n')
    count = 1
    while j <= n1 - m1:
        if m[i] == n[j]:
            i += 1 
            j += 1
        else:
            i = 0 
            j = j - i + 1
        if i >= m1 - 1 and m[i] == n[j]:
            print(m,n)
            print('the %s position: %s\n' % (count,j-m1+1))
            i = 0
            j = j - i + 1
            count += 1
            #print(count)
    if count == 1:
        print('No match for %s in %s\n' % (m,n))

def KMP(m,n):               #m为模式串，n为目标串  主算法
    next[] = get_next(m)
    m1, n1 = len(m), len(n)
    i, j = 0, 0
    while j <= n1 - m1:
        if m[i] == n[j]:
            i += 1
            j += 1
        else:
            i = i-next[i-1]

def get_next(m):            #构造next[]
    i, k, m = 0, -1, lem(m)
    next[] = -1 * m
    while i < m - 1:
        if k == -1 or p[i] == p [k]:
            i, k = i + 1, k + 1
            next[i] = K
        else:
            k = next[k]
    return next
            
if __name__ == '__main__':
    n = 'qwesfxasefaefaf'
    m = 'fxa'
    p = 'fa'
    o = 'fxs'
    simple_match(m,n)
    simple_match(p,n)
    simple_match(o,n)