import argparse
from lark import Lark, Transformer, v_args, Tree, UnexpectedInput
import traceback
import logging
from config import *
import config
import interactive_m

try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass

calc_grammar = r"""
    ?start: (imply _LI)+ initial_fact _LI query _LI

    ?imply: xor "=>" xor    -> imply
        | xor "<=>" xor     -> iff
    ?xor: or
        | xor "^" or        -> ft_xor
    ?or: and
        | or "|" and        -> ft_or
    ?and: atom
        | and "+" atom      -> ft_and
    ?atom: UCASE_LETTER     -> var
        | "!" atom         -> ft_not
        | "(" xor ")"

    ?initial_fact: "=" UCASE_LETTER* -> set_fact
    ?query: "?" UCASE_LETTER+ ->query

    _LI: (_COMMENT | LF+)
    _COMMENT: /#[^\n].*\n/

    %import common.UCASE_LETTER
    %import common.NUMBER
    %import common.WS_INLINE
    %import common.LF
    %ignore WS_INLINE
    %ignore _COMMENT
"""

def set_fact(tree):
    ifact = tree.find_data("initial_fact")
    for fact in ifact:
       computer.iter_subtree(fact)

def set_trees(tree):
    implies = tree.find_data("imply")
    for imply in list(implies):
        new_tree = imply.children[0]
        computer.set_state(imply.children[1], new_tree)
    iffs = tree.find_data("iff")
    for iff in list(iffs):
        new_tree1 = iff.children[0]
        new_tree2 = iff.children[1]
        computer.set_state(iff.children[1], new_tree1)
        computer.set_state(iff.children[0], new_tree2)

def query(tree):
    config.glob = True
    queries = list(tree.find_data("query"))
    if (len(queries) <= 0):
        return
    st = str()
    for token in queries[0].children:
        st += str(token)
    computer.print_state(st)

def test(args):
    if (args.interactive == True):
        interactive_m.interactive()
        return
    calc_parser = Lark(calc_grammar, parser='lalr',
        debug=True, transformer=computer)
    with open(args.path, 'r') as myfile:
            string=myfile.read()
    print(string)
    try:
        tree = calc_parser.parse(string)
    except UnexpectedInput as e:
        print(e)
        return
    set_trees(tree)
    query(tree)

def main():
    parser = argparse.ArgumentParser(description='Smarter expert system you have ever seen')
    parser.add_argument("-i", "--interactive", default=False, action="store_true",
                                       help="interactive expert system")
    parser.add_argument("path", type=str, default=False, help="input file name")
    args = parser.parse_args()
    test(args)

if __name__ == '__main__':
    main()
