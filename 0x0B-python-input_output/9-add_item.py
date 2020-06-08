#!/usr/bin/python3
"""
Script that adds all arguments to a python list and then
saves them into a file
"""
from sys import argv
from os import path
save = __import__("7-save_to_json_file").save_to_json_file
load = __import__("8-load_from_json_file").load_from_json_file


filename = "add_item.json"
args = argv[1:]
my_list = []

# Creating file if doesn't exist and adding the list in it
if path.exists(filename):
    my_list = load(filename)
save(my_list + args, filename)
