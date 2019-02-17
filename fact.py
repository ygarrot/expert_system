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

    def get_state(self, computer):
        #TODO Change that lul
        if (self.isset == True):
            return self.state
        if (self.mutex_lock == 2):
            self.ft_error()
        self.mutex_lock+=1 
        config.glob = True
        for idx, tree in enumerate(self.trees):
            new_state = computer.apply_func(tree[0])
            new_state = not new_state if tree[1] else new_state
            if (idx > 0 and new_state != self.state):
                self.ft_error()
            self.state |= new_state 
        self.mutex_lock-=1
        return self.state
