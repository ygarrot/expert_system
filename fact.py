import config

def check_fact(key):
    if (config.fact_dict.get(key) == None):
        config.fact_dict[key] = Fact(value=True)

class Fact:

    def __init__(self, value = False):
        self.trees = list()
        self.value = value

    def get_value(self):
        config.glob = True
        for tree in self.trees:
            computer.apply_func(tree)
        return self.value
