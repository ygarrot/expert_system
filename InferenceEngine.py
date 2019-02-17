from fact import Fact, check_fact
from Ft_op import Ft_op
from config import *
import config

@v_args(inline=True)    # Affects the signatures of the methods
class InferenceEngine(Transformer):

    def iter_subtree(self, fact_tree):
        for fact in fact_tree.children:
            self.set_fact(str(fact))

    def set_fact(self, *string):
        for letter in string:
           self.assign_var(letter, True)

    def print_state(self, string):
        for letter in string:
          print(letter, '=', self.var(letter))

    def apply_func(self, tree):
        if (isinstance(tree, Tree) == False):
            return self.var(str(tree)) 
        else:
            return getattr(Ft_op, tree.data)(self.apply_func(tree.children[0]),
                    self.apply_func(tree.children[1] if len(tree.children) > 1 else 0))

    def assign_var(self, name, state):
        config.fact_dict[name] = Fact(state=state, key=name, isset=True)
        return state

    def var(self, name):
        if (config.glob != True):
          return name
        if (config.fact_dict.get(name) == None):
          config.fact_dict[name] = Fact(key=name)
        # config.fact_dict[name].mutex_lock = False
        return config.fact_dict[name].get_state(self)

    def set_choices(self,tree):
        if (isinstance(tree, Tree) == False):
            return str(tree)
        else:
            return tree.pretty().replace('\n', '')

    def ask_choice(self, tree):
            choices = [self.set_choices(tree.children[0]), self.set_choices(tree.children[1])]
            choice = 0
            while choice not in [ '0', '1']:
                choice = input(str('would you like to choose {'+ choices[0]+ '} or {'+ choices[1]+ '}\n'))
            return choice

    def set_state(self, tree, op_tree, is_not=False):
        if (isinstance(tree, Tree) == False):
            check_fact(str(tree))
            config.fact_dict[str(tree)].trees.append((op_tree, is_not))
        elif (tree.data == 'ft_and'):
            self.set_state(tree.children[0], op_tree, is_not)
            self.set_state(tree.children[1], op_tree, is_not)
        elif (tree.data == 'ft_not'):
            self.set_state(tree.children[0], op_tree, not is_not)
        elif (tree.data == 'ft_or'):
            choice = self.ask_choice(tree)
            self.set_state(tree.children[int(choice)], op_tree, is_not)
        elif (tree.data == 'ft_xor'):
            choice = self.ask_choice(tree)
            #TODO change that
            self.set_state(tree.children[int(choice)], op_tree, False)
            self.set_state(tree.children[(not int(choice))], op_tree, True)
