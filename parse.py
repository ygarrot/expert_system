fact_dict = {}

from lark import Lark, Transformer, v_args


try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass

calc_grammar = """
    ?start: assign
    ?assign: xor
        | xor "=>" LETTER -> assign_var
    ?xor: or
        | and "^" atom  -> xor
    ?or: and
        | and "|" atom   -> or
    ?and: atom
        | and "+" atom   -> and
    ?atom: LETTER        -> var
         | "!" atom      -> not
         | "(" assign ")" 

    %import common.LETTER
    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""


@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import __and__, __or__, __xor__, __not__
    number = bool

    def assign_var(self, name, value):
        fact_dict[name] = value
        return value

    def var(self, name):
        if (fact_dict.get(name) == None):
           fact_dict[name] = 0
        return fact_dict[name]

    def test(self):
        return fact_dict


calc_parser = Lark(calc_grammar, parser='lalr')
#, transformer=CalculateTree())
calc = calc_parser.parse


def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc(s))

def test():
    string = "A + B + (T | B) => B"
    print(string)
    # print(calc(string))
    tree = calc(string)
    print(tree.pretty())

if __name__ == '__main__':
    test()
    # main()
