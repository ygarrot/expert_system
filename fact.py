import config

def check_fact(key, value=False):

    if (config.fact_dict.get(key) == None):
        config.fact_dict[key] = Fact(value, key)

class Fact:

    def __init__(self, value = False, key = 0):
        self.trees = list()
        self.key = key
        self.value = value

    def get_value(self, computer):
        config.glob = True
        #TODO Change that lul
        for tree in self.trees:
            self.value |= computer.apply_func(tree)
        return self.value
