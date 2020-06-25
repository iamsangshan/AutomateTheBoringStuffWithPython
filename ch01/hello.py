#######################################
# Automate the boring Stuff with Python
#######################################
# Chapter 1
#######################################

import time

# 1. Simple Hello 
print("Hello, Good day!, What's your name?")
name = input()
print("Welcome, "+name+"!")
print("Your name has "+str(len(name))+" characters!\n")
print("What's your age?\n")
age = input()
print("You are "+str(int(age) * 365)+" days old approximately\n")
print("But wait...........\n")
time.sleep(2)
print("Age is just a number!!!!\n\n")
