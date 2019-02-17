import config

def check_fact(key, state=False):

    if (config.fact_dict.get(key) == None):
        config.fact_dict[key] = Fact(state, key)

class Fact:

    def __init__(self, state = False, key = 0):
        self.trees = list()
        self.mutex_lock = False
        self.key = key
        self.state = state

    def get_state(self, computer):
        if (self.mutex_lock == True):
            print("infinit loop wtf!!!")
            exit()
        self.mutex_lock = True
        config.glob = True
        #TODO Change that lul
        for tree in self.trees:
            self.state |= (tree[1] & computer.apply_func(tree[0]))
        self.mutex_lock = False
        return self.state
