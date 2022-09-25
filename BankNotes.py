# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 12:42:47 2022

@author: User
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float