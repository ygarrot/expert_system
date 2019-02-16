from fact import Fact
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
           self.assign_var(letter, True)

    def get_fact_state(self, *string):
        if (config.glob != True):
          return string
        for letter in string:
          print(letter)
          print(fact_dict[letter])

    def assign_var(self, name, value):
        if (config.glob != True):
          return name
        fact_dict[name] = Fact(value)
        return value

    def var(self, name):
        if (config.glob != True):
          return name
        if (fact_dict.get(name) == None):
           fact_dict[name] = Fact()
        return fact_dict[name].get_value()
