class fact:

    def __init__(self, trees = {}, value = False):
        self.tree = trees
        self.value = value

    def get_value(self):
        for tree in self.trees:
            self.value = tree()
        return self.value