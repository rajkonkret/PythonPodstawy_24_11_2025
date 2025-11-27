# import fun8
#
# fun8.all_params(1, 2, 3, 4)
# # a=1, b=2
# # c=3, d=4

import pakiet
# AttributeError: module 'pakiet' has no attribute 'powitanie'
# pakiet.powitanie()
pakiet.info()

from pakiet import fun

fun.powitanie()  # Hello World

import pakiet.fun as pk  # jako alias

pk.powitanie()  # Hello World
