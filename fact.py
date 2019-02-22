import sys
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

    def ft_error(self):
        print("infinit loop wtf!!!")
        exit()

    def check_fact(self,fact):
        if (self.key == str(fact)):
            return 1
            print("infinit loop")

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
        #TODO Change that lul
        # if (self.isset == True):
           # return self.state
        if (self.mutex_lock >= 2):
            # self.ft_error()
            return self.state
        self.mutex_lock+=1
        config.glob = True
        for idx, tree in enumerate(self.trees):
            is_set = self.isset is True or idx > 0
            if (self.check_imply(tree[0]) and tree[1] is True):
                sys.exit("infinit loop")
            new_state = computer.apply_func(tree[0])
            new_state = not new_state if tree[1] and new_state else new_state 
            if tree[1] and not new_state:
                continue
            if (tree[2] is False and is_set and new_state != self.state):
                self.ft_error()
            self.state |= new_state
        self.mutex_lock-=1
        return self.state
