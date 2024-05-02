def unconsumed_input():
    """Returns any remaining input from the input file after the last read."""
    rem = fin.read()
    return rem

def lex():
    """Reads the next character from the input, ignoring whitespace characters."""
    global next_token
    while True:
        next_token = fin.read(1)
        if next_token in ['\t', '\n', ' ']:
            pass
        else:
            break

def G():
    """Starts the parsing process and handles the end-of-input and errors."""
    global error
    while True:
        error = False
        lex()
        print('G->E')
        E()
        if next_token == '$' and not error:
            print('success')
            print("-" * 13)
        else:
            print('failure: unconsumed_input:', unconsumed_input())
        if not fin.read(1):
            break

def E():
    """Non-terminal E, entry point for handling expressions starting with term followed by '+' or '-'."""
    global error
    if error:
        return
    print('E->TR')
    T()
    R()

def R():
    """Handles the continuation of expression parsing after the first term, processing '+' and '-'."""
    global error
    if error:
        return
    if next_token == '+':
        print('R->+TR')
        lex()
        T()
        R()
    elif next_token == '-':
        print('R->-TR')
        lex()
        T()
        R()
    else:
        print('R->e')

def T():
    """Non-terminal T, starts parsing of a term that could be followed by '*' or '/'."""
    global error
    if error:
        return
    print('T->FS')
    F()
    S()

def S():
    """Handles multiplication and division operations within a term."""
    global error
    if error:
        return
    if next_token == '*':
        print('S->*FS')
        lex()
        F()
        S()
    elif next_token == '/':
        print('S->/FS')
        lex()
        F()
        S()
    else:
        print('S->e')

def F():
    """Parses factors, which could be an expression in parentheses, a variable, or a number."""
    global error
    if error:
        return
    if next_token == '(':
        print('F->(E)')
        lex()
        E()
        if next_token == ')':
            lex()
        else:
            error = True
            print('error: unexpected token', next_token)
            print('unconsumed input:', unconsumed_input())
            return
    elif next_token in ['a', 'b', 'c', 'd']:
        print('F->M')
        M()
    elif next_token in ['0', '1', '2', '3']:
        print('F->N')
        N()
    else:
        error = True
        print('error: unexpected token', next_token)
        print('unconsumed input:', unconsumed_input())

def M():
    """Parses variables, which are expected to be one of 'a', 'b', 'c', or 'd'."""
    global error
    if error:
        return
    if next_token in ['a', 'b', 'c', 'd']:
        print('M->', next_token, sep='')
        lex()
    else:
        error = True
        print('error: unexpected token', next_token)
        print('unconsumed input:', unconsumed_input())

def N():
    """Parses numbers, which are expected to be one of '0', '1', '2', '3'."""
    global error
    if error:
        return
    if next_token in ['0', '1', '2', '3']:
        print('N->', next_token, sep='')
        lex()
    else:
        error = True
        print('error: unexpected token', next_token)
        print('unconsumed input:', unconsumed_input())

error = False
next_token = '%'
if __name__ == '__main__':
    fin = open('input.txt', 'r')
    G()
