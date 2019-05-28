from random import choice, choices

def random_symbols(symbols):
    L = choices(list(symbols.keys()), weights=list(symbols.values()), k=1)
    result = ''
    for s in L:
        result += s
    return result


def random_template(N, max_length):
    L = ['{}' for i in range(N)]

    length = 0
    iteration = 1
    while length < max_length and iteration < 500:
        entry = choice(range(len(L)))
        event = choice(range(1, 16))
        if event == 1:
            L[entry] = L[entry].replace('{}', '{} {} ', 1)
        elif event == 2 and len(L)>1:
            L[entry] = '\\frac{' + L[entry] + '}{' + L[entry-1] + '}'
            L[entry-1] = '{} '
        elif event == 3:
            L[entry] = '\\sum_{i={}}^{{}} \\left(' + L[entry] + '\\right)'
        elif event == 4:
            L[entry] = '\\left(' + L[entry] + '\\right)^{' + L[entry-1] + '}'
            L[entry-1] = '{} '
        elif event == 5:
            L[entry] = '\\left(' + L[entry] + '\\right)^\\mbox{It follows that}'
        elif event == 6:
            L[entry] = '\\sqrt{{' + L[entry] + '}}'
        elif event == 7:
            L[entry] = '\\sqrt[{}]{{' + L[entry] + '}}'
        elif event == 8 and '{}' in L[entry]:
            L[entry] = L[entry].replace('{}', L[entry-1], 1)
            L[entry-1] = '{} '
        elif event == 9:
            L[entry] = '\\left(' + L[entry] + '\\right)_{{}}'
        elif event == 10:
            L[entry] = '\\left(' + L[entry] + '\\right)_{' + L[entry-1] + '}'
            L[entry-1] = '{} '
        elif event == 11:
            L[entry] = '\\sum_{i\\in\\mathcal{F}({},{},{})} \\left(' + L[entry] + '\\right)'
        elif event == 12:
            L[entry] = L[entry] + '+' + L[entry-1]
            L[entry-1] = '{} '
        elif event == 13:
            L[entry] = L[entry] + '-' + L[entry-1]
            L[entry-1] = '{} '
        elif event == 14:
            L[entry] = L[entry] + '\\times ' + L[entry-1]
            L[entry-1] = '{} '
        elif event == 15 and len(L) > 3:
            L[entry] = ('\\left[\\begin{array}{cc}'
                     + L[entry] + ' & ' + L[entry-1] + ' \\\\ '
                     + L[entry-2] + ' & ' + L[entry-3]
                     + '\\end{array}\\right]')
            L[entry-1] = '{} '
            L[entry-2] = '{} '
            L[entry-3] = '{} '
        else:
            L[entry] = '\\left(' + L[entry] + '\\right)^{{}}'

        iteration += 1
        length = 0
        for x in L:
            length += len(x)

        print('iteration no.', iteration)
        print('length =', length)
        print(L)

    T = ''
    for x in L:
        T += x
        T += ' '
    return T


def random_math(symbols, max_length, h):
    # higher value of h means a more 'horizontal' equation
    S = random_template(h, int(max_length/2))
    while '{}' in S and len(S) < max_length:
        S = S.replace('{}', random_symbols(symbols), 1)
        print('length =', len(S))
        print(S)
    return S


symbols = {
'x': 9,
'y': 7,
'z': 6,
'\\lambda': 3,
'\\mho': 1,
'\\alpha': 3,
'\\omega': 3,
'\\Omega': 3,
'\\beta': 3,
'\\eta': 3,
'\\Theta': 3,
'\\mu': 4,
'\\zeta': 4,
'\\Phi': 2,
'\\kappa': 2,
'\\sigma': 3,
'\\varepsilon': 3,
'\\Lambda': 2,
'\\mathbb{A}': 2,
'\\mathbb{C}': 3,
'\\mathbb{R}': 4,
'\\mathbb{Z}': 4,
'\\mathbb{N}': 3,
'\\mathbb{P}': 2,
'\\mathbb{Q}': 3,
'\\mathbb{K}': 2,
'\\uparrow': 2,
'\\downarrow': 2,
'\\partial': 3,
'\\hbar': 1,
'\\aleph': 3,
'\\beth': 2,
'\\nabla': 3,
'\\sharp': 1,
'\\cdot': 3,
'\\natural': 1,
'\\triangle': 2,
'\\spadesuit': 3,
'\\diamondsuit': 3,
'\\heartsuit': 3,
'\\clubsuit': 3,
'\\infty': 2,
}

#S = random_symbols(symbols)
S = random_math(symbols, 2500, 4)
#S = random_template(10, 500)
with open('test.txt','w') as file:
    file.write(S)
