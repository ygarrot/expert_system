from fact import Fact, check_fact
from config import *
import config

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import __and__, __or__, __xor__, __not__
    number = bool

    def iter_subtree(self, fact_tree):
        print (config.glob)
        for fact in fact_tree.children:
            self.set_fact(str(fact))

    def set_fact(self, *string):
        for letter in string:
           print(letter)
           self.assign_var(letter, True)

    def get_fact_state(self, *string):
        if (config.glob != True):
          return string
        for letter in string:
          print(letter)
          print(config.fact_dict[letter])

    def apply_func():
        if (isinstance(tree, Tree) == False):
            check_fact(str(tree))
            return config.fact_dict[str(tree)].get_value()
        else:
            return get_attr(ft_op, tree.data)(tree.children[0], tree.children[0])

    def assign_var(self, name, value):
        config.fact_dict[name] = Fact(value)
        return value

    def var(self, name):
        if (config.glob != True):
          return name
        if (config.fact_dict.get(name) == None):
          config.fact_dict[name] = Fact()
        return config.fact_dict[name].get_value()

    def set_value(self, tree, op_tree):
        if (isinstance(tree, Tree) == False):
            check_fact(str(tree))
            config.fact_dict[str(tree)].trees.append(op_tree)
        elif (tree.data == 'and'):
            self.set_value(tree.children[0], op_tree)
            self.set_value(tree.children[1], op_tree)
        return
    # def set_tree(self, tree)
        # for 
    
