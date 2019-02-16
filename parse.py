import traceback
import logging
from tree_transformer import CalculateTree
from config import *
import config

try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass

computer = CalculateTree()
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
        | "!" atom         -> not
        | "(" xor ")"

    ?initial_fact: "=" UCASE_LETTER+ -> set_fact
    ?query: "?" UCASE_LETTER+ ->query

    _LI: (_COMMENT | LF)
    _COMMENT: /#[^\n].*\n/

    %import common.UCASE_LETTER
    %import common.NUMBER
    %import common.WS_INLINE
    %import common.LF
    %ignore WS_INLINE
    %ignore _COMMENT
"""

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

def set_fact(tree):
  ifact = tree.find_data("initial_fact")
  for fact in ifact:
     computer.iter_subtree(fact)

def set_trees(tree):
  implies = tree.find_data("imply")
  tree = tree.find_data("imply") 
  lchild = list(list(implies)[0].children[1].iter_subtrees_topdown())
  new_tree = list(tree)[0].children[0]
  for imply in list(lchild):
    computer.set_value(imply, new_tree)
  # print(config.fact_dict)
  print(config.fact_dict['C'].get_value(computer))

def test():
    calc_parser = Lark(calc_grammar, parser='lalr', debug=True, transformer=computer) # Cheat ?
    # cal_parser.transformer = 0
    string = """#we
    A + B => C + D + E#wewe
    =ADE
    ?SAL\n"""
    print(string)
    try:
        tree = calc_parser.parse(string)
    except Exception as e:
        logging.error(traceback.format_exc())
        return
    # config.glob = True
    print(tree.pretty(pstr))
    set_trees(tree)
    # subtrees = list(tree.iter_subtrees())
    # for subtree in (subtrees):
    #   try:
    #     subtree.iter_subtrees()
    #   except:
    #     print("couldn't .sub")
    #   print(subtree.pretty(pstr))

if __name__ == '__main__':
   test()
    # main()
