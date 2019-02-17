import config

def check_fact(key, state=False):

    if (config.fact_dict.get(key) == None):
        config.fact_dict[key] = Fact(state, key)

class Fact:

    def __init__(self, state = False, key = 0, isset=False):
        self.trees = list()
        self.isset = False
        self.mutex_lock = False
        self.key = key
        self.state = state

    def ft_error(self):
        print("infinit loop wtf!!!")
        exit()

    def get_state(self, computer):
        #TODO Change that lul
        if (self.isset == True):
            return True
        if (self.mutex_lock == True):
            self.ft_error()
        self.mutex_lock = True
        config.glob = True
        for idx, tree in enumerate(self.trees):
            new_state = (tree[1] & computer.apply_func(tree[0]))
            if (idx > 0 and new_state != self.state):
                self.ft_error()
            self.state |= new_state 
        self.mutex_lock = False
        return self.state
