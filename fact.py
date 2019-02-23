import sys
from user import *
from lark import Tree
import config

def check_fact(key, state=False):

    if (config.fact_dict.get(key) == None):
        config.fact_dict[key] = Fact(state, key)

class Fact:

    def __init__(self, state = False, key = 0, isset=False):
        self.trees = list()
        self.isset = isset
        self.mutex_lock = 0
        self.key = key
        self.state = state

    def check_fact(self,fact):
        if (self.key == str(fact)):
            return 1

    def remove_tree(self, tree, idx, computer):
        choice = 'w'
        st = ("<=>" if tree[2] else "=>") + ('!' if tree[1] else '') + self.key
        while choice not in ['y', 'n']:
            choice = input(str("There is an error in operation, would you like to remove this one ? {"
                + set_choices(tree[0]) + st+ "} y/n?\n"))
        if (choice == 'n'):
            sys.exit('infinit loop')
        self.trees.pop(idx)
        return self.get_state(computer)
        
    def check_imply(self,tree):
        ret = 0
        if (isinstance(tree, Tree)):
            fact = tree.find_data("query")
            for truc in fact:
                ret = self.check_fact(fact)
        else:
            ret = self.check_fact(tree)
        return ret

    def get_state(self, computer):
        if (self.mutex_lock >= 2):
            return self.state
        self.mutex_lock += 1
        config.glob = True
        for idx, tree in enumerate(self.trees):
            is_set = self.isset is True or idx > 0
            if (self.check_imply(tree[0]) and tree[1] is True):
                return self.remove_tree(tree, idx, computer)
            new_state = computer.apply_func(tree[0])
            if tree[1] and not new_state:
                continue
            new_state = not new_state if tree[1] and new_state else new_state 
            if (tree[2] is False and is_set and new_state != self.state):
                return self.remove_tree(tree, idx, computer)
            self.state |= new_state
        self.mutex_lock -= 1
        return self.state
