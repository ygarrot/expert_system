import traceback
import logging
from tree_transformer import CalculateTree
from config import glob, fact_dict
from lark import Lark, Transformer, v_args

try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass

calc_grammar = r"""
    ?start: (imply _LI)+ initial_fact _LI query _LI

    ?imply: xor "=>" xor -> imply
        | xor "<=>" xor -> iff
    ?xor: or
        | xor "^" or  -> xor
    ?or: and
        | or "|" and   -> or
    ?and: atom
        | and "+" atom   -> and
    ?atom: UCASE_LETTER        -> var
         | "!" atom      -> not
         | "(" xor ")"

    ?initial_fact: "=" UCASE_LETTER+ -> set_fact
    ?query: "?" UCASE_LETTER+ -> get_fact_state

    _LI: (_COMMENT | LF)
    _COMMENT: /#[^\n].*\n/

    %import common.UCASE_LETTER
    %import common.NUMBER
    %import common.WS_INLINE
    %import common.LF
    %ignore WS_INLINE
    %ignore _COMMENT
"""
calc_parser = Lark(calc_grammar, parser='lalr', debug=True
, transformer=CalculateTree()) # Cheat ?
calc = calc_parser.parse

def run_instruction(t):
    try:
        print(t.data)
        for instr in t.children:
            run_instruction(instr)
    except:
         return

def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc(s))

def test():
    string = """A <=> S + A
#we
    S => S + S#wewe
    =QWE
    ?SAL\n"""
    print(string)
    try:
        tree = calc(string)
    except Exception as e:
        logging.error(traceback.format_exc())
        return
    print(tree.pretty("\033[1;32m--->\033[0m"))
    subtrees = list(tree.iter_subtrees())
    for subtree in (subtrees):
      print(subtree)

if __name__ == '__main__':
   test()
    # main()
