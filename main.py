# FILE: /type_annotations/main.py

# pip install mypy
# pip install flake8

var_string: str = 'Hi, friend.' #A:
var_integer: int = 123456
var_float: float = 1.44
var_boolean: bool = False
var_set: set = {1, 2, 3}
var_list: list = []
var_tuple: tuple = (1, 2, 3)
var_dict: dict = {}

var_string = 1 #1:
print(var_string)

def sum_sum(x: int, y: int, z: float) -> float:
    return x + y + z
print(sum_sum(1, 2, 3))
'''
(...)
'''

# ------------------------------------------------------------------
#1: Não apontou que o tipo era incompatível com #A:.

# Edson Copque | https://linktr.ee/edsoncopque
