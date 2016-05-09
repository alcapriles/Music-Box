# -*- coding: utf-8 -*-
"""
Created on Mon May  9 19:18:06 2016

@author: Ana Capriles
"""

import os

os.startfile('teste.ly')

while True:
    if os.path.isfile('teste.pdf'):
        os.startfile('teste.pdf')
        break
