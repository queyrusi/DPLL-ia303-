import boolean
algebra = boolean.BooleanAlgebra()
toto = algebra.parse("!(a & b) | (c & (d & e)) | (!f & !(g & !h))")


def get_subformulas(formula, subformulas_list):
    """

    Args:
        formula (boolean.boolean.*): * is OR, AND or NOT
        subformulas_list (list): empty list

    Returns:
        subformulas_list (list): list of all subformulas

    """
    subformulas_list.append(formula)
    for arg in formula.args:
        print("TYPE", type(arg))
        if isinstance(arg, tuple) or isinstance(arg, list) \
                or isinstance(arg, boolean.boolean.AND) \
                or isinstance(arg, boolean.boolean.OR) \
                or isinstance(arg, boolean.boolean.NOT):
            print("STRING", str(arg))
            get_subformulas(arg, subformulas_list)
        elif not isinstance(arg, boolean.boolean.Symbol):
            subformulas_list.append(arg)
    return subformulas_list


subformulas = get_subformulas(toto, [])
