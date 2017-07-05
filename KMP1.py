'''
    KMP algorithm from data book
    don't understand!!!
    gen_pnext('abbcabcaabbcaa') = [-1,0,0,0,-1,0,2,-1,1,0,0,0,-1,5]
'''

def KMP_matching(t, p, pnext):
    m, n = len(p), len(t)
    i, j = 0, 0
    while i< m and j < m:
        if i == -1:
            i, j = i + 1, j + 1
        elif t[j] == p[i]:
            j, i = j + 1, i + 1
        else:
            i = pnext[i]

    if i == m:
        return j - i
    return -1

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
