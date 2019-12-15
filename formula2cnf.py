from boolean.boolean import *
algebra = BooleanAlgebra()


def get_subformulas(formula, subformulas_list):
    """gets all subformulas from input formula

    Args:
        formula (boolean.boolean.*): * is OR, AND or NOT
        subformulas_list (list): empty list

    Returns:
        subformulas_list (list): list of all subformulas

    Examples:
        >>>toto = algebra.parse( "~(a&b)|!c")
        >>>subformulas_list = get_subformulas(toto,[])
        >>>for subf in subformulas_list: print(subf)
        (~(a&b))|~c
        ~(a&b)
        a&b
        ~c
    """
    subformulas_list.append(formula)
    for arg in formula.args:
        if isinstance(arg, tuple) or isinstance(arg, list) \
                or isinstance(arg, AND) \
                or isinstance(arg, OR) \
                or isinstance(arg, NOT):
            get_subformulas(arg, subformulas_list)
        elif not isinstance(arg, Symbol):
            subformulas_list.append(arg)
    return subformulas_list


def tseytin(formula):
    """returns a Tseytin transformation of input formul

    Args:
        formula (boolean.boolean.*): * is OR, AND or NOT

    Returns:
        clause.simplify() (boolean.boolean.AND):
            CNF form of input formula with newly introduced formula (due to
            Tseytin transformation) and simplified so that double NOT are
            dismissed

    """
    clause = None
    subformulas_list = get_subformulas(formula, [])
    # on commence par i = 0 :
    subformulas_list.reverse()

    # on crée m variables fraîches x_1, x_2, ... , x_m :
    x = [Symbol("x" + str(i)) for i in range(1, len(subformulas_list) + 1)]
    i = 0

    while i < len(subformulas_list):
        subformula = subformulas_list[i]
        if subformula.operator == '~':  # we encounter NOT
            p = subformula
            equivalence_formula = AND(OR(NOT(p), NOT(x[i])), OR(p, x[i]))
            clause = equivalence_formula if clause is None else \
                AND(clause, equivalence_formula)

        elif subformula.operator == '&':  # we encounter AND
            p = subformula.args[0]
            q = subformula.args[1]
            equivalence_formula = AND(
                OR(NOT(p), NOT(q), x[i]),
                OR(p, NOT(x[i])),
                OR(q, NOT(x[i]))
            )
            clause = equivalence_formula if clause is None else \
                AND(clause, equivalence_formula)

        elif subformula.operator == '|':  # we encounter OR
            p = subformula.args[0]
            q = subformula.args[1]
            equivalence_formula = AND(
                OR(p, q, x[i]),
                OR(NOT(p), x[i]),
                OR(NOT(q), x[i])
            )
            clause = equivalence_formula if clause is None else \
                AND(clause, equivalence_formula)
        i += 1
        subformulas_list = propagate(subformulas_list, subformula, x[i-1], i)
    return clause.simplify()


def propagate(subformulas_list, phi_i, fresh_variable, i):
    """replaces all occurrences of expression phi_i in input list starting at
    element number i included

    Args:
        subformulas_list (list):
        phi_i (boolean.boolean.*): * is OR, AND or NOT
            minimal expression to be replaced by a new variable. It can be of
            form φ = ¬p, φ = p ∨ q or φ = p ∧ q
        fresh_variable (boolean.boolean.Symbol):
            newly introduced variable replacing phi_i
        i (int):

    Returns:
        propagated (list):

    Examples:
        >>>toto = algebra.parse( "~(a&b|!c)|!c")
        >>>subformulas_list = get_subformulas(toto,[])
        >>>subformulas_list.reverse()
        >>>for subf in subformulas_list: print(subf)
        ~c
        ~c
        a&b
        (a&b)|~c
        ~((a&b)|~c)
        (~((a&b)|~c))|~c
        >>>propagated = propagate(subformulas_list, subformulas_list[0],
        ...Symbol('x1'), 1)
        >>>for subf in propagated: print(str(subf))
        ~c
        x1
        a&b
        (a&b)|x1
        ~((a&b)|x1)
        (~((a&b)|x1))|x1
    """
    propagated = subformulas_list[:i]
    for f in subformulas_list[i:]:
        if str(phi_i) in str(f):
            propagated.append(
                algebra.parse(str(f).replace(str(phi_i), str(fresh_variable)))
            )
        else:
            propagated.append(f)
    return propagated


toto = algebra.parse("!(a & b) | (c & (d & e)) | (!f & !(g & !h))")
# minimal_example = algebra.parse("!(p|q|s|t) & !r")
tsey_toto = tseytin(toto)
print(tsey_toto)
