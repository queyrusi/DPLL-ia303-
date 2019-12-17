IA3030 : implémentation de DPLL
====

### Auteurs
Zhi Zhou, <zhi.zhou@ensta-paris.fr>
 Simon Queyrut,  <simon.queyrut@ensta-paris.fr>
 
 [@zroykhi](https://github.com/zroykhi), [@queyrusi][github] 

[github]: http://github.com/queyrusi

### Sujet
Implémentation simple d'un solveur SAT DPLL et d'une transformation de Tseytin

## Contenu du package
+ `simple_dpll.py` avec l'algorithme DPLL et sa fonction de propagation en dessous
+ `tseytin_1.py` et `tseytin_2.py` qui implémentent une transformation de Tseytin 
+ `cnf_files` 

### Usage

transform a string of logic formule into cnf using Tseitin tranformation:
```
python Tseitin_recursive.py --logic '!(p|q|s|t)&z'
```
result will be like `~p&~q&~s&s0&~s2&~s3&~s4&~t&z`

Parse cnf in string to a list of DIMACS format
```
python ParserCNF2Dimacs.py
```
then enter your cnf in the terminal, for example, `~p&~q&~s&s0&~s2&~s3&~s4&~t&z`. It will output the result like `[[-7], [-1], [-4], [2], [-8], [-6], [-5], [-3], [9]]`

find model using dpll
```
python simple_dpll.py
```
then enter your dimacs list, like `[[-7], [-1], [-4], [2], [-8], [-6], [-5], [-3], [9]]`. It will output the result, like `[-5, -2, -6, 4, -9, -3, -7, -8, 1]`

Or you can run all these command in a pipeline:
```
python Tseitin_recursive.py --logic '!(p|q|s|t)&z' | python ParserCNF2Dimacs.py | python simple_dpll.py
```