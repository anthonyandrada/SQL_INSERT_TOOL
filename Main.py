#!/usr/bin/env python
'''
Created on Mar 20, 2017

@author: aandrada92
'''
from insert import InsertTool
import os

if __name__ == '__main__':
    prompt = '> '
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print ("SQL Insert Statement Creator Created by Anthony Andrada")
    print ("Please enter the filename: ")
    file_name = input(prompt)
    file_path = dir_path + "/" + file_name
    print ("Please enter the table name: ")
    tableName = input(prompt)
    I = InsertTool(file_path)
    I.process(tableName)
