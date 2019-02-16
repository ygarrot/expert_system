import config

def check_fact(key, value=True):
    if (config.fact_dict.get(key) == None):
        config.fact_dict[key] = Fact(value=False)

class Fact:

    def __init__(self, value = False):
        self.trees = list()
        self.value = value

    def get_value(self, computer):
        config.glob = True
        for tree in self.trees:
            self.value = computer.apply_func(tree)
        return self.value
