#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""dpll_main.py
Functions and main for a dictionary-based-implementation of DPLL.

Check https://github.com/queyrusi/DPLL-ia303- for updates!
"""

debug = True


def unit_propagate(formula, model):
    """

    Args:
        formula (list):

            [{1: False, -3: None}, {2: None}]

        model (dict):

            {1: None, 3: False}

    Returns:

    """
    # wrong = False
    cursor = 0
    if (not has_empty_clauses(formula)) and has_unit_clauses(formula):
        for clause in formula:
            for literal in model:
                # avoid missing key errors
                if literal in clause.keys() and model[literal] is not None:
                    clause[literal] = model[literal]
                if -literal in clause.keys() and model[literal] is not None:
                    clause[-literal] = not model[literal]
            formula[cursor] = clause
            cursor += 1
        symbol, truth_value = None, None
        if has_unit_clauses(formula):
            unit_literal = get_literal_from_unit_clause(get_unit_clause(formula))
            symbol, truth_value = unit_literal.popitem()
            model[symbol] = truth_value
            if debug:
                print(formula)
                print("[+] propagate ", symbol)
        unit_propagate(formula, model)
    return formula

# if literal in clause.keys():  # avoid missing key errors
#     wrong = clause[literal] != model[literal]
#     if wrong:
#         print('WRONG')
# if -literal in clause.keys():  # opposite check
#     wrong = clause[-literal] == model[literal]
#     if wrong:
#         print('WRONG')


def has_empty_clauses(formula):
    """

    Args:
        formula ():

    Returns:

    """
    has_empty = None
    for clause in formula:
        if is_empty(clause):
            has_empty = True
            break
    return has_empty


def is_empty(clause):
    """

    Args:
        clause ():

    Returns:

    """
    return list(clause.values()).count(True) == 0 and\
        list(clause.values()).count(None) == 0


def get_literal_from_unit_clause(unit_clause):
    """Returns unit literal in natural form (NOT operators are dismissed)

    Args:
        unit_clause (dict):

    Returns:

    Examples:
        >>>get_literal_from_unit_clause( {4: False, -5: None, 3: False} )
        {5: False}
        >>>get_literal_from_unit_clause( {2: False, 1: None} )
        {1: True}

    """
    unit_literal = {}
    unit_symbol = [l for l in unit_clause.keys() if unit_clause[l] is None][0]
    if unit_symbol <= -1:
        unit_literal[-unit_symbol] = False
    elif unit_symbol >= 1:
        unit_literal[unit_symbol] = True
    return unit_literal


def has_unit_clauses(formula):
    """

    Args:
        formula ():

    Returns:

    """
    return len([clause for clause in formula if is_unit(clause)]) > 0


def get_unit_clause(formula):
    """True if formula has unit clauses. Returns first unit clause.

    Args:
        formula ():

    Returns:
        unit clause (dict)

    Examples:
        >>> get_unit_clause([{2: None}, {4: False, -5: None}]
        {2: None}
    """
    first_unit_clause = None
    if has_unit_clauses(formula):
        first_unit_clause = [clause for clause in formula if is_unit(clause)][0]
    return first_unit_clause



def is_unit(clause):
    """True if clause is unit

    Args:
        clause (dict):
            {1: True, -3: None}

    Returns:

    Examples:
        >>> is_unit({1: True, -3: None})
        False
        >>> is_unit({1: False, -3: None, 2: False})
        True

    """
    return list(clause.values()).count(None) == 1 and \
        not list(clause.values()).count(True)


def clause_is_consistent(clause):  # dispensable
    """

    Args:
        clause (dict):

    Returns:

    """
    is_consistent = None
    for literal in clause:
        if -literal in clause.keys():
            is_consistent = clause[-literal] == clause[literal]
    return is_consistent
