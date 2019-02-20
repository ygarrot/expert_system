from parse import *

interactive_grammar = r"""
    ?start: imply
        | initial_fact | query

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


def interactive():
        calc_parser = Lark(interactive_grammar, parser='lalr',
        debug=True, transformer=computer)
        while True:
           try:
               s = input('> ')
           except EOFError:
               break
           try:
               tree = calc_parser.parse(s)
           except:
               logging.error(traceback.format_exc())
               continue
           if (tree == None):
             continue
           if (tree.data == "imply" or tree.data == "iff"):
                set_trees(tree)
           else:
                query(tree)

