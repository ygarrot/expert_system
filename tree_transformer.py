from fact import Fact, check_fact
from ft_op import ft_op
from config import *
import config

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import __and__, __or__, __xor__, __not__
    number = bool

    def iter_subtree(self, fact_tree):
        for fact in fact_tree.children:
            self.set_fact(str(fact))

    def set_fact(self, *string):
        for letter in string:
           print(letter)
           self.assign_var(letter, True)

    def get_fact_state(self, string):
        for letter in string:
          print(letter, '=', self.var(letter))

    def apply_func(self, tree):
        if (isinstance(tree, Tree) == False):
            return self.var(str(tree)) 
        else:
            return getattr(ft_op, tree.data)(self.apply_func(tree.children[0]),
                    self.apply_func(tree.children[1]))

    def assign_var(self, name, value):
        config.fact_dict[name] = Fact(value=value, key=name)
        return value

    def var(self, name):
        if (config.glob != True):
          return name
        if (config.fact_dict.get(name) == None):
          config.fact_dict[name] = Fact(key=name)
        return config.fact_dict[name].get_value(self)

    def set_value(self, tree, op_tree):
        if (isinstance(tree, Tree) == False):
            check_fact(str(tree))
            config.fact_dict[str(tree)].trees.append(op_tree)
        elif (tree.data == 'ft_and'):
            self.set_value(tree.children[0], op_tree)
            self.set_value(tree.children[1], op_tree)
        return
