#######################################
# Automate the boring Stuff with Python
#######################################
# Chapter 1 
# Self learning from Python Documentation
#######################################

# Absolute
"""
print('find absolute of the number')
print('Enter any number\n')
num1 = input()
print("Absolute number is "+str(abs(float(num1))))
"""

#All
## check if all elements are True
## In dict, check if all keys are 'True'
"""
fruits_dict =  {
    1: "Apple",
    1: "Oranges",
    1: "Peach",
}
print("Healthy fruit basket? \n")
x = all(fruits_dict)
if(x):
    print("yes!")
else:
    print('no')

"""

#Any
## check if any elements is True
## In dict, check if any key is 'True'
fruits_dict =  {
    1: "Apple",
    1: "Oranges",
    0: "Peach",
}
print("Healthy fruit basket? \n")
x = any(fruits_dict)
if(x):
    print("yes!")
else:
    print('no')

# ASCII - printable version of any object 
print(ascii(fruits_dict))

