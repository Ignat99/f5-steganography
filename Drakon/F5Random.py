#!/usr/bin/env python
# coding: utf-8


# Символы Юникод

import F5Random

# Autogenerated with DRAKON Editor 1.31
class PythonF5Random(F5Random):




    def __init__(self, password):
        #item 103
        random.seed(password)


    def get_next_byte(self):
        #item 72
        return random.randint(-128, 127)


