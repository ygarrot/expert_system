import config
from config import *
def set_choices(tree):
    if (isinstance(tree, Tree) == False):
        return str(tree)
    else:
        return tree.pretty().replace('\n', '')

def ask_xor(tree):
    if (config.skip is True):
        return 0
    choices = [set_choices(tree.children[0]), set_choices(tree.children[1])]
    choice = 0
    while choice not in [ '0', '1']:
        choice = input(str('Would you like to choose 0:{'+ choices[0]+ '} or 1:{'+ choices[1]+ '}\n'))
    return int(choice)

def ask_or(tree):
    if (config.skip is True):
        return 0
    choices = [set_choices(tree.children[0]), set_choices(tree.children[1])]
    choice = 0
    while choice not in [ '0', '1', '2']:
        choice = input(str('Would you like to choose 0:{'+ choices[0]+ '} or 1:{'+ choices[1]+ '} or 2: for both\n'))
    return int(choice)
