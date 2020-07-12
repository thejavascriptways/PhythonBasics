## creating your own functions ##

def mean(mylist):
    the_mean = sum(mylist)/len(mylist)
    return the_mean
print(mean([1,2,3,4,5]))

## notice the types of the functions and built in funtctions/methods
print(type(mean), type(sum))

def lengther(lst):
    number = len(lst)
    return number
print(lengther([1,2,3,4,5,6,7,8,9]))

def squareArea(l):
    area = l*l
    return area
print(squareArea(5))

def ConvertOuncesToMillilitres(v):
    vol_in_mill = v * 29.57353
    return vol_in_mill
print(ConvertOuncesToMillilitres(100))

## Conditionals ##

def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:    
        the_mean = sum(value)/len(value)
    return the_mean

print(mean([1,2,3,4,5]))
print(mean({"morning": 40.5, "noon":90.5,"evening":65.6}))

def passwordController(password):
    if len(password) < 8:
        return False
    else: 
        return True
print( passwordController("mypass"))
print( passwordController("mypassword"))

def checkTemp(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
print(checkTemp(15))

def tempCheck(temp):
    if temp > 25:
        return "HOT"
    elif temp >= 15 and temp <= 25:
        return "WARN"
    else:
        return "COLD"

print(tempCheck(12))
print(tempCheck(30))
print(tempCheck(17))

# # # Summary: Functions and Conditionals
# # # In this section you learned to:

# #Define a function:
# def cube_volume(a):
#     return a * a * a

# #Write a conditional block:
# message = "hello there"
# if "hello" in message:
#     print("hi")
# else:
#     print("I don't understand")

# #Write a conditional block of multiple conditions:
# message = "hello there"
# if "hello" in message:
#     print("hi")
# elif "hi" in message:
#     print("hi")
# elif "hey" in message:
#     print("hi")
# else:
#     print("I don't understand")

# #Use the and operator to check if both conditions are True at the same time:
# x = 1
# y = 1
# if x == 1 and y==1:
#     print("Yes")
# else:
#     print("No")
# #Output is Yes since both x and y are 1.

# #Use the or operator to check if at least one condition is True:
# x = 1
# y = 2
# if x == 1 or y==2:
#     print("Yes")
# else:
#     print("No")
# #Output is Yes since x is 1.

# #Check if a value is of a certain type with:
# isinstance("abc", str)
# isinstance([1, 2, 3], list)
# #or

# type("abc") == str
# type([1, 2, 3]) == lst


