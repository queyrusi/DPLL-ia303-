import boolean.boolean
algebra = boolean.BooleanAlgebra()
toto = algebra.parse("!(a & b) | (c & (d & e)) | (!f & !(g & !h))")


def get_subformulas(formula, subformulas_list):
    """gets all subformulas from input formula

    Args:
        formula (boolean.boolean.*): * is OR, AND or NOT
        subformulas_list (list): empty list

    Returns:
        subformulas_list (list): list of all subformulas

    Examples:
        >>>toto = algebra.parse( "~(a&b)|!c")
        >>>subsformulas = get_subformulas(toto,[])
        >>>for subf in subformulas: print(subf)
        (~(a&b))|(c&(d&e))|(~f&(~(g&~h)))
        ~(a&b)
        a&b
        c&(d&e)
        d&e
        ~f&(~(g&~h))
        ~f
        ~(g&~h)
        g&~h
        ~h
    """
    subformulas_list.append(formula)
    for arg in formula.args:
        if isinstance(arg, tuple) or isinstance(arg, list) \
                or isinstance(arg, boolean.AND) \
                or isinstance(arg, boolean.OR) \
                or isinstance(arg, boolean.NOT):
            get_subformulas(arg, subformulas_list)
        elif not isinstance(arg, boolean.Symbol):
            subformulas_list.append(arg)
    return subformulas_list


subformulas = get_subformulas(toto, [])
for subf in subformulas:
    print(subf)


def get_symbols(formula, symbols_list):
    """gets symbols from input formula

    Args:
        formula (boolean.boolean.*): * is OR, AND or NOT
        symbols_list (list): empty list

    Returns:
        symbols_list (list): list of all symbols in formula

    Examples:
        >>>toto = algebra.parse("!(a & b) | (c & (d & e))")
        >>>get_symbols(toto, [])
        [Symbol('a'), Symbol('b'), Symbol('c'), Symbol('d'), Symbol('e')]
    """
    print(symbols_list)
    for arg in formula.args:
        print(str(arg))
        if isinstance(arg, tuple) or isinstance(arg, list)\
                or isinstance(arg, boolean.AND) \
                or isinstance(arg, boolean.OR) \
                or isinstance(arg, boolean.NOT):
            get_symbols(arg, symbols_list)
        elif isinstance(arg, boolean.Symbol) and arg not in symbols_list:
            symbols_list.append(arg)
    return symbols_list


symbols = get_symbols(toto, [])
subformula_symbols = []
clauses = []


# TODO
def tseytin(formula, subformulas):
    """

    Args:
        formula ():
        subformulas ():

    Returns:

    """
    new_symbol_number = 1
    clause = None
    i = 0
    for subformula in get_subformulas(formula, []):
        subformula_symbols.append(
            boolean.boolean.Symbol(str(new_symbol_number))
        )
    while i < len(subformulas):
        x_i = subformula_symbols[i]
        subf_i = subformulas[i].simplify()  # simplify not compulsory
        # left =
        clause = (boolean.AND((boolean.NOT(x_i), subf_i),
                               boolean.NOT(subf_i), x_i))

    return
