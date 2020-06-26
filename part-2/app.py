#### Automate stuff with Python #####

### Part-2 #####

# Dictionary operations #

##get() - get values of the keys, also has a fallback if no key found
import pprint

grocery = {
    "milk": 2,
    "oranges": 12,
    "banana":10,
    "rice":1,
}

print("I have bought "+str(grocery.get("milk", 0))+ " packets of milk today!")
print("I have bought "+str(grocery.get("apples", 0))+ " apples today!")



## keys(), values() and items()

for key in grocery.keys():
    print("The key is "+key)

for value in grocery.values():
    print("The value is "+str(value))

for item in grocery.items():
    print("The item is "+str(item))

#list(dict)
print(list(grocery.keys()))
print(list(grocery.values()))
print(list(grocery.items()))


#setdefault() - adds if and only if not existing already
grocery.setdefault("maggi", 2)
print(grocery)
grocery.setdefault("maggi", 0)

## example of setdefault
print("Enter a message and I'll tell you its character count:\n")
message = input()
count_dict = {}
for character in message: # that's nice n easy
    count_dict.setdefault(character, 0)
    count_dict[character] +=1
pprint.pprint(count_dict)


