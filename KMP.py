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

def KMP_Match(subject,object):               #m为模式串，n为目标串  主算法
    next = get_next(subject)
    m1, n1 = len(subject), len(object)
    i = 0
    for j in range(n1):
        while subject[i] != object[j]:       #如果不相等，
            i = next[i - 1]
        if subject[i] == object[j]:
            i += 1 
        if i == m1:
            print(j - i + 1)
            i = 0               #find all match
            #return True
    return False

def get_next(subject):            #构造next[]
    k, m1 = 0, len(subject)
    next = [0] * m1
    for i in range(1,m1):
        while k > 0 and subject[i] != subject[k]:   #i位置与k位置不相等
            k = next[k-1]               #将k=next[k]，转去考虑前一个更短的保证匹配的前缀
        if subject[i] == subject[k]:
            k = k + 1                   #若匹配则将k+1，即向前走一位
        next[i] = k
    return next
            
if __name__ == '__main__':
    n = 'abbcabcaabbcaa'
    m = 'bcaa'
    p = 'fa'
    o = 'fxs'
    simple_match(m,n)
    #simple_match(p,n)
    #simple_match(o,n)
    next1 = get_next('abbcabcaabbcaa')
    #[0, 0, 0, 0, 1, 2, 0, 1, 1, 2, 3, 4, 5, 1]
    print(next1)
    KMP_Match(m,n)