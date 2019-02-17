import argparse
from lark import Lark, Transformer, v_args, Tree
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
  queries = list(tree.find_data("query"))
  if (len(queries) <= 0):
    return
  st = str()
  for token in queries[0].children:
    print(token)
    st += str(token)
  computer.print_state(st)


def test(interactive=False):
    if (interactive == True):
      interactive_m.interactive()
      return
    calc_parser = Lark(calc_grammar, parser='lalr',
        debug=True, transformer=computer)
    string = """
    A=>!B
    E=>A|D
    A+!C=>D+D ^ E+E
    =AY
    ?EACD
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
                
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Smarter expert system you have ever seen')
  parser.add_argument("-i", "--interactive", default=False, action="store_true",
                                       help="interactive expert system")
  args = parser.parse_args()
  test(args.interactive)
  # main()
