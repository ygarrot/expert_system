
#
# This example shows how to write a basic calculator with variables.
#

from lark import Lark, Transformer, v_args


try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass


calc_grammar = """
    ?start: sum
    ?sum: product
        | sum "+" product   -> and
        | sum "|" product   -> or
    ?product: atom
        | product "^" atom  -> xor
    ?atom: LETTER           -> var
         | "(" sum ")"
         | LETTER "=>" sum -> assign_var
    %import common.LETTER
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
        print(name, value)
        self.vars[name] = value
        return value

    def var(self, name):
        if (self.vars.get(name) == None):
           self.vars[name] = 0
        return self.vars[name]


calc_parser = Lark(calc_grammar, parser='lalr', transformer=CalculateTree())
calc = calc_parser.parse


def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc(s))


def test():
    print(calc("A + B | T => B").pretty())
    # print(calc_parser.transforme())


if __name__ == '__main__':
    test()
    # main()
