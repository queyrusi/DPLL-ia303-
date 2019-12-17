#!/usr/bin/python
#  -*- coding: utf-8 -*-

"""sat_solve.py
Module to execute to SAT solve dimacs (.cnf) file.

Check github.com/queyrusi/DPLL-ia303- for updates!
"""

import simple_dpll
import dimacs_parser
import sys

__name__ = "main"


if __name__ == "main":
    dimacs_file = sys.argv[1]
    lines = dimacs_parser.dimacs2dimacs_list(dimacs_file)
    f = dimacs_parser.dimacs_list2formula(lines)
    simple_dpll.dpll_wrap(f)
