import traceback
import logging
from lark import Lark, Transformer, v_args

try:
  input = raw_input   # For Python2 compatibility
except NameError:
  pass

fact_dict = {}

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

    ?initial_fact: "=" UCASE_LETTER+
    ?query: "?" UCASE_LETTER+

    _LI: (_COMMENT | LF)
    _COMMENT: /#[^\n].*\n/

    %import common.UCASE_LETTER
    %import common.NUMBER
    %import common.WS_INLINE
    %import common.LF
    %ignore WS_INLINE
    %ignore _COMMENT
"""

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
  from operator import __and__, __or__, __xor__, __not__
    number = bool

    def set_fact(self, string):
      for letters in string:
        fact_dict[letters] = True

    def get_fact_state(self, string):
      for letters in string:
        print(fact_dict[letters].get_value())

    def assign_var(self, name, value):
      fact_dict[name] = value
        return value

    def var(self, name):
      if (fact_dict.get(name) == None):
        fact_dict[name] = 0
        return fact_dict[name]

calc_parser = Lark(calc_grammar, parser='lalr', debug=True)
#, transformer=CalculateTree()) # Cheat ?
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
    # subtrees = list(tree.iter_subtrees())
     # for subtree in (subtrees):
                          #   t.children = tree.children[0]
 #   for token in tree.children[1]
 #       if (type(toke  == common.LETTER)
 #           if (!fact_tree[token])
 #               fact_tree[token].children[] = tree;
 #           tree.children[1][k].children = tree.children[0]
 #   tree.data = tree.children[1];
 #   delete(tree.children[1]);
  #  for instr in tree.children:
   # 	run_instruction(instr)

if __name__ == '__main__':
  test()
    # main()
