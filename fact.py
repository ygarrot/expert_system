import config

def check_fact(key, state=False):

    if (config.fact_dict.get(key) == None):
        config.fact_dict[key] = Fact(state, key)

class Fact:

    def __init__(self, state = False, key = 0):
        self.trees = list()
        self.key = key
        self.state = state

    def get_state(self, computer):
        config.glob = True
        #TODO Change that lul
        for tree in self.trees:
            self.state |= tree[1] * computer.apply_func(tree[0])
        return self.state
