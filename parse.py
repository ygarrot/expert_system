from lark import Lark, Transformer, v_args

try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass

fact_dict = {}

calc_grammar = """
    ?start: imply | initial_fact | query

    ?imply: xor "=>" xor -> imply
        | xor "<=>" xor -> iff
    ?xor: or
        | xor "^" xor  -> xor
    ?or: and
        | xor "|" xor   -> or
    ?and: atom
        | xor "+" xor   -> and
    ?atom: UCASE_LETTER        -> var
         | "!" atom      -> not
         | "(" xor ")"

    ?initial_fact: "=" UCASE_LETTER+
    ?query: "?" UCASE_LETTER+

    %import common.UCASE_LETTER
    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
    %ignore /#.*/
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

calc_parser = Lark(calc_grammar, parser='lalr')
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
    string = "A + B + B | T + B => B"
#    string = "A | B | A <=> B"
#    string = "A => S"
#    string = "=ABG"
#    string = "# ?ABG"
#    string = "C + B => C# => C      # C AND B implies C"
#    string = "C + R"
    print(string)
    try:
        tree = calc(string)
    except:
        print("Wrong file format")
        return
    print(tree.pretty("\033[1;32m--->\033[0m"))
    print(tree.children[0].pretty("\033[1;32m--->\033[0m"))
    print(tree.children[1].pretty("\033[1;32m--->\033[0m"))

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
