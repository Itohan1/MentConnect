#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.SignUp import SignUp

fs = FileStorage()

# All SignUp
all_signup = fs.all(SignUp)
print("All SignUp: {}".format(len(all_signup.keys())))
for signup_key in all_signup.keys():
    print(all_signup[signup_key])

# Create a new SignUp
new_signup = SignUp()
new_signup.name = "Moses"
fs.new(new_signup)
fs.save()
print("New Signup: {}".format(new_signup))

# All SignUp
all_signup = fs.all(SignUp)
print("All SignUp: {}".format(len(all_signup.keys())))
for signup_key in all_signup.keys():
    print(all_signup[signup_key])

# Create another SignUp
another_signup = SignUp()
another_signup.name = "Blizzy"
fs.new(another_signup)
fs.save()
print("Another State: {}".format(another_signup))

# All SignUp
all_signup = fs.all(SignUp)
print("All SignUp: {}".format(len(all_signup.keys())))
for signup_key in all_signup.keys():
    print(all_signup[signup_key])        

# Delete the new SignUp
fs.delete(new_signup)

# All SignUp
all_signup = fs.all(SignUp)
print("All SignUp: {}".format(len(all_signup.keys())))
for signup_key in all_signup.keys():
    print(all_signup[signup_key])
