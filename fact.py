import config

def check_fact(key):
    if (config.fact_dict.get(key) == None):
        config.fact_dict[key] = Fact(value=True)

class Fact:

    def __init__(self, value = False):
        self.trees = list()
        self.value = value

    def get_value(self):
        for tree in self.trees:
            self.value = tree()
        return self.value
