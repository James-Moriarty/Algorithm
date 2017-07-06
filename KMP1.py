'''
    KMP algorithm from data book
    don't understand!!!
    gen_pnext('abbcabcaabbcaa') = [-1,0,0,0,-1,0,2,-1,1,0,0,0,-1,5]
'''

def KMP_matching(t, p, pnext):
    m, n = len(p), len(t)
    i, j = 0, 0
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            i, j = i + 1, j + 1
        else:
            i = pnext[i]
    if i == m:
        print(j - i)
    print('no match\n')

def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m-1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext

if __name__ == '__main__':
    next = gen_pnext('abbcabcaabbcaa')
    print(next)
    KMP_matching('abbcabcaabbcaa','bcaa',next)