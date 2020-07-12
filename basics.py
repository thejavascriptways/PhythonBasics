# import datetime

#     print ("The date and time is: ", datetime.datetime.now() )
# # print(datetime.datetime.now())

# ##Variables##

#     mynow = datetime.datetime.now()
#     print (mynow)

#     mynum = 100
#     mytext = "Hello World"
#     print(mynum,mytext)

# ##Simple Types##

#     x=10
#     y="10"
#     z=10.1
#     print (x+x)
#     print (y+y)
#     print (x+z)
#     print ( type(x), type(y), type(z))


# ##List Types##
#     stds =["Mile", "Mia", "Nile"]
#     print(stds)
#     grades = [10,12,15]
#     print (grades)

# #List with range
#     print(list(range(1,10)))
#     print(list(range(1,10,2)))

# ## Type attributes##
#     print(dir(str))
#     print(dir(int))
#     print(dir(float))
#     print(dir(list))

# #method to find built ins in python
#     print(dir(__builtins__))

# dictionary

    # day_temperatures = {"morning": 40.5, "noon":90.5,"evening":65.6}
    # print (day_temperatures)

#tuple
        # color_codes = ( (10,13,24),(34,23,45),(54,65,76))

        # print (color_codes)

#complex dictionary

    # day_temperatures = {"morning": (12.2,12.4,56.8), "noon": (12.2,812.4,565.8), "evening": (112.2,12.4,34.8)}

    # print (day_temperatures)

    # Keys of a dictionary can be extracted with:

    # phone_numbers.keys()
    # Values of a dictionary can be extracted with:

    # phone_numbers.values()
    # Tuples represent arrays of values that are not to be changed during the course of the program:

    # vowels = ('a', 'e', 'i', 'o', 'u')
    # one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    # To find out what attributes a type has:

    # dir(str)
    # dir(list)
    # dir(dict)
    # To find out what Python builtin functions there are:

    # dir(__builtins__)
    # Documentation for a Python command can be found with:

    # help(str)
    # help(str.replace)
    # help(dict.values)

## More operations on Types    

    # dir(list)

# use help(list.<methodname>) to see how to use that method

    # 'append', 'clear', 'copy', 'count', 'extend',
    # 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# #accessing list
    # serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
    # print(serials[2])

#acessing ans clicing list    

    # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # print(letters[1:4])
    # Answer
    # ['b', 'c', 'd']

    # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # print(letters[:3])
    # Answer 
    # ['a', 'b', 'c']

    # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # print(letters[-3:])
    # Answer
    # ['e', 'f', 'g']

# #     Summary: Positive/Negative Indexes, Slicing
# # In this section you learned that:

    # Lists, strings, and tuples have a positive index system:
        # ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        # 0      1      2      3      4      5      6

    # And a negative index system:
        # ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        # -7     -6     -5     -4     -3     -2     -1

    # In a list, the 2nd, 3rd, and 4th items can be accessed with:
        # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        # days[1:4]
        # Output: ['Tue', 'Wed', 'Thu']

    # First three items of a list:
        # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        # days[:3]
        # Output:['Mon', 'Tue', 'Wed'] 

    # Last three items of a list:
        # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        # days[-3:]
        # Output: ['Fri', 'Sat', 'Sun']

    # Everything but the last:
        # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        # days[:-1] 
        # Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

    # Everything but the last two:
        # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        # days[:-2] 
        # Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 

    # A single in a dictionary can be accessed using its key:
        # phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
        # phone_numbers["Marry Simpsons"]
        # Output: '+423998200919'

    