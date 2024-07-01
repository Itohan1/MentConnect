#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.sign import SignUp

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(SignUp)))

first_state_id = list(storage.all(SignUp).values())[0].id
print("First state: {}".format(storage.get(SignUp, first_state_id)))
