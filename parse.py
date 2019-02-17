import argparse
import traceback
import logging
from InferenceEngine import InferenceEngine
from config import *
import config

try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass

computer = InferenceEngine()
calc_grammar = r"""
    ?start: _LI (imply _LI)+ initial_fact _LI query _LI

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

def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc(s))

def set_fact(tree):
  ifact = tree.find_data("initial_fact")
  for fact in ifact:
     computer.iter_subtree(fact)

def set_trees(tree):
  implies = tree.find_data("imply") 
  for imply in list(implies):
    new_tree = imply.children[0]
    computer.set_state(imply.children[1], new_tree)

def query(tree):
  config.glob = True
  queries = tree.find_data("query") 
  st = str()
  for token in list(queries)[0].children:
    st += str(token)
  computer.print_state(st)


def test(interactive=False):
    calc_parser = Lark(calc_grammar, parser='lalr',
        debug=True, transformer=computer) # Cheat ?
    string = """
    A+!C=>D+D ^ E+E
    =A
    ?E
    """
    print(string)
    try:
        tree = calc_parser.parse(string)
    except Exception as e:
        logging.error(traceback.format_exc())
        return
    print(tree.pretty(pstr))
    set_trees(tree)
    # print("B value", config.fact_dict['B'].get_value(computer))
    query(tree)
    if (interactive == True):
        while True:
           try:
               s = input('> ')
           except EOFError:
               break
           print(calc_parser.parse(s))
           set_trees(tree)
           query(tree)
        
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Smarter expert system you have ever seen')
  parser.add_argument("-i", "--interactive", default=False, action="store_true",
                                       help="interactive expert system")
  args = parser.parse_args()
  test(args.interactive)
  # main()
