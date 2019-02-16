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
        | xor "^" or        -> xor
    ?or: and
        | or "|" and        -> or
    ?and: atom
        | and "+" atom      -> and
    ?atom: UCASE_LETTER     -> var
        | "!" atom         -> not
        | "(" xor ")"

    ?initial_fact: "=" UCASE_LETTER+ -> initial_fact
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
  # if (t.data == var)
    # return var.get_value()
  # if (t.data == op)
    # return func_tab[op](children1, children2)
  # else
    # error
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

def set_trees(tree)
  implies = tree.find_data("imply")
  for imply in implies:
    print(imply)
    
 

def test():
    calc_parser = Lark(calc_grammar, parser='lalr', debug=True, transformer=computer) # Cheat ?
    string = """#we
    S +S => S #wewe
    =QWE
    ?SAL\n"""
    print(string)
    try:
        tree = calc_parser.parse(string)
    except Exception as e:
        logging.error(traceback.format_exc())
        return
    config.glob = True
    print(tree.pretty(pstr))
    subtrees = list(tree.iter_subtrees())
    set_trees(tree)
    # for subtree in (subtrees):
    #   try:
    #     subtree.iter_subtrees()
    #   except:
    #     print("couldn't .sub")
    #   print(subtree.pretty(pstr))

if __name__ == '__main__':
   test()
    # main()
