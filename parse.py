
#
# This example shows how to write a basic calculator with variables.
#

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

    def __init__(self):
        self.vars = {}

    def assign_var(self, name, value):
        self.vars[name] = value
        return value

    def var(self, name):
        if (self.vars.get(name) == None):
           self.vars[name] = 0
        return self.vars[name]

    def test(self):
        return self.vars


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
    string = "A + B + T | B => B"
    print(string)
    # print(calc(string))
    print(calc(string).pretty())
    # print(calc_parser.transforme())


if __name__ == '__main__':
    test()
    # main()
