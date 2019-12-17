#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""simple_dpll.py
Functions and main for a dictionary-based-implementation of DPLL.

Check github.com/queyrusi/DPLL-ia303- for updates!
"""

import sys
import copy
import ast

debug = False  # tODO
show_steps = False


def dpll(formula, model):
    """

    Args:
        formula ():
        model ():

    Returns:

    """
    unit_propagate(formula, model)
    new_f1 = copy.deepcopy(formula)
    new_f2 = copy.deepcopy(formula)
    if len(new_f1) == 0:
        if show_steps:
            print("[+] SAT")
        # print(new_f1)
        print(model)
        return True
    if [] in new_f1:
        if show_steps:
            print("[-] UNDO")
        return False
    literal = new_f1[0][0]
    if show_steps:
        print("[+] DECISION ON: ", literal)
    model_union_l = copy.deepcopy(model)
    model_union_l.append(literal)
    model_union_not_l = copy.deepcopy(model)
    model_union_not_l.append(-literal)
    if debug:
        print("MODEL WITH l: ", model_union_l)
    if dpll(new_f1, model_union_l):
        if show_steps:
            print("[+] SAT")
        return True
    if debug:
        print("[debug] MODEL WITH NOT l: ", model_union_not_l)
        print("[debug] FORMULA WITH NOT l: ", new_f2)
    return dpll(new_f2, model_union_not_l)


def unit_propagate(formula, model):
    """reduce

    Args:
        formula ():
        model ():

    Returns:

    """
    if [] in formula:  # has empty clause
        return
    has_unit_clause = False
    cursor = 0
    while cursor != len(formula) and len(model) != 0:
        clause = formula[cursor]
        kept = True
        for literal in model:
            if literal in clause:
                if debug:
                    print("[debug] literal ", literal)
                    print("in clause so clause is removed: ", clause)
                kept = False
                formula.remove(clause)
                break
            elif -literal in clause:
                if debug:
                    print("[debug] literal ", -literal)
                    print("so occurences will be removed: ", clause)
                while -literal in clause:
                    clause.remove(-literal)
                formula[cursor] = clause
        if kept:
            cursor += 1

    for clause in formula:
        if len(clause) == 1:
            has_unit_clause = True
            model.append(clause[0])
            if show_steps:
                print("[+] PROPAGATE ON: ", clause[0])
            break
    if has_unit_clause:
        unit_propagate(formula, model)
    return formula, model

def dpll_wrap(formule):
    dpll(formule, [])

def check_sat(formula, model):
    """

    Args:
        formula ():
        model ():

    Returns:

    """
    unit_propagate(formula,model)
    return False

if __name__ == "__main__":
    formule_in_list = [[-2], [-1], [-4], [-3], [-6], [-5]] # just an example
    try:
        formule_in_list = ast.literal_eval(sys.stdin.readline())
    except Exception as e:
        print('Error', e)   
    dpll_wrap(formule_in_list)