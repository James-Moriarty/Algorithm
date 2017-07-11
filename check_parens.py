import quene

def check_parens(text):
    parens = '()[]{}'
    open_parens = '({['
    oppsite = {')' : '(', '}' : '{', ']' : '['}

    def get_text(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i],i
            i += 1

    st = quene.SStack()
    for word, i in get_text(text):
        if word in open_parens:
            st.push(word)
        elif st.pop() != oppsite[word]:
            print('unmatching is FOUND at', i, 'for', word)
            return False
    print('All match')
    return True

if __name__ == '__main__':
    text1 = '[]{}(){{{(())}}}'
    text2 = '{}{}({}{}{}){}{[}}'
    text3 = ')('
    text4 = '[{}(){}{[q(w)e]}]'
    check_parens(text1)
    check_parens(text2)
    check_parens(text3)
    check_parens(text4)