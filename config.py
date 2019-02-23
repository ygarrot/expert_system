from lark import Lark, Transformer, v_args, Tree
from InferenceEngine import InferenceEngine
computer = InferenceEngine()
pstr ="\033[1;32m--->\033[0m"
skip = False
glob = False
fact_dict = {}

